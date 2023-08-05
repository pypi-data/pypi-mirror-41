from .__version__ import version as __version__

import subprocess as sp
import datetime
import logging
import re
import semver
import os

log = logging.getLogger("gwsa")


def get_semver(root, rc='rc', full=False):
    log.debug("root %s", root)
    os.chdir(root)
    ver = sp.check_output('git describe --long --dirty', shell=True).strip()
    dirty = None
    if ver.endswith('-dirty'):
        ver = ver[:-6]
        dirty = datetime.datetime.now()
        dirty = 'd{time:%Y%m%d}'.format(time=dirty)
    log.debug("dirty %s", dirty)

    ver = ver.rsplit('-', 2)
    tagre = 'v?(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)'
    m = re.match(tagre, ver[0])
    if not m:
        log.error("%s is not SemVer tag, eg M.N.P", ver[0])
        exit(1)
    major, minor, patch = [int(x) for x in m.groups()]

    pr = None
    if ver[1] != '0':
        pr = rc + ver[1]

    build = ver[2]
    if dirty:
        build += '.' + dirty
    if dirty or pr:
        patch += 1
        full = True
    if not full:
        build = None
    sm = semver.VersionInfo(major, minor, patch, prerelease=pr, build=build)
    log.debug("sm %s", repr(sm))
    return sm


def next_tag(sm):
    tag = "%d.%d.%d" % (sm.major, sm.minor, sm.patch)
    if sm.prerelease:
        print tag
        log.info("You can set it with command 'git tag -a -m %s %s'", tag, tag)
    else:
        log.error("You are still on '%s' tag", tag)
        exit(1)
