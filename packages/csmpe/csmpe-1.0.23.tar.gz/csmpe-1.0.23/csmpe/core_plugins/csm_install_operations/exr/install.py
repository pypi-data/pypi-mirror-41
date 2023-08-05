# coding=utf-8
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
from functools import partial
import itertools
import re
import time
from condoor import ConnectionError, CommandError, CommandSyntaxError
from csmpe.core_plugins.csm_node_status_check.exr.plugin_lib import parse_show_platform
from csmpe.core_plugins.csm_install_operations.actions import a_error

# match for:
# Error! Not enough free disk space for installation.
# ERROR:Initrd md5sum does not match. The iso might be corrupted
# ERROR!! failed while handling validate reply
install_error_pattern = re.compile("E[Rr][Rr][Oo][Rr]:?!* *(.*)", re.MULTILINE)

plugin_ctx = None


def log_install_errors(ctx, output):
        errors = re.findall(install_error_pattern, output)
        for line in errors:
            ctx.warning(line)


def check_ncs6k_release(ctx):
    """
    Only release 5.2.5 and above are supported by the plugin.
    """
    if ctx.family == 'NCS6K':
        packages = ctx.software_packages
        if packages is not None:
            for package_name in packages:
                matches = re.findall(r"\d+\.\d+\.\d+", package_name)
                if matches:
                    if matches[0] < '5.2.5':
                        ctx.error('Abort: Software package earlier than release 5.2.5 for NCS6K is not supported.')


def check_ncs4k_release(ctx):
    """
    Only release 6.0.2 and above are supported by the plugin.
    """
    if ctx.family == 'NCS4K':
        packages = ctx.software_packages
        if packages is not None:
            for package_name in packages:
                matches = re.findall(r"\d+\.\d+\.\d+", package_name)
                if matches:
                    if matches[0] < '6.0.2':
                        ctx.error('Abort: Software package earlier than release 6.0.2 for NCS4K is not supported.')


def watch_operation(ctx, op_id=0):
    """
    Watch for the non-reload situation.  Upon issuing add/activate/commit/remove/deactivate, the install operation
    will be executed in the background.  The following message

    Install operation will continue in the background

    will be displayed.  After some time elapses, a successful or abort message will be displayed.

    The CLI command, 'show install request' is used in the loop to report the progress percentages.  Upon
    completion, 'show install request' returns 'No install operation in progress'.  The watch_operation will be
    done at that point.

    As an example,

    RP/0/RP0/CPU0:Deploy#install deactivate ncs6k-5.2.5.CSCuz65240-1.0.0
    May 31 20:14:14 Install operation 3 started by root:
      install deactivate pkg ncs6k-5.2.5.CSCuz65240-1.0.0
    May 31 20:14:14 Package list:
    May 31 20:14:14     ncs6k-5.2.5.CSCuz65240-1.0.0
    May 31 20:14:20 Install operation will continue in the background

    <--- Time Lapse --->

    RP/0/RP0/CPU0:Deploy#May 31 20:15:10 Install operation 3 finished successfully

    ------------------------------------------------------------------------------------------------------------
    RP/0/RP0/CPU0:Deploy#show install request
    The install operation 17 is 30% complete

    or

    RP/0/RP0/CPU0:Deploy#show install request
    No install operation in progress

    When install is completed, the following message will be displayed

    ------------------------------------------------------------------------------------------------------------
    If the install operation is successful, the following message will be displayed.

    RP/0/RP0/CPU0:Deploy#May 24 22:25:43 Install operation 17 finished successfully
    """
    no_install = r"No install operation in progress"
    # In ASR9K eXR, the output to show install request may be "The install prepare operation 9 is 40% complete"
    # or "The install service operation 9 is 40% complete" or "The install add operation 9 is 40% complete" and etc.
    op_progress = r"The install \w*?\s?operation {} is (\d+)% complete".format(op_id)
    success = "Install operation {} finished successfully".format(op_id)

    cmd_show_install_request = "show install request"
    ctx.info("Watching the operation {} to complete".format(op_id))

    propeller = itertools.cycle(["|", "/", "-", "\\", "|", "/", "-", "\\"])

    last_status = None
    finish = False
    time_tried = 0
    op_id = str(op_id)
    while not finish:
        try:
            try:
                # this is to catch the successful operation as soon as possible
                ctx.send("", wait_for_string=success, timeout=20)
                finish = True
            except ctx.CommandTimeoutError:
                pass

            message = ""
            try:
                output = ctx.send(cmd_show_install_request, timeout=300)
            except (CommandError, CommandSyntaxError) as e:
                ctx.info("{} received an error".format(cmd_show_install_request))
                time.sleep(10)
                output = ctx.send(cmd_show_install_request, timeout=300)
            if op_id in output:
                result = re.search(op_progress, output)
                if result:
                    status = result.group(0)
                    message = "{} {}".format(propeller.next(), status)

                if message != last_status:
                    ctx.post_status(message)
                    last_status = message
        except (ConnectionError, ctx.CommandTimeoutError) as e:
            if time_tried > 2:
                raise e

            time_tried += 1
            ctx.disconnect()
            time.sleep(60)
            ctx.reconnect(force_discovery=True)

        # ctx.send returns with an empty output from 'show install request'. go back to loop
        if output is None:
            continue

        # ctx.send returns and no active install action in progress. terminate the loop
        if no_install in output:
            break

    report_install_status(ctx, op_id)


def validate_node_state(inventory):
    valid_state = [
        'IOS XR RUN',
        'PRESENT',
        'READY',
        'FAILED',
        'OK',
        'DISABLED',
        'UNPOWERED',
        'POWERED_OFF',
        'SW_INACTIVE',
        'ADMIN DOWN',
        'OPERATIONAL',
        'NOT ALLOW ONLIN',  # This is not spelling error
    ]

    for key, value in inventory.items():
        if 'CPU' in key:
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
    if not ctx.is_console:
        ctx.disconnect()
        ctx.post_status("Waiting for device boot to reconnect")
        ctx.info("Waiting for device boot to reconnect")
        # it may take up to 10 minutes before Fretta actually reboots
        time.sleep(600)
        ctx.reconnect(max_timeout=3600, force_discovery=True)  # 60 * 60 = 3600

    else:
        ctx.info("Keeping console connected")
        ctx.post_status("Boot process started")
        ctx.info("Boot process started")
        if not ctx.reload(reload_timeout=1500, no_reload_cmd=True):
            ctx.error("Encountered error when attempting to reload device.")
        ctx.info("Boot process finished")

    ctx.info("Device connected successfully")

    timeout = 7200
    poll_time = 30
    time_waited = 0
    xr_run = "IOS XR RUN"

    cmd = "show platform"
    ctx.info("Waiting for all nodes to come up")
    ctx.post_status("Waiting for all nodes to come up")

    time.sleep(100)

    while 1:
        # Wait till all nodes are in XR run state
        time_waited += poll_time
        if time_waited >= timeout:
            break

        time.sleep(poll_time)

        # show platform can take more than 1 minute after router reload. Issue No. 47
        output = ctx.send(cmd, timeout=600)
        if xr_run in output:
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


def observe_install_add_remove(ctx, output, has_tar=False):
    """
    Success Condition:
    ADD:
    install add source tftp://223.255.254.254/auto/tftpboot-users/alextang/ ncs6k-mpls.pkg-6.1.0.07I.DT_IMAGE
    May 24 18:54:12 Install operation will continue in the background
    RP/0/RP0/CPU0:Deploy#May 24 18:54:30 Install operation 12 finished successfully

    REMOVE:
    RP/0/RP0/CPU0:Deploy#install remove ncs6k-5.2.5.47I.CSCux97367-0.0.15.i
    May 23 21:20:28 Install operation 2 started by root:
      install remove ncs6k-5.2.5.47I.CSCux97367-0.0.15.i
    May 23 21:20:28 Package list:
    May 23 21:20:28     ncs6k-5.2.5.47I.CSCux97367-0.0.15.i
    May 23 21:20:29 Install operation will continue in the background

    RP/0/RP0/CPU0:Deploy#May 23 21:20:29 Install operation 2 finished successfully

    Failed Condition:
    RP/0/RSP0/CPU0:CORFU#install remove ncs6k-5.2.5.47I.CSCux97367-0.0.15.i
    Mon May 23 22:57:45.078 UTC
    May 23 22:57:46 Install operation 28 started by iox:
      install remove ncs6k-5.2.5.47I.CSCux97367-0.0.15.i
    May 23 22:57:46 Package list:
    May 23 22:57:46     ncs6k-5.2.5.47I.CSCux97367-0.0.15.i
    May 23 22:57:47 Install operation will continue in the background

    RP/0/RSP0/CPU0:CORFU#May 23 22:57:48 Install operation 28 aborted
    """
    result = re.search(r'Install operation (\d+)', output)
    if result:
        op_id = result.group(1)
    else:
        log_install_errors(ctx, output)
        ctx.error("Operation failed")
        return  # for sake of clarity

    op_success = "Install operation will continue in the background"

    if op_success in output:
        watch_operation(ctx, op_id)
        if has_tar is True:
            ctx.set_operation_id(ctx.software_packages, op_id)
            ctx.info("The operation {} stored".format(op_id))
    else:
        log_install_errors(ctx, output)
        ctx.error("Operation {} failed".format(op_id))


def get_op_id(output):
    """
    :param output: Output from the install command
    :return: the operational ID
    """
    result = re.search(r'Install operation (\d+)', output)
    if result:
        return result.group(1)
    return -1


def report_install_status(ctx, op_id):
    """
    :param ctx: CSM Context object
    :param op_id: operational ID
    Peeks into the install log to see if the install operation is successful or not
    """
    failed_oper = r'Install operation {} aborted'.format(op_id)
    output = ctx.send("show install log {} detail".format(op_id))
    if re.search(failed_oper, output):
        log_install_errors(ctx, output)
        ctx.error("Operation {} failed".format(op_id))

    report_changed_pkg(ctx, output)

    ctx.info("Operation {} finished successfully".format(op_id))


def handle_aborted(fsm_ctx):
    """
    :param ctx: FSM Context
    :return: True if successful other False
    """
    global plugin_ctx

    report_install_status(ctx=plugin_ctx, op_id=get_op_id(fsm_ctx.ctrl.before))

    # Indicates the failure
    return False


def handle_non_reload_activate_deactivate(fsm_ctx):
    """
    :param ctx: FSM Context
    :return: True if successful other False
    """
    global plugin_ctx

    op_id = get_op_id(fsm_ctx.ctrl.before)
    if op_id == -1:
        return False

    watch_operation(plugin_ctx, op_id)

    return True


def handle_reload_activate_deactivate(fsm_ctx):
    """
    :param ctx: FSM Context
    :return: True if successful other False
    """
    global plugin_ctx

    op_id = get_op_id(fsm_ctx.ctrl.before)
    if op_id == -1:
        return False

    try:
        watch_operation(plugin_ctx, op_id)
    except plugin_ctx.CommandTimeoutError:
        # The device already started the reload
        pass

    success = wait_for_reload(plugin_ctx)
    if not success:
        plugin_ctx.error("Reload or boot failure")
        return

    plugin_ctx.info("Operation {} finished successfully".format(op_id))

    return True


def no_impact_warning(fsm_ctx):
    plugin_ctx.warning("This was a NO IMPACT OPERATION. Packages are already active on device.")
    return True


def handle_not_start(fsm_ctx):
    """
    :param ctx: FSM Context
    :return: False
    """
    global plugin_ctx

    plugin_ctx.error("Could not start this install operation because an install operation is still in progress")
    return False


def install_activate_deactivate(ctx, cmd):
    """
    Abort Situation:
    RP/0/RP0/CPU0:Deploy#install activate ncs6k-5.2.5.CSCuz65240-1.0.0

    Jun 02 20:19:31 Install operation 8 started by root:
      install activate pkg ncs6k-5.2.5.CSCuz65240-1.0.0
    Jun 02 20:19:31 Package list:
    Jun 02 20:19:31     ncs6k-5.2.5.CSCuz65240-1.0.0
    Jun 02 20:19:31     ncs6k-5.2.5.47I.CSCuy47880-0.0.4.i
    Jun 02 20:19:31     ncs6k-5.2.5.CSCux82987-1.0.0
    Jun 02 20:19:38 Install operation 8 aborted

    ------------------------------------------------------------------------------------------------------------
    Non-Reload Situation:

    RP/0/RP0/CPU0:Deploy#install deactivate ncs6k-5.2.5.CSCuz65240-1.0.0
    May 31 20:14:14 Install operation 3 started by root:
      install deactivate pkg ncs6k-5.2.5.CSCuz65240-1.0.0
    May 31 20:14:14 Package list:
    May 31 20:14:14     ncs6k-5.2.5.CSCuz65240-1.0.0
    May 31 20:14:20 Install operation will continue in the background (may or may not be displayed)

    <--- Time Lapses --->

    RP/0/RP0/CPU0:Deploy#May 31 20:15:10 Install operation 3 finished successfully

    ------------------------------------------------------------------------------------------------------------
    Reload Situation 1:

    RP/0/RP0/CPU0:Deploy#install activate ncs6k-5.2.5.CSCux82987-1.0.0
    May 31 20:17:08 Install operation 4 started by root:
      install activate pkg ncs6k-5.2.5.CSCux82987-1.0.0
    May 31 20:17:08 Package list:
    May 31 20:17:08     ncs6k-5.2.5.CSCux82987-1.0.0

    <--- Time Lapses --->

    This install operation will reboot the sdr, continue?
     [yes/no]:[yes] <Hit Enter>
    May 31 20:17:47 Install operation will continue in the background

    <--- Time Lapses --->

    RP/0/RP0/CPU0:Deploy#May 31 20:18:44 Install operation 4 finished successfully

    <--- Router Starts Reloading --->

    Connection closed by foreign host.

    Reload Situation 2:

    RP/0/RSP0/CPU0:ios#install activate id 25
    Jun 09 15:49:15 Install operation 27 started by root:
    install activate id 25
    Jun 09 15:49:15 Package list:
    Jun 09 15:49:15     asr9k-sysadmin-system-6.1.1.17-r61116I.CSCcv44444.x86_64
    Jun 09 15:49:15     asr9k-os-supp-64-3.1.0.1-r61116I.CSCxr90021.x86_64
    Jun 09 15:49:15     asr9k-base-64-4.0.0.2-r61116I.CSCxr90014.x86_64
    Jun 09 15:49:15     asr9k-sysadmin-topo-6.1.1.17-r61116I.CSCcv55555.x86_64

    This install operation will reload the sdr, continue?
    [yes/no]:[yes] <Hit Enter>
    Jun 09 15:49:26 Install operation will continue in the background
    RP/0/RSP0/CPU0:ios#

    <--- Time Lapses --->

    RP/0/RSP0/CPU0:ios#Jun 09 15:53:51 Install operation 27 finished successfully

    """
    global plugin_ctx
    plugin_ctx = ctx

    ABORTED = re.compile("aborted")

    # REBOOT_PROMP for eXR reload response:
    # This install operation will reload the sdr, continue?
    #  [yes/no]:[yes]
    # REBOOT_PROMP for NCS5K reload response:
    # This install operation will reload the system, continue?
    #  [yes/no]:[yes]

    # Seeing this message without the reboot prompt indicates a non-reload situation
    CONTINUE_IN_BACKGROUND = re.compile("Install operation will continue in the background")
    REBOOT_PROMPT = re.compile("This install operation will (?:reboot|reload) the sdr, continue")
    RELOAD_PROMPT = re.compile("This install operation will reload the system, continue")
    RUN_PROMPT = re.compile("#")
    NO_IMPACT = re.compile("NO IMPACT OPERATION")
    ERROR = re.compile(re.escape("ERROR! there was an SU/ISSU done. please perform install commit before "
                                 "proceeding with any other prepare/activate/deactivate operation"))
    NOT_START = re.compile("Could not start this install operation")

    #                  0                    1              2           3          4         5          6
    events = [CONTINUE_IN_BACKGROUND, REBOOT_PROMPT, RELOAD_PROMPT, ABORTED, NO_IMPACT, RUN_PROMPT, ERROR, NOT_START]
    transitions = [
        (CONTINUE_IN_BACKGROUND, [0], -1, handle_non_reload_activate_deactivate, 300),
        (REBOOT_PROMPT, [0], -1, handle_reload_activate_deactivate, 300),
        (RELOAD_PROMPT, [0], -1, handle_reload_activate_deactivate, 300),
        (NO_IMPACT, [0], -1, no_impact_warning, 60),
        (RUN_PROMPT, [0], -1, handle_non_reload_activate_deactivate, 300),
        (ABORTED, [0], -1, handle_aborted, 300),
        (ERROR, [0], -1, partial(a_error, ctx), 0),
        (NOT_START, [0], -1, handle_not_start, 300),
    ]

    if not ctx.run_fsm("ACTIVATE-OR-DEACTIVATE", cmd, events, transitions, timeout=300):
        ctx.error("Failed: {}".format(cmd))


def send_admin_cmd(ctx, cmd):
    ctx.send("admin")
    output = ctx.send(cmd)
    ctx.send("exit")

    return output


def observe_install_remove_all(ctx, cmd, prompt):
    """
    Success Condition:
    RP/0/RSP0/CPU0:vkg3#install remove inactive all
    Mar 01 16:17:13 Install operation 15 started by root:
      install remove inactive all
    Mar 01 16:17:14 Install operation will continue in the background
    RP/0/RSP0/CPU0:vkg3#Mar 01 16:17:18 Install operation 15 finished successfully

    Failed Conditions:
    RP/0/RSP0/CPU0:vkg3#install remove inactive all
    Mar 01 21:31:22 Install operation 17 started by root:
      install remove inactive all
    Mar 01 21:31:24 Install operation will continue in the background
    RP/0/RSP0/CPU0:vkg3#Mar 01 21:31:25 Install operation 17 aborted

    RP/0/RSP0/CPU0:vkg3#install remove inactive all
    Could not start this install operation. Install operation 18 is still in progress
    """
    # no op_id is returned from XR for install remove inactive
    # need to figure out the last op_id first

    cmd_show_install_log_reverse = 'show install log reverse | utility egrep "Install operation [0-9]+ started"'
    output = ctx.send(cmd_show_install_log_reverse, timeout=300)

    if 'No install operation' in output:
        op_id = 0
    else:
        result = re.search(r'Install operation (\d+) started', output)
        if result:
            op_id = int(result.group(1))
        else:
            log_install_errors(ctx, output)
            ctx.error("Operation ID not found by show install log reverse")
            return

    # Expected Operation ID
    op_id += 1

    oper_err = "Install operation {} aborted".format(op_id)
    oper_success = "Install operation {} finished successfully".format(op_id)
    Error1 = re.compile("Could not start this install operation. Install operation")
    Error2 = re.compile(oper_err)
    Proceed_removing = re.compile(oper_success)
    Host_prompt = re.compile(prompt)

    events = [Host_prompt, Error1, Error2, Proceed_removing]
    transitions = [
        (Error1, [0], -1, CommandError("Another install command is currently in operation",
                                       ctx._connection.hostname), 1800),
        (Error2, [0], -1, CommandError("No packages can be removed", ctx._connection.hostname), 1800),
        (Proceed_removing, [0], -1, None, 1800),
        (Host_prompt, [0], -1, None, 1800),
    ]

    if not ctx.run_fsm("Remove Inactive All", cmd, events, transitions, timeout=1800):
        ctx.error("Failed: {}".format(cmd))

    message = "Waiting the operation to continue asynchronously"
    ctx.info(message)
    ctx.post_status(message)

    last_status = None
    no_install = r"No install operation in progress"
    op_progress = r"The install operation {} is (\d+)% complete".format(op_id)
    cmd_show_install_request = "show install request"
    propeller = itertools.cycle(["|", "/", "-", "\\", "|", "/", "-", "\\"])

    finish = False
    time_tried = 0
    op_id = str(op_id)
    while not finish:
        try:
            try:
                # this is to catch the successful operation as soon as possible
                ctx.send("", wait_for_string=oper_success, timeout=20)
                finish = True
            except ctx.CommandTimeoutError:
                pass

            message = ""
            try:
                output = ctx.send(cmd_show_install_request, timeout=300)
            except (CommandError, CommandSyntaxError) as e:
                ctx.info("{} received an error".format(cmd_show_install_request))
                time.sleep(10)
                output = ctx.send(cmd_show_install_request, timeout=300)
            if op_id in output:
                result = re.search(op_progress, output)
                if result:
                    status = result.group(0)
                    message = "{} {}".format(propeller.next(), status)

                if message != last_status:
                    ctx.post_status(message)
                    last_status = message
        except (ConnectionError, ctx.CommandTimeoutError) as e:
            if time_tried > 120:
                raise e

            time_tried += 1
            time.sleep(30)

        if no_install in output:
            break

    cmd_show_install_log = "show install log {} detail".format(op_id)
    output = ctx.send(cmd_show_install_log, timeout=600)
    ctx.info(output)

    if oper_success in output:
        report_changed_pkg(ctx, output)
        message = "Remove All Inactive Package(s) Successfully"
        ctx.info(message)
        ctx.post_status(message)
    else:
        ctx.error("Remove All Inactive Package(s) failed")


def report_changed_pkg(ctx, output):
    """
    :param ctx: CSM Context object
    :param output: show install log op_id detail
    """

    pkg_list = []
    flag = False

    lines = output.split('\n')
    lines = [x for x in lines if x]

    for line in lines:
        if 'Packages added:' in line or 'Package list:' in line:
            flag = True
            continue

        if flag:
            if line[16].isalnum():
                break
            else:
                pkg = line[20:].strip()
                pkg = pkg.replace('.x86_64', '')
                pkg_list.append(pkg)

    if flag:
        pkg_change_list = ','.join(pkg_list)
        ctx.save_job_data("package_change_list", pkg_change_list)
        ctx.info("package change list:")
        for pkg in pkg_list:
            ctx.info("\t{}".format(pkg))
