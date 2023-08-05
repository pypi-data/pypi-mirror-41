#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', os.path.join('.', 'build'), os.path.join('.', 'dist'), 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + os.path.sep, package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.base',
      version='0.3.36',
      description=('The base components of the docassemble system.'),
      long_description=read("README.md"),
      long_description_content_type='text/markdown',
      author='Jonathan Pyle',
      author_email='jhpyle@gmail.com',
      license='MIT',
      url='https://docassemble.org',
      download_url='https://download.docassemble.org/docassemble-base.tar.gz',
      namespace_packages = ['docassemble'],
      install_requires = ['docassemble==0.3.36', 'python-docx==0.8.7', '3to2', 'astunparse', 'babel', 'bcrypt', 'blinker', 'cffi', 'fdfgen', 'guess-language-spirit', 'httplib2', 'itsdangerous', 'jellyfish==0.5.6', 'jinja2', 'lxml', 'mako', 'markdown', 'markupsafe', 'mdx-smartypants', 'namedentities==1.5.2', 'passlib', 'pdfminer', 'pillow', 'pip', 'pycparser', 'pycrypto', 'geopy', 'pygments', 'pyjwt', 'pypdf', 'pypdftk', 'PyPDF2', 'python-dateutil', 'pytz', 'pyyaml', 'ruamel.yaml', 'qrcode', 'six', 'titlecase', 'wheel', 'pattern', 'tzlocal', 'us', 'phonenumbers', 'pycountry', 'ua-parser', 'user-agents', 'textstat', 'twine', 'docxtpl', 'qrtools', 'pylatex', 'pandas', 'XlsxWriter', 'xlwt'],
      packages=find_packages(),
      zip_safe = False,
      package_data=find_package_data(where=os.path.join('docassemble', 'base', ''), package='docassemble.base'),
     )
