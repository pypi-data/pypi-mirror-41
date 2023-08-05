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


def get_filesystems(ctx):
    """
    RP/0/RSP0/CPU0:R3#show filesystem
    Tue May 17 08:06:50.659 UTC
    File Systems:

         Size(b)     Free(b)        Type  Flags  Prefixes
               -           -     network     rw  qsm/dev/fs/tftp:
               -           -     network     rw  qsm/dev/fs/rcp:
               -           -     network     rw  qsm/dev/fs/ftp:
      2420113408  2417984512  dumper-lnk     rw  qsm/dumper_disk0a:
      2420113408  2419496448  dumper-lnk     rw  qsm/dumper_disk1a:
      6442434560  4083949568  dumper-lnk     rw  qsm/dumper_harddisk:
       771276800   771268608  dumper-lnk     rw  qsm/dumper_harddiskb:
       805306368   798971392  dumper-lnk     rw  qsm/dumper_harddiska:
     12101599232 10883157504  dumper-lnk     rw  qsm/dumper_disk1:
     12101599232  7567057920  dumper-lnk     rw  qsm/dumper_disk0:
     12101599232  7567057920  flash-disk     rw  disk0:
      6442434560  4083949568    harddisk     rw  harddisk:
       805306368   798971392    harddisk     rw  harddiska:
       771276800   771268608    harddisk     rw  harddiskb:
     12101599232 10883157504  flash-disk     rw  disk1:
      2420113408  2417984512  flash-disk     rw  disk0a:
      2420113408  2419496448  flash-disk     rw  disk1a:
          515072      485376       nvram     rw  nvram:
    """
    output = ctx.send("show filesystem")
    file_systems = {}
    start = False
    for line in output.split('\n'):
        if line.strip().endswith("Prefixes"):
            start = True
            continue
        if start:
            items = line.split()
            if len(items) == 5:
                size, free, fs_type, flags, fs_name, = line.split()
                file_systems[fs_name] = {
                    'size': 0 if size == '-' else long(size),
                    'free': 0 if size == '-' else long(free),
                    'fs_type': fs_type,
                    'flags': flags,
                }
            else:
                continue
    return file_systems
