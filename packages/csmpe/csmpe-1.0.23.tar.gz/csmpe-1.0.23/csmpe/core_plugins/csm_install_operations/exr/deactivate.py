# =============================================================================
#
# Copyright (c) 2016, Cisco Systems
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

from package_lib import SoftwarePackage
from csmpe.plugins import CSMPlugin
from install import install_activate_deactivate
from install import send_admin_cmd
from csmpe.core_plugins.csm_get_inventory.exr.plugin import get_package, get_inventory
from csmpe.core_plugins.csm_install_operations.utils import get_cmd_for_install_activate_deactivate


class Plugin(CSMPlugin):
    """This plugin deactivates packages on the device."""
    name = "Install Deactivate Plugin"
    platforms = {'ASR9K', 'NCS1K', 'NCS1001', 'NCS4K', 'NCS5K', 'NCS540',
                 'NCS5500', 'NCS6K', 'IOSXRv-9K', 'IOSXRv-X64'}
    phases = {'Deactivate'}
    os = {'eXR'}

    def get_tobe_deactivated_pkg_list(self):
        """
        Produces a list of packaged to be deactivated
        """
        packages = self.ctx.software_packages
        pkgs = SoftwarePackage.from_package_list(packages)

        admin_installed_act = SoftwarePackage.from_show_cmd(send_admin_cmd(self.ctx, "show install active"))
        installed_act = SoftwarePackage.from_show_cmd(self.ctx.send("show install active"))

        installed_act.update(admin_installed_act)

        if pkgs:
            # packages to be deactivated and installed active packages
            packages_to_deactivate = pkgs & installed_act
            if not packages_to_deactivate:
                to_deactivate = " ".join(map(str, pkgs))

                state_of_packages = "\nTo deactivate :{} \nActive: {}".format(
                    to_deactivate, installed_act
                )

                self.ctx.info(state_of_packages)
                self.ctx.error('To be deactivated packages not in active packages list.')
                return None
            else:
                if len(packages_to_deactivate) != len(packages):
                    self.ctx.info('Packages selected for deactivation: {}\n'.format(" ".join(map(str, packages))) +
                                  'Packages that are to be deactivated: {}'.format(" ".join(map(str,
                                                                                            packages_to_deactivate))))
                return " ".join(map(str, packages_to_deactivate))

    def run(self):
        """
        Performs install deactivate operation
        RP/0/RP0/CPU0:Deploy#install deactivate ncs6k-5.2.5.CSCuz65240-1.0.0
        May 27 16:39:31 Install operation 33 started by root:
          install deactivate pkg ncs6k-5.2.5.CSCuz65240-1.0.0
        May 27 16:39:31 Package list:
        May 27 16:39:31     ncs6k-5.2.5.CSCuz65240-1.0.0
        May 27 16:39:36 Install operation will continue in the background
        """
        cmd = get_cmd_for_install_activate_deactivate(self.ctx, self.get_tobe_deactivated_pkg_list,
                                                      cmd_with_package_names='install deactivate {}',
                                                      cmd_with_operation_id='install deactivate id {}')

        if not cmd:
            self.ctx.info("Nothing to be deactivated.")
            return True

        self.ctx.info("Deactivate package(s) pending")
        self.ctx.post_status("Deactivate Package(s) Pending")

        install_activate_deactivate(self.ctx, cmd)

        self.ctx.info("Deactivate package(s) done")

        # Refresh package and inventory information
        get_package(self.ctx)
        get_inventory(self.ctx)
