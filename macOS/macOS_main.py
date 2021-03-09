from PyQt5.QtWidgets import *
import os
import locale
import subprocess
import json
# End of imports


# main function
def main(langauage):
    print("We are on macOS!!!")
    scan_screens()
    main_app = QApplication([])
    main_window = QWidget()
    main_window.setMinimumSize(852, 480)
    presentation_button = QPushButton(main_window)
    public_button = QPushButton(main_window)
    private_button = QPushButton(main_window)
    other_button = QPushButton(main_window)
    if langauage == "fr":
        main_window.setWindowTitle("Tableau de bord de Smart Wallpaper")
        presentation_button.setText("Professionel")
        public_button.setText("Public")
        private_button.setText("Privé")
        other_button.setText("Autre...")
    else:
        main_window.setWindowTitle("Smart Wallpaper's Dashboard")
        presentation_button.setText("Professional")
        public_button.setText("Public")
        private_button.setText("Private")
        other_button.setText("Other...")
    presentation_button.move(10, 10)
    public_button.move(10, 40)
    private_button.move(10, 70)
    other_button.move(10, 100)
    other_button.setEnabled(False)
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


def scan_screens():
    output = subprocess.getstatusoutput("system_profiler SPDisplaysDataType -json")
    if output[0] == 0:
        # print(output[1])
        json_output = json.loads(output[1])
        # print(json_output)
        # sPDisplaysDataType = json_output["SPDisplaysDataType"]
        # print(type(sPDisplaysDataType))
        output_array = (json_output["SPDisplaysDataType"])
        output_dict = output_array[0]
        list_displays = output_dict["spdisplays_ndrvs"]
        print(len(list_displays))

    else:
        print("Error! Can't get the information from command in terminal!")
