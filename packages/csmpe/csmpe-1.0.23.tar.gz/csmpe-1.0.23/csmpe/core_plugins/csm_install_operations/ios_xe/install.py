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
import re
import time

from csmpe.core_plugins.csm_node_status_check.ios_xe.plugin_lib import parse_show_platform
from utils import install_add_remove

plugin_ctx = None


def send_newline(fsm_ctx):
    fsm_ctx.ctrl.sendline('\r\n')
    fsm_ctx.ctrl.sendline('\r\n')
    fsm_ctx.ctrl.sendline('\r\n')
    return True


def issu_error_state(fsm_ctx):
    plugin_ctx.warning("Error in ISSU. Please see session.log for details")
    return False


def issu_connection_closed(fsm_ctx):
    plugin_ctx.info("Connection closed by foreign host during ISSU")
    # sleep until both standby and active RSP's are upgraded
    time.sleep(3600)
    return True


def validate_node_state(inventory):
    valid_state = [
        'ok',
        'ok, active',
        'ok, standby',
        'ps, fail',
        'out of service',
        'N/A'
    ]
    for key, value in inventory.items():
        if value['state'] not in valid_state:
            break
    else:
        return True
    return False


def wait_for_reload(ctx):
    """
     Wait for system to come up with max timeout as 25 Minutes

    """
    begin = time.time()
    ctx.disconnect()
    ctx.post_status("Waiting for device boot to reconnect")
    ctx.info("Waiting for device boot to reconnect")
    time.sleep(1500)   # 25 * 60 = 1500
    ctx.reconnect(force_discovery=True)
    ctx.info("Boot process finished")
    ctx.info("Device connected successfully")

    timeout = 3600
    poll_time = 30
    time_waited = 0

    ctx.info("Waiting for all nodes to come up")
    ctx.post_status("Waiting for all nodes to come up")
    time.sleep(30)

    output = None

    ncnt = 0
    while 1:

        ncnt += 1
        if ncnt > 20:
            break

        # Wait till all nodes are in XR run state
        time_waited += poll_time
        if time_waited >= timeout:
            break

        time.sleep(poll_time)

        # show platform can take more than 1 minute after router reload. Issue No. 47
        output = ctx.send('show platform', timeout=600)

        ctx.info("show platform = {}".format(output))

        inventory = parse_show_platform(ctx, output)
        if validate_node_state(inventory):
            ctx.info("All nodes in desired state")
            elapsed = time.time() - begin
            ctx.info("Overall outage time: {} minute(s) {:.0f} second(s)".format(elapsed // 60, elapsed % 60))
            return True

    # Some nodes did not come to run state
    ctx.error("Not all nodes have came up: {}".format(output))
    # this will never be executed
    return False


def install_activate_write_memory(ctx, cmd):
    """

    PAN-5201-ASR903#write memory
    Building configuration...
    [OK]
    PAN-5201-ASR903#

    PAN-5201-ASR903#write memory
    Warning: Attempting to overwrite an NVRAM configuration previously written
    by a different version of the system image.
    Overwrite the previous NVRAM configuration?[confirm]

    """
    global plugin_ctx
    plugin_ctx = ctx

    # Seeing this message without the reboot prompt indicates a non-reload situation
    Build_config = re.compile(r'\[OK\]')
    Overwrite_warning = re.compile(r"Overwrite the previous NVRAM configuration\?\[confirm\]")

    events = [Overwrite_warning, Build_config]
    transitions = [
        (Overwrite_warning, [0], 1, send_newline, 1200),
        (Build_config, [0, 1], -1, None, 1200),
    ]

    if not ctx.run_fsm("write memory", cmd, events, transitions, timeout=1200):
        ctx.error("Failed: {}".format(cmd))


def expand_subpkgs_exec(ctx, folder, pkg):
    """
    Expand the consolidated file into the image folder

    :param: ctx
    :param: folder
    :param: pkg ie bootflash:asr900*.bin or harddisk:asr1000*.bin
    :return: True or False
    """
    pkg_conf = folder + '/packages.conf'
    pkg_conf2 = pkg_conf + '-'

    output = ctx.send('dir ' + pkg_conf)
    if 'No such file or directory' not in output:
        ctx.send('del /force ' + pkg_conf2)
        cmd = 'copy ' + pkg_conf + ' ' + pkg_conf2
        install_add_remove(ctx, cmd)
        ctx.send('del /force ' + pkg_conf)

    ctx.info("Expanding subpackages into {}".format(folder))

    cmd = 'request platform software package expand file ' + pkg + ' to ' + folder
    output = ctx.send(cmd, timeout=600)
    m = re.search('SUCCESS: Finished expanding all-in-one software package', output)
    if not m:
        ctx.warning("Error: {}".format(cmd))
        return False

    return True


def expand_subpkgs(ctx, rsp_count, disk, folder, pkg):
    """
    Expand the consolidated file into the image folder

    :param: ctx
    :param: rsp_count
    :param: pkg
    :return: True or False
    """

    package = disk + pkg
    result = expand_subpkgs_exec(ctx, folder, package)
    if not result:
        ctx.error('Expanding {} into {} has encountered '
                  'an error'.format(package, folder))
        return False

    if rsp_count == 2:
        cmd = 'copy ' + disk + pkg + ' ' + 'stby-' + disk + pkg
        install_add_remove(ctx, cmd)

        package = 'stby-' + package
        folder = 'stby-' + folder
        result = expand_subpkgs_exec(ctx, folder, package)
        if not result:
            ctx.error('Expanding {} into {} has encountered '
                      'an error'.format(package, folder))
            return False

    return True


def install_activate_reload(ctx):
    """
    Reload the router

    :param ctx
    :return: nothing
    """
    message = "Waiting the {} operation to continue".format('reload')
    ctx.info(message)
    ctx.post_status(message)

    if not ctx.reload(reload_timeout=1200, no_reload_cmd=True):
        ctx.error("Encountered error when attempting to reload device.")

    success = wait_for_reload(ctx)

    if not success:
        ctx.error("Reload or boot failure")
        return

    ctx.info("Operation reload finished successfully")
    return


def install_activate_issu(ctx, cmd):
    """
    Start the issu

    :param ctx
    :param cmd
    :param hostname
    :return: nothing
    """

    global plugin_ctx
    plugin_ctx = ctx

    # Seeing a message without STAGE 4 is an error
    Phase_one = re.compile("Starting disk space verification")
    Stage_one = re.compile("STAGE 1: Installing software on standby RP")
    Stage_two = re.compile("STAGE 2: Restarting standby RP")
    Stage_three = re.compile("STAGE 3: Installing sipspa package on local RP")
    Stage_four = re.compile("STAGE 4: Installing software on active RP")
    Load_on_reboot = re.compile("SUCCESS: Software provisioned.  New software will load on reboot")
    Missing_conf = re.compile("SYSTEM IS NOT BOOTED VIA PACKAGE FILE")
    Failed = re.compile("FAILED:")
    Connection_closed = re.compile("Connection closed by foreign host")
    #            0          1          2          3             4            5
    events = [Phase_one, Stage_one, Stage_two, Stage_three, Stage_four, Load_on_reboot,
              Missing_conf, Failed, Connection_closed]
    #            6            7            8
    transitions = [
        (Phase_one, [0], 1, None, 1800),
        (Stage_one, [0, 1], 2, None, 1800),
        (Stage_two, [2], 3, None, 1800),
        (Stage_three, [3], 4, None, 1800),
        (Stage_four, [4], 5, None, 1800),
        (Load_on_reboot, [5], -1, None, 1800),
        (Missing_conf, [0, 1, 2, 3, 4, 5], -1, issu_error_state, 60),
        (Failed, [0, 1, 2, 3, 4, 5], -1, issu_error_state, 60),
        (Connection_closed, [1, 2, 3, 4], -1, issu_connection_closed, 4200)
    ]

    if not ctx.run_fsm("ISSU", cmd, events, transitions, timeout=4200):
        ctx.error("Failed: {}".format(cmd))

    time.sleep(300)

    success = wait_for_reload(ctx)

    if not success:
        ctx.error("Reload or boot failure")
        return

    ctx.info("Operation reload finished successfully")
    return
