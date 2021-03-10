from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import locale
# import subprocess
# import json
import applescript
from functools import partial
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
    dict_screens = {}
    # dict_screens_full = display_screens(list_monitor, x_value, y_value, main_window, langauage, dict_screens)
    display_screens(list_monitor, x_value, y_value, main_window, langauage, dict_screens)
    print(dict_screens)
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
    refresh_button.clicked.connect(lambda: reset_screens_info(x_value, y_value, main_window, langauage, dict_screens))
    # delete_button.clicked.connect(lambda: destrcution(dict_screens, main_window, delete_button))
    other_button.setEnabled(False)
    main_window.show()
    center(main_window)

    main_app.exec_()


# initial_setup function
# Used to make sure the app works properly.
def initial_setup():
    custom_wallpaper_folder_path = "~/Pictures/Smart-Wallpaper/"
    my_custom_dir = os.path.expanduser(custom_wallpaper_folder_path)  # Custom absolute folder path with username in it.
    subfolder1 = "~/Pictures/Smart-Wallpaper/Professional"
    subfolder2 = "~/Pictures/Smart-Wallpaper/Public"
    subfolder3 = "~/Pictures/Smart-Wallpaper/Private"
    subfolder4 = "~/Pictures/Smart-Wallpaper/Other"
    my_custom_subfolder1 = os.path.expanduser(subfolder1)
    my_custom_subfolder2 = os.path.expanduser(subfolder2)
    my_custom_subfolder3 = os.path.expanduser(subfolder3)
    my_custom_subfolder4 = os.path.expanduser(subfolder4)
    if os.path.isdir(my_custom_dir):
        print("The folder is already there! Yay! Let's check if subfolders are there too!")
        print(os.path.expanduser(custom_wallpaper_folder_path))
        if os.path.isdir(my_custom_subfolder1):
            pass
        else:
            os.mkdir(my_custom_subfolder1)
        if os.path.isdir(my_custom_subfolder2):
            pass
        else:
            os.mkdir(my_custom_subfolder2)
        if os.path.isdir(my_custom_subfolder3):
            pass
        else:
            os.mkdir(my_custom_subfolder3)
        if os.path.isdir(my_custom_subfolder4):
            pass
        else:
            os.mkdir(my_custom_subfolder4)
    else:
        print("Need to create the folder so the app can work properly.")
        try:
            # Create target Directory
            os.mkdir(my_custom_dir)
            print("Directory ", my_custom_dir, " Created ")
            os.mkdir(my_custom_subfolder1)
            os.mkdir(my_custom_subfolder2)
            os.mkdir(my_custom_subfolder3)
            os.mkdir(my_custom_subfolder4)
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


def display_screens(list_of_avaible_screens, x, y, main_window, language, dict_screens):
    if dict_screens != {}:
        print("empty")
    splitting = (main_window.width() / (len(list_of_avaible_screens) + 1))
    print(splitting)
    # index_value = len(list_of_avaible_screens)
    # horizontal_box = QHBoxLayout(main_window)
    # horizontal_box2 = QHBoxLayout(main_window)

    for index, item in enumerate(list_of_avaible_screens):
        # dict_screens[item] = {}
        # group = QGroupBox(main_window)
        # print(index, item)
        # # horizontal_box = QHBoxLayout(group)
        screen_icon = QPixmap("Ressources/icon_screen.png")
        screen_icon = screen_icon.scaledToWidth(160)
        screen_icon_label = QLabel(main_window)
        screen_icon_label.setPixmap(screen_icon)
        dict_screens["icon{0}".format(index)] = screen_icon_label
        screen_icon_label.show()
        screen_icon_label.move(((index + 1) * splitting) - 80, y)
        # screen_icon_label.show()
        # dict_screens[item]["image"] = screen_icon_label
        # radio_button = QRadioButton(main_window)
        # dict_screens[item]["radio_button"] = radio_button
        # # horizontal_box.addWidget(radio_button)
        # # horizontal_box.addWidget(screen_icon_label)
        if "ACL" in item:
            check_box = QCheckBox((item + "*"), main_window)
            dict_screens["check_box{0}".format(index)] = check_box
            print(dict_screens)
            check_box.show()
            screen_notice = QLabel(main_window)
            # group.setTitle(item + "*")
            if language == "fr":
                screen_notice.setText("* Le nom de cet écran correspond probablement à l'écran interne de votre Mac.")
            else:
                screen_notice.setText("* This is probably the name of your internal Mac screen.")
            print(dict_screens)
            screen_notice.move(10, (main_window.height() - 10 - screen_notice.height()))
            dict_screens["notice"] = screen_notice
            screen_notice.show()
        else:
            check_box = QCheckBox(item, main_window)
            dict_screens["check_box{0}".format(index)] = check_box
            print(dict_screens)
            check_box.show()
            # group.setTitle(item)
            # screen_label = QLabel(main_window)
            # screen_label.setText(item)
            print(dict_screens)
        check_box.move(((index + 1) * splitting) - (check_box.width() / 2), (2 * y) + 20)
        # # horizontal_box.addWidget(screen_icon_label)
        # # horizontal_box2.addWidget(screen_label)
        # # dict_screens[item]["group"] = group
        # print(index)
        # x_value_for_group = (main_window.width() / ((len(list_of_avaible_screens)) + 1))
        # print(x_value_for_group)
        # group_value = (radio_button.width() + screen_icon_label.width())/2
        # print(group_value)
        # x_place = ((x_value_for_group * ((int(index)) + 1)) - group_value)
        # print(x_place)
        # # group.move(x_place, (0.75 * y))
    # return dict_screens


def destrcution(dict_screens, main_window):
    if dict_screens != {}:
        print("Not empty")
        print(dict_screens)
        # if "radio_button0" in dict_screens:
        #     dict_screens["radio_button0"].deleteLater()
        #     del dict_screens["radio_button0"]
        #     print(dict_screens)
        for key in dict_screens:
            dict_screens[key].close()
            print(dict_screens)
        dict_screens = {}
        print(dict_screens)

    else:
        print("Empty")
    del dict_screens


def reset_screens_info(x, y, main_window, language, dict_screens):
    destrcution(dict_screens, main_window)
    list_reset = scan_screens()
    display_screens(list_reset, x, y, main_window, language, dict_screens)
    print("This is the dictionnary of the avaible screens right now: " + str(dict_screens))
