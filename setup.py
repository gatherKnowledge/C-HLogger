from cx_Freeze import setup, Executable

base = None    

executables = [Executable("init.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "myLogger",
    options = options,
    version = "1.0",
    description = 'log maker',
    executables = executables
)
