import os,shutil,sys
import py_compile
platform = sys.argv[1]
BuildName = (sys.argv[2])+"_"+platform


files_to_copy: list[str] = [
    "cminter.pyc",
    "Create.py",
    "edit.py",
    "menuconfig.py",
    "package.toml",
    "pkg.py",
    "Remove.py",
    "shell.py",
    "source.py",
    "Spiner_settings.json",
    ("Spiner.sh" if platform == "Unix" else "Spiner.bat"),
    "UseConfig"
]

BuildDir = "Build"

if not os.path.exists(os.path.join(BuildDir,BuildName)):
    os.mkdir(os.path.join(BuildDir,BuildName))
else:
    shutil.rmtree(os.path.join(BuildDir,BuildName))
    os.mkdir(os.path.join(BuildDir,BuildName))

for file in files_to_copy:
    if file.endswith(".py"):
        py_compile.compile(file)
        without_ext = file[:-3]
        shutil.copy(f"__pycache__\\{without_ext}.cpython-312.pyc", f"{BuildDir}\\{BuildName}\\{without_ext}.pyc")
        shutil.rmtree("__pycache__")
    else:
        shutil.copy(file,f"{BuildDir}\\{BuildName}\\{file}")

