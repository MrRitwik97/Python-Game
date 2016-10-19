import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup( name = "Dodger",
       version = "1.0",
       description = "Dodge The Blocks!",
       executables = [Executable("game.py", base=base)])
