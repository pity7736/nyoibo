from Cython.Build import cythonize
from setuptools import setup, Extension


extensions = (
    Extension('nyoibo.fields', ['nyoibo/fields.pyx']),
    Extension('nyoibo.entities.entity', ['nyoibo/entities/entity.pyx'])
)
setup(
    name='nyoibo',
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': 3}
    )
)
