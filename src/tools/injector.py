import subprocess
import os
from pathlib import Path


def inject_dll(addon_prefs):
    scriptPath = Path(addon_prefs.scriptPath)
    injectorExePath = scriptPath.joinpath("tools", "SimpleInjector.exe")
    dllPath = scriptPath.joinpath("tools", "BlenderPerfPatch.dll")

    subprocess.run([injectorExePath, dllPath, str(os.getpid())])
