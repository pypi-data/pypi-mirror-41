#!/usr/bin/python2
"""Print SemVer version for a git project. Git tags must match `v?M.N.P` pattern.
"""

############################################################
# {{{ configure logging
import logging
import sys
import json

try:
    import customlogging
except:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

log = logging.getLogger("gwsa")
if "--debug" in sys.argv:
    log.setLevel(logging.DEBUG)


def prettify(obj):
    class AllEncoder(json.JSONEncoder):
        def default(self, obj):
            try:
                return json.JSONEncoder.default(self, obj)
            except Exception as e:
                return str(obj)

    return json.dumps(obj, indent=4, sort_keys=True, cls=AllEncoder)


# }}}

############################################################
# {{{ main: argparse and dispatch

import json
import argparse
import os
import semver_tool


def AppArgParser():
    p = argparse.ArgumentParser(
        prog=__package__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    p.add_argument("--debug", help="debug mode", action="store_true")
    p.add_argument(
        "--version", action="version", version=semver_tool.__version__)
    p.add_argument(
        "--rc",
        help='release candidate prefix; default "%(default)s"',
        metavar='str',
        default='rc')
    p.add_argument(
        "--short",
        help='print first N components of M.N.P version',
        metavar='N',
        choices=[1, 2, 3],
        type=int)
    p.add_argument(
        "--full", help="full version with hash", action="store_true")
    p.add_argument(
        "-n", "--next-tag", help="print next tag", action="store_true")
    p.add_argument(
        "dir",
        help='git repo dir; default "%(default)s"',
        default='.',
        nargs='?')
    return p


def main():
    p = AppArgParser()

    Args, UnknownArgs = p.parse_known_args()
    log.debug("Args: %s", prettify(vars(Args)))
    log.debug("UnknownArgs: %s", UnknownArgs)

    sm = semver_tool.get_semver(root=Args.dir, rc=Args.rc, full=Args.full)
    if Args.next_tag:
        semver_tool.next_tag(sm)
    elif not Args.short:
        print sm
    else:
        ver = [sm.major, sm.minor, sm.patch]
        ver = [str(i) for i in ver]
        ver = ver[:Args.short]
        print '.'.join(ver)


# }}}

if __name__ == "__main__":
    main()
