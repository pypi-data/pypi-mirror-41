import setuptools
from pytzer import __version__

with open('README.md','r') as fh:
    long_description = fh.read()

setuptools.setup(
    name         = 'pytzer',
    version      = __version__,
    author       = 'Matthew P. Humphreys',
    author_email = 'm.p.humphreys@cantab.net',
    description  = 'Pitzer model for chemical speciation',
    url          = 'https://github.com/mvdh7/pytzer',
    packages     = setuptools.find_packages(),
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    classifiers = (
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry'),)
