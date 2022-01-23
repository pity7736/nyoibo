import os

from setuptools import setup, Extension, find_packages

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

if USE_CYTHON:
    ext = 'pyx'
else:
    ext = 'c'

init_file = os.path.join(
    os.path.dirname(__file__),
    'nyoibo',
    '__init__.py'
)

with open(init_file) as f:
    for line in f:
        if line.startswith('__version__ ='):
            _, _, version = line.partition('=')
            VERSION = version.strip(" \n'\"")
            break

with open('README.rst') as f:
    readme = f.read()

tests_require = [
    'pytest==6.2.5'
    'pytest-cov==3.0.0'
]

extensions = [
    Extension('nyoibo.fields', [f'nyoibo/fields.{ext}']),
    Extension('nyoibo.entities.entity', [f'nyoibo/entities/entity.{ext}'])
]

for e in extensions:
    e.cython_directives = {"embedsignature": True}


if USE_CYTHON:
    extensions = cythonize(
        extensions,
        compiler_directives={'language_level': 3}
    )

setup(
    name='nyoibo',
    version=VERSION,
    packages=find_packages(),
    author='Julián Cortés',
    author_email='pity7736@gmail.com',
    description='Implement attributes accessors in an easy way',
    long_description=readme,
    keywords='accessors private',
    ext_modules=extensions,
    url='https://github.com/pity7736/nyoibo',
    tests_require=tests_require,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'Typing :: Typed'
    ]
)
