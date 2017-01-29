import sys
import dyn


def check_python_version():
    version = sys.version_info

    if version.major < 3 or (version.major == 3 and version.minor < 5):
        sys.exit("You need at least Python 3.5")

check_python_version()


import testing.tests

environment = dyn.create()
