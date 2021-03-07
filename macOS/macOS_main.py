from PyQt5.QtWidgets import *
import os
# End of imports


# main function
def main():
    print("We are on macOS!!!")
    main_app = QApplication([])
    main_window = QWidget()
    main_window.setWindowTitle("Smart Wallpaper")
    main_window.show()

    main_app.exec_()


# initial_setup function
# Used to make sure the app works properly.
def initial_setup():
    custom_wallpaper_folder_path = "~/Pictures/Smart-Wallpaper/"
    my_custom_dir = os.path.expanduser(custom_wallpaper_folder_path)  # Custom absolute folder path with username in it.
    if os.path.isdir(my_custom_dir):
        print("The folder is already there! Yay!")
        print(os.path.expanduser(custom_wallpaper_folder_path))
    else:
        print("Need to create the folder so the app can work properly.")
        try:
            # Create target Directory
            os.mkdir(my_custom_dir)
            print("Directory ", my_custom_dir, " Created ")
        except FileExistsError:
            print("Directory ", my_custom_dir, " already exists")
    main()
    # In case we need to do an inital setup, for example, create a folder in the ~/Pictures/ folder...
