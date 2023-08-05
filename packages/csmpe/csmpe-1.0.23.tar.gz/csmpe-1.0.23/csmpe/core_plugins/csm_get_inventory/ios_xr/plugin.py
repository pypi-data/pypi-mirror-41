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

from csmpe.plugins import CSMPlugin


class Plugin(CSMPlugin):
    """This plugin retrieves software information from the device."""
    name = "Get Inventory Plugin"
    platforms = {'ASR9K', 'XR12K', 'CRS'}
    phases = {'Get-Inventory'}
    os = {'XR'}

    def run(self):
        get_package(self.ctx)
        get_inventory(self.ctx)
        get_satellite(self.ctx)


def get_inventory(ctx):
    # saved the output of "admin show inventory"
    output = ctx.send("admin show inventory")
    ctx.save_job_data("cli_show_inventory", output)


def get_package(ctx):
    ctx.save_job_data("cli_show_install_inactive",
                      ctx.send("admin show install inactive summary"))
    ctx.save_job_data("cli_show_install_active",
                      ctx.send("admin show install active summary"))
    ctx.save_job_data("cli_show_install_committed",
                      ctx.send("admin show install committed summary"))


def get_satellite(ctx):
    ctx.save_job_data("cli_show_nv_satellite",
                      ctx.send("show nv satellite status"))
