"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytest_gh_log_group',
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description='pytest plugin for gh actions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/embedded-community/pytest_gh_log_group',
    author='Jussi Vatjus-Anttila',
    author_email='jussiva@gmail.com',

    # Classifiers help users find your project by categorizing it.
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        'Framework :: Pytest',
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['tests']),
    keywords="py.test pytest github actions log grouping",
    python_requires='>=3.7, <4',
    entry_points={
        'pytest11': ['builds = source.plugin']

    },
    install_requires=[
        'pytest'
    ],
    extras_require={
        'dev': ['pytest-cov', 'pylint']
    },

    project_urls={  # Optional
        'Source': 'https://github.com/embedded-community/pytest_gh_log_group',
    }
)