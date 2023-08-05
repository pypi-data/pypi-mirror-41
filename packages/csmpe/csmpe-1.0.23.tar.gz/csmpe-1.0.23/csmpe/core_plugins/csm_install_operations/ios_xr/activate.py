# =============================================================================
#
# Copyright (c) 2016, Cisco Systems
# All rights reserved.
#
# # Author: Klaudiusz Staniek
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
from install import install_activate_deactivate, parse_pkg_list, report_changed_pkg
from csmpe.core_plugins.csm_get_inventory.ios_xr.plugin import get_package, get_inventory
from csmpe.core_plugins.csm_install_operations.utils import update_device_info_udi, get_cmd_for_install_activate_deactivate


class Plugin(CSMPlugin):
    """This plugin Activates packages on the device."""
    name = "Install Activate Plugin"
    platforms = {'ASR9K', 'XR12K', 'CRS'}
    phases = {'Activate'}
    os = {'XR'}

    def get_tobe_activated_pkg_list(self):
        """
        Produces a list of packaged to be activated
        """
        packages = self.ctx.software_packages

        pkgs = SoftwarePackage.from_package_list(packages)
        installed_inact = SoftwarePackage.from_show_cmd(self.ctx.send("admin show install inactive summary"))
        installed_act = SoftwarePackage.from_show_cmd(self.ctx.send("admin show install active summary"))

        # Packages to activate but not already active
        pkgs = pkgs - installed_act
        if pkgs:
            packages_to_activate = set()
            # After the packages are considered equal according to SoftwarePackage.__eq__(),
            # Use the package name in the inactive area.  It is possible that the package
            # name given for Activation may be an external filename like below.
            # asr9k-px-5.3.3.CSCuy81837.pie to disk0:asr9k-px-5.3.3.CSCuy81837-1.0.0
            # asr9k-mcast-px.pie-5.3.3 to disk0:asr9k-mcast-px-5.3.3
            for inactive_pkg in installed_inact:
                for pkg in pkgs:
                    if pkg == inactive_pkg:
                        packages_to_activate.add(inactive_pkg)

            if not packages_to_activate:
                to_activate = " ".join(map(str, pkgs))

                state_of_packages = "\nTo activate :{} \nInactive: {} \nActive: {}".format(
                    to_activate, installed_inact, installed_act
                )
                self.ctx.info(state_of_packages)
                self.ctx.error('To be activated packages not in inactive packages list.')
                return None
            else:
                if len(packages_to_activate) != len(packages):
                    self.ctx.info('Packages selected for activation: {}\n'.format(" ".join(map(str, packages))) +
                                  'Packages that are to be activated: {}'.format(" ".join(map(str,
                                                                                          packages_to_activate))))
                return " ".join(map(str, packages_to_activate))

    def run(self):
        """
        Performs install activate operation
        """
        cmd = get_cmd_for_install_activate_deactivate(self.ctx, self.get_tobe_activated_pkg_list,
                                                      cmd_with_package_names='admin install activate {} prompt-level none async',
                                                      cmd_with_operation_id='admin install activate id {} prompt-level none async')

        if not cmd:
            self.ctx.info("Nothing to be activated.")
            return True

        output = self.ctx.send("show install active summary")
        before = parse_pkg_list(output)

        self.ctx.info("Activate package(s) pending")
        self.ctx.post_status("Activate Package(s) Pending")

        install_activate_deactivate(self.ctx, cmd)

        self.ctx.info("Activate package(s) done")

        output = self.ctx.send("show install active summary")
        after = parse_pkg_list(output)

        pkg_list = report_changed_pkg(before, after)
        pkg_change_list = ','.join(pkg_list)

        self.ctx.save_job_data("package_change_list", pkg_change_list)
        self.ctx.info("package change list:")

        for pkg in pkg_list:
            self.ctx.info("\t{}".format(pkg))

        self.ctx.info("Refreshing package and inventory information")
        self.ctx.post_status("Refreshing package and inventory information")
        # Refresh package and inventory information
        get_package(self.ctx)
        get_inventory(self.ctx)

        update_device_info_udi(self.ctx)
