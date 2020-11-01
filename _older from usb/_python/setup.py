from cx_Freeze import setup, Executable

base = None


executables = [Executable("line finder.py", base=base)]

packages = ["urllib"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
