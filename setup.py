
#Exe Deployment Configuration  with py2exe

from distutils.core import setup
import py2exe

setup(

    windows=['multiwinmain.py'],
    options = {
        "py2exe": {
            "dll_excludes": ["MSVCP90.dll"]
        }
    }

)