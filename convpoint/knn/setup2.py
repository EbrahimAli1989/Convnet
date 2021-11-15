from distutils.core import setup
from Cython.Distutils import Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(Extension(
        "bla.combined",
        ["knn.pyx"])),
    requires=['Cython'])