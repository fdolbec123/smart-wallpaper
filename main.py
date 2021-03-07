import platform
from macOS import macOS_main
hostOS = platform.system()
print(hostOS)
if hostOS == "Darwin":
    macOS_main.initial_setup()
