import sys
# Other imports AFTER version check!

def check_python_version():
    version = sys.version_info

    if version.major < 3 or (version.major == 3 and version.minor < 5):
        sys.exit("You need at least Python 3.5. You have version {}.{}...".format(version.major, version.minor))

check_python_version()


import dyn
import testing.tests

environment = dyn.create()
