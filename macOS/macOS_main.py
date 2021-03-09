from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import locale
# import subprocess
# import json
import applescript
# End of imports


# main function
def main(langauage):
    print("We are on macOS!!!")
    list_monitor = scan_screens()
    print(list_monitor)
    main_app = QApplication([])
    main_window = QWidget()
    main_window.setMinimumSize(852, 480)
    x_value = int(main_window.width() / 8)
    y_value = int(main_window.height() / 4)
    display_screens(list_monitor, x_value, y_value, main_window)
    presentation_button = QPushButton(main_window)
    public_button = QPushButton(main_window)
    private_button = QPushButton(main_window)
    other_button = QPushButton(main_window)
    refresh_button = QPushButton(main_window)
    if langauage == "fr":
        main_window.setWindowTitle("Tableau de bord de Smart Wallpaper")
        presentation_button.setText("Professionel")
        public_button.setText("Public")
        private_button.setText("Privé")
        other_button.setText("Autre...")
        refresh_button.setText("Actualiser")
    else:
        main_window.setWindowTitle("Smart Wallpaper's Dashboard")
        presentation_button.setText("Professional")
        public_button.setText("Public")
        private_button.setText("Private")
        other_button.setText("Other...")
        refresh_button.setText("Refresh")
    presentation_button.move((x_value - (presentation_button.size().width()/2)), (3 * y_value))
    public_button.move(((3 * x_value) - (public_button.size().width()/2)), (3 * y_value))
    private_button.move(((5 * x_value) - (private_button.size().width()/2)), (3 * y_value))
    other_button.move(((7 * x_value) - (other_button.size().width()/2)), (3 * y_value))
    refresh_button.move((main_window.width() - 10 - refresh_button.width()), 10)
    refresh_button.clicked.connect(lambda: reset_screens_info(x_value, y_value, main_window))
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
    # output = subprocess.getstatusoutput("system_profiler SPDisplaysDataType -json")
    script = applescript.run('tell application "System Events" to get name of desktops')
    print("Exit code is: " + str(script.code))
    if script.code == 0:
        list_of_monitor = script.out.split(", ")
        if len(set(list_of_monitor)) < len(list_of_monitor):
            print("Caution!!! Multiple monitors have the same name! There might be some conflicts and issues with this "
                  "program!")
        return list_of_monitor
    else:
        print("Oh oh! There's an error while executing the script! The error is the following: " + script.err)
    # 'tell application "System Events" to get name of desktops'
    # if output[0] == 0:
    #     # print(output[1])
    #     json_output = json.loads(output[1])
    #     # print(json_output)
    #     # sPDisplaysDataType = json_output["SPDisplaysDataType"]
    #     # print(type(sPDisplaysDataType))
    #     output_array = (json_output["SPDisplaysDataType"])
    #     output_dict = output_array[0]
    #     list_displays = output_dict["spdisplays_ndrvs"]
    #     print(len(list_displays))
    #     print(list_displays)
    #
    # else:
    #     print("Error! Can't get the information from command in terminal!")


def display_screens(list_of_avaible_screens, x, y, main_window):
    dict_screen = {}
    index_value = len(list_of_avaible_screens)
    for index, item in enumerate(list_of_avaible_screens):
        print(index, item)
        screen_icon = QPixmap("Ressources/icon_screen.png")
        screen_icon = screen_icon.scaledToWidth(161)
        screen_icon_label = QLabel(main_window)
        screen_icon_label.setPixmap(screen_icon)

        if "ACL" in item:
            screen_label = QLabel(main_window)
            screen_label.setText(item + "*")
            print(screen_label)
        else:
            screen_label = QLabel(main_window)
            screen_label.setText(item)
            print(screen_label)
        # vertical_box = QVBoxLayout(main_window)
        # vertical_box.addWidget(screen_icon_label)
        # vertical_box.addWidget(screen_label)


def reset_screens_info(x, y, main_window):
    list_reset = scan_screens()
    display_screens(list_reset, x, y, main_window)
