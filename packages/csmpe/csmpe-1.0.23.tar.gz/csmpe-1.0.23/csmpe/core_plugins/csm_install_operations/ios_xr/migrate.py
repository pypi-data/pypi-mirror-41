# =============================================================================
# migrate.py - plugin for migrating classic XR to eXR/fleXR
#
# Copyright (c)  2013, Cisco Systems
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
# =============================================================================

import time
import re

from csmpe.plugins import CSMPlugin
from migration_lib import check_exr_final_band, log_and_post_status, run_additional_custom_commands
from csmpe.core_plugins.csm_get_inventory.exr.plugin import get_package, get_inventory
from csmpe.core_plugins.csm_install_operations.utils import update_device_info_udi


XR_PROMPT = re.compile(r'(\w+/\w+/\w+/\w+:.*?)(\([^()]*\))?#')

SCRIPT_BACKUP_CONFIG_611_DOWN = "harddiskb:/classic.cfg"
SCRIPT_BACKUP_CONFIG_612_UP = "harddiskb:/cXR_xr_plane.cfg"
SCRIPT_BACKUP_ADMIN_CONFIG_611_DOWN = "harddiskb:/admin.cfg"
SCRIPT_BACKUP_ADMIN_CONFIG_612_UP = "harddiskb:/cXR_admin_plane.cfg"

MIGRATION_TIME_OUT = 7200

PASSWORD_PROMPT = re.compile(r"[P|p]assword:\s?")
USERNAME_PROMPT = re.compile(r"([U|u]sername:|login:)\s?")

PERMISSION_DENIED = r"Permission denied"
AUTH_FAILED = r"Authentication failed|not authorized|Login incorrect"
RESET_BY_PEER = r"reset by peer|closed by foreign host"
SET_USERNAME = r"[Ee]nter.*username:"
SET_PASSWORD = r"Enter secret"
PASSWORD_OK = r"[Pp]assword [Oo][Kk]"
PRESS_RETURN = r"Press RETURN to get started\."

# Error when the hostname can't be resolved or there is
# network reachability timeout
UNABLE_TO_CONNECT = "nodename nor servname provided, or not known|" \
                    "Unknown host|" \
                    "[Operation|Connection] timed out|" \
                    "[D|d]estination unreachable|" \
                    "[U|u]nable to connect|" \
                    "[C|c]onnection refused"

# Telnet connection initiated
ESCAPE_CHAR = "Escape character is|Open"
# Connection refused i.e. line busy on TS
CONNECTION_REFUSED = re.compile("Connection refused")


class Plugin(CSMPlugin):
    """
    A plugin for migrating a ASR9K IOS-XR(XR) system to
    ASR9K IOS-XR 64 bit(eXR/fleXR).
    This plugin calls the migration script on device and reload
    device to boot eXR image.
    Console access is needed.
    """
    name = "Migrate Plugin"
    platforms = {'ASR9K'}
    phases = {'Migrate'}

    def _run_migration_script(self):
        """
        Run the migration script in /pkg/bin/migrate_to_eXR on device to set
        internal variables for booting eXR image.
        Check that no error occurred.
        :return: True if no error occurred.
        """

        output = self.ctx.send("run /pkg/bin/migrate_to_eXR -m eusb", timeout=1800)

        self._check_migration_script_output(output)

        return True

    def _check_migration_script_output(self, output):
        """Check that the migration script finished without errors, and also, the configs are backed up."""
        lines = output.splitlines()
        for line in lines:
            if "No such file" in line:
                self.ctx.error("Found file missing when running migration script. Please check session.log.")
            if "Error:" in line:
                self.ctx.error("Migration script reported error. Please check session.log.")

        if not self._is_config_backed_up(SCRIPT_BACKUP_CONFIG_612_UP, "IOS-XR"):
            if not self._is_config_backed_up(SCRIPT_BACKUP_CONFIG_611_DOWN, "IOS-XR"):
                self.ctx.error("Migration script failed to back up the IOS-XR running config. " +
                               "Please check session.log.")

        if not self._is_config_backed_up(SCRIPT_BACKUP_ADMIN_CONFIG_612_UP, "admin"):
            if not self._is_config_backed_up(SCRIPT_BACKUP_ADMIN_CONFIG_611_DOWN, "admin"):
                self.ctx.error("Migration script failed to back up the admin running config. " +
                               "Please check session.log.")

    def _is_config_backed_up(self, config_filename, config_type):
        output = self.ctx.send('dir {}'.format(config_filename))
        if "No such file" in output:
            return False
        log_and_post_status(self.ctx, "The {} configurations are backed up in {}".format(config_type,
                                                                                         config_filename))
        return True

    def _reload_all(self):
        """Reload all nodes to boot eXR image."""
        if self.ctx.is_console:
            if not self.ctx.reload(reload_timeout=MIGRATION_TIME_OUT):
                self.ctx.error("Encountered error when attempting to reload device.")
        else:
            def send_newline(fsm_ctx):
                fsm_ctx.ctrl.sendline()
                return True

            UNCOMMITTED_PACKAGES = re.compile(r"software packages are not yet committed. Proceed\?\[confirm\]")
            DONE = re.compile(re.escape(r"[Done]"))
            PROCEED = re.compile(re.escape(r"Proceed with reload? [confirm]"))

            events = [UNCOMMITTED_PACKAGES, DONE, PROCEED]
            transitions = [
                (UNCOMMITTED_PACKAGES, [0], 1, send_newline, 300),
                (DONE, [0, 1], 2, None, 300),
                (PROCEED, [0, 1, 2], -1, send_newline, 300)
            ]

            if not self.ctx.run_fsm("RELOAD", "admin reload location all", events, transitions, timeout=300):
                self.ctx.error("Failed to reload.")

            # wait a little bit before disconnect so that newline character can reach the router
            time.sleep(5)
            self.ctx.disconnect()
            self.ctx.post_status("Waiting for device boot to reconnect")
            self.ctx.info("Waiting for device boot to reconnect")
            time.sleep(300)
            self.ctx.reconnect(max_timeout=MIGRATION_TIME_OUT, force_discovery=True)  # 60 * 60 = 3600

        return check_exr_final_band(self.ctx)

    def run(self):

        host = None
        try:
            host = self.ctx.get_host
        except AttributeError:
            self.ctx.error("No host selected.")

        if host is None:
            self.ctx.error("No host selected.")

        log_and_post_status(self.ctx,
                            "Run migration script to extract the image and boot files and set boot mode in device")

        self._run_migration_script()

        log_and_post_status(self.ctx, "Reload device to boot ASR9K-X64 image.")
        self._reload_all()

        run_additional_custom_commands(self.ctx, {"show platform"})

        # Refresh package and inventory information
        get_package(self.ctx)
        get_inventory(self.ctx)

        update_device_info_udi(self.ctx)

        return True
