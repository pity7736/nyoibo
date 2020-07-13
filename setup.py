from setuptools import setup, Extension
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

if USE_CYTHON:
    ext = 'pyx'
else:
    ext = 'c'

extensions = [
    Extension('nyoibo.fields', [f'nyoibo/fields.{ext}']),
    Extension('nyoibo.entities.entity', [f'nyoibo/entities/entity.{ext}'])
]

if USE_CYTHON:
    extensions = cythonize(
        extensions,
        compiler_directives={'language_level': 3}
    )

setup(
    name='nyoibo',
    ext_modules=extensions
)
