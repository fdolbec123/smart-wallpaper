import platform
from macOS import macOS_main
hostOS = platform.system()
print(hostOS)
if hostOS == "Darwin":
    macOS_main.initial_setup()
elif hostOS == "Linux":
    pass
elif hostOS == "Windows":
    pass
else:
    print("Sorry, but this OS is not supported. This program is going to quit.")
