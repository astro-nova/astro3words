
from setuptools import setup, find_packages
import numpy
import re

# borrowed from orbitize: https://github.com/sblunt/orbitize
def get_requires():
    reqs = []
    for line in open('requirements.txt', 'r').readlines():
        reqs.append(line)
    return reqs

# auto-updating version code stolen from RadVel
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
                       open(project + '/__init__.py').read())
    return result.group(1)

setup(
    name='astro3words',
    version=get_property('__version__', 'astro3words'),
    description='astro3words - get a simple 3-word coordinate of your favorite object!',
    url='https://github.com/astro-nova/astro-3-words',
    author='',
    author_email='',
    license='MIT',
    packages=find_packages(),
    include_dirs=[numpy.get_include()],
    include_package_data = True,
    zip_safe=False,
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        # 'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
        ],
    keywords='Astronomy Astrometry',
    install_requires=get_requires()
    )

