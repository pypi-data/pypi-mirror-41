import os

from codecs import open
from setuptools import setup

import quilljs

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-quilljs',
    version=quilljs.__version__,
    author='Mukesh Yadav',
    author_email='mak.gnu@gmail.com',
    description='Easily use Quill.js in your django admin.',
    long_description=long_description,
    packages=['quilljs'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Editors :: Word Processors",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Text Processing :: Markup :: HTML"
    ]
)
