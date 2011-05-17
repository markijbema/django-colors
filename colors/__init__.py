VERSION = (0, 0, 3, 'alpha', 0)

# Most of this code is taken form from the Django project

import os.path, re, colors

def get_version():
    return '0.0.4'
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    else:
        if VERSION[3] != 'final':
            version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    return version
