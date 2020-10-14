import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Hemang\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Hemang\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("YouTube_download.py", base=base, icon="YouTube.ico")]


cx_Freeze.setup(
    name = "You Tube Downloader",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["YouTube.ico",'tcl86t.dll','tk86t.dll', 'A.png']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
