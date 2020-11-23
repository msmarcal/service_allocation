from pathlib import Path
from setuptools import setup

README = Path('README.md').open('r').read()
REQUIREMENTS = Path('requirements.txt').open('rt').read().strip().split('\n')
VERSION = open(Path('VERSION.txt')).read().strip()

setup(
    name='service-allocation',
    version=VERSION,
    description='''
        Generates a CSV with the services allocation of an OpenStack Cloud.
    ''',
    long_description=README,
    long_description_content_type='text/markdown',
    platforms=['any'],
    author='Marcelo Subtil Marcal',
    author_email='marcelo.marcal@canonical.com',
    url='',
    license='MIT',
    py_modules=['service_allocation'],
    packages=['service_allocation'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Intended Audience :: System Administrators',
    ],
    install_requires=REQUIREMENTS,
    entry_points='''
        [console_scripts]
        service-allocation=service_allocation.service_allocation:main
    ''',
)
