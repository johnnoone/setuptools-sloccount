import sys, os
from setuptools import setup, find_packages
from pkg_resources import DistributionNotFound

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join('src'))

from setuptools_sloccount.utils import check_requirement

try:
    check_requirement()
except:
    print
    print 'sloccount is required for this package, but it was unable to find it.'
    print 'please install it before install this package.'
    print 'refer to you distro for installing it.'
    print
    sys.exit()

README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1'

setup(name='setuptools_sloccount',
    version=version,
    description="Setuptools command for sloccount",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Topic :: Documentation",
        "Framework :: Setuptools Plugin",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: BSD License',
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='sloccount setuptools command',
    author='Xavier Barbosa',
    author_email='',
    url='',
    license='BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        "distutils.commands": [
            "sloccount = setuptools_sloccount.setuptools_command:SloccountCommand",
        ]
    }
)
