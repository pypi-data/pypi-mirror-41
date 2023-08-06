import setuptools

with open('README.md','r') as fh:
    long_description = fh.read()

setuptools.setup(
    name         = 'aqualibrium',
    version      = '0.0.1',
    author       = 'Matthew P. Humphreys',
    author_email = 'm.p.humphreys@cantab.net',
    description  = 'Equilibrium solver for aqueous solutions',
    url          = 'https://github.com/mvdh7/aqualibrium',
    packages     = setuptools.find_packages(),
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    classifiers = (
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry'),)
