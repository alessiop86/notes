__author__ = 'John'

from distutils.core import setup
import py2exe

setup(

    windows=['test.py'],
    options = {
        "py2exe": {
            "dll_excludes": ["MSVCP90.dll"]
        }
    }

)