from codecs import open
from os import path
from setuptools import setup, find_packages
from megalus import __version__
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

here = path.abspath(path.dirname(__file__))

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Megalus',
    version=__version__,
    description='Command line helpers for docker and docker-compose',
    long_description=long_description,
    author='Chris Maillefaud',
    include_package_data=True,
    # Choose your license
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='aws deploy docker npm redis memcached bash',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'meg=megalus.cmd:start'
        ],
    },
)
