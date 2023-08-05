from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import importlib
import os
import sys

import compas_rhino

from compas._os import create_symlink


__all__ = ['install']


INSTALLABLE_PACKAGES = ('compas', 'compas_ghpython', 'compas_rhino')


def _get_package_path(package):
    return os.path.abspath(os.path.join(os.path.dirname(package.__file__), '..'))


def install(version='6.0', packages=None):
    """Install COMPAS for Rhino.

    Parameters
    ----------
    version : {'5.0', '6.0'}
        The version number of Rhino.
    packages : list of str
        List of packages to install or None to use default package list.

    Examples
    --------
    .. code-block:: python

        >>> import compas_rhino
        >>> compas_rhino.install('6.0')

    .. code-block:: python

        $ python -m compas_rhino.install 6.0

    """

    print('Installing COMPAS packages to Rhino {0} IronPython lib:'.format(version))

    ipylib_path = compas_rhino._get_ironpython_lib_path(version)

    results = []
    exit_code = 0

    for package in packages:
        base_path = _get_package_path(importlib.import_module(package))
        package_path = os.path.join(base_path, package)
        symlink_path = os.path.join(ipylib_path, package)

        if os.path.exists(symlink_path):
            results.append(
                (package, 'ERROR: Package "{}" already found in Rhino lib, try uninstalling first'.format(package)))
            continue

        try:
            create_symlink(package_path, symlink_path)
            results.append((package, 'OK'))
        except OSError:
            results.append(
                (package, 'Cannot create symlink, try to run as administrator.'))

    for _, status in results:
        if status is not 'OK':
            exit_code = -1

    # Installing the bootstrapper rarely fails, so, only do it if no other package failed
    if exit_code == -1:
        results.append(('compas_bootstrapper', 'ERROR: One or more packages failed, will not install bootstrapper, try uninstalling first'))
    else:
        conda_prefix = os.environ.get('CONDA_PREFIX', None)
        try:
            with open(os.path.join(ipylib_path, 'compas_bootstrapper.py'), 'w') as f:
                f.write('CONDA_PREFIX = r"{0}"'.format(conda_prefix))
                results.append(('compas_bootstrapper', 'OK'))
        except:
            results.append(
                ('compas_bootstrapper', 'Could not create compas_bootstrapper to auto-determine Python environment'))

    for package, status in results:
        print('   {} {}'.format(package.ljust(20), status))

        # Re-check just in case bootstrapper failed
        if status is not 'OK':
            exit_code = -1

    print('\nCompleted.')
    sys.exit(exit_code)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    import sys

    print('\nusage: python -m compas_rhino.install [version]\n')
    print('  version       Rhino version (5.0 or 6.0)\n')

    try:
        version = sys.argv[1]
    except IndexError:
        version = '6.0'
    else:
        try:
            version = str(version)
        except Exception:
            version = '6.0'

    install(version=version, packages=INSTALLABLE_PACKAGES)
