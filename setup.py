from distutils.core import setup, Extension
setup(name='helloworld', version='1.0', ext_modules=[Extension('helloworld', sources=['hello.c'])])

