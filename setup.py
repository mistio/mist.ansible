import sys
import os
import glob
import shutil
from setuptools import setup
from distutils.command.install import install as _install

here = os.path.abspath(os.path.dirname(__file__))


def _post_install():
    """
    Install mist modules to the ansible modules directory
    """
    try:
        from ansible.constants import DEFAULT_MODULE_PATH
    except ImportError:
        print
        print "Could not find ansible installed"
        print "Consider manually copying mist modules"
        sys.exit(1)

    module_dir = os.path.join(here, "mist.modules")
    modules = glob.glob(module_dir+"/*")

    mist_modules_dir = os.path.join(DEFAULT_MODULE_PATH, "mist.modules")
    if not os.path.isdir(mist_modules_dir):
        os.mkdir(mist_modules_dir)

    for module in modules:
        shutil.copy(module, mist_modules_dir)

    print
    print "Finished copying mist ansible modules"


class install(_install):
    def run(self):
        _install.run(self)
        _post_install()


requires = [
    'ansible'
]


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='mist.ansible',
    version='0.0.1',
    description='Ansible modules for the mist.io service',
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    url='https://github.com/mistio/mist.ansible',
    keywords=' ansible web cloud server management monitoring automation mobile libcloud pyramid amazon aws rackspace openstack linode softlayer digitalocean gce',
    author='Chris Loukas',
    author_email='commixon@gmail.com',
    license='AGPLv3',
    cmdclass={'install': install},
    install_requires=requires,
    zip_safe=False
)

