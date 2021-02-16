# setup.py
# from distutils.core import setup, Extension
#
# setup(name='sample',
#       ext_modules=[
#           Extension('sample',
#                     ['pysample.c'])
#
#       ]
#       )
from distutils.core import setup, Extension

setup(name='myModule', version='1.0',ext_modules=[Extension('myModule', ['test.c'])])
