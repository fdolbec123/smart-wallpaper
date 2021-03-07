from PyQt5.QtWidgets import *
import os
import locale
# End of imports


# main function
def main(langauage):
    print("We are on macOS!!!")
    main_app = QApplication([])
    main_window = QWidget()
    if langauage == "fr":
        main_window.setWindowTitle("Tableau de bord de Smart Wallpaper")
    else:
        main_window.setWindowTitle("Smart Wallpaper's Dashboard")
    button = QPushButton()
    main_window.show()
    center(main_window)

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
    test_language = locale.setlocale(locale.LC_ALL, "")
    print(test_language)
    if "fr" in test_language:
        print("Français")
        language = "fr"
    else:
        print("send to english")
        language = "en"
    main(language)
    # In case we need to do an inital setup, for example, create a folder in the ~/Pictures/ folder...


def center(window_to_center):
    frame = window_to_center.frameGeometry()
    ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
    frame.moveCenter(point_central)
    window_to_center.move(frame.topLeft())