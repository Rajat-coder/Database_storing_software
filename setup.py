import sys, os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "tcl\\tk8.6"


# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": ["os","tkinter","babel.numbers"], "include_files": ["tcl86t.dll", "tk86t.dll"]}
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
 base = "Win32GUI"


setup( name = "TRADEMARK",
 version = "1.0",
 description = "SHANDA&CO",
 options = {"build_exe": build_exe_options},
 executables = [Executable("MainFile.py", base=base)])