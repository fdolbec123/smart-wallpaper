from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import locale
import applescript
import random
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
    ticked_box = []
    display_screens(list_monitor, y_value, main_window, langauage, dict_screens)
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
    refresh_button.clicked.connect(lambda: reset_screens_info(y_value, main_window, langauage, dict_screens))
    presentation_button.clicked.connect(lambda: set_professional(dict_screens, list_monitor, ticked_box))
    public_button.clicked.connect(lambda: set_public(dict_screens, list_monitor, ticked_box))
    private_button.clicked.connect(lambda: set_private(dict_screens, list_monitor, ticked_box))
    other_button.clicked.connect(lambda: set_other(dict_screens, list_monitor, ticked_box))
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


def display_screens(list_of_avaible_screens, y, main_window, language, dict_screens):
    if dict_screens != {}:
        print("empty")
    splitting = (main_window.width() / (len(list_of_avaible_screens) + 1))
    print(splitting)
    for index, item in enumerate(list_of_avaible_screens):
        screen_icon = QPixmap("Ressources/icon_screen.png")
        screen_icon = screen_icon.scaledToWidth(160)
        screen_icon_label = QLabel(main_window)
        screen_icon_label.setPixmap(screen_icon)
        dict_screens["icon{0}".format(index)] = screen_icon_label
        screen_icon_label.show()
        screen_icon_label.move(((index + 1) * splitting) - 80, y)
        if "ACL" in item:
            check_box = QCheckBox((item + "*"), main_window)
            dict_screens["check_box{0}".format(index)] = check_box
            print(dict_screens)
            check_box.show()
            screen_notice = QLabel(main_window)
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
            print(dict_screens)
        check_box.move(((index + 1) * splitting) - (check_box.width() / 2), (2 * y) + 20)


def destrcution(dict_screens):
    if dict_screens != {}:
        print("Not empty")
        print(dict_screens)
        for key in dict_screens:
            dict_screens[key].close()
            print(dict_screens)
        dict_screens = {}
        print(dict_screens)

    else:
        print("Empty")
    del dict_screens


def reset_screens_info(y, main_window, language, dict_screens):
    destrcution(dict_screens)
    list_reset = scan_screens()
    display_screens(list_reset, y, main_window, language, dict_screens)
    print("This is the dictionnary of the avaible screens right now: " + str(dict_screens))


def set_public(dict_screens, list_of_monitor, ticked_box):
    print(dict_screens)
    for key in dict_screens:
        print(dict_screens[key])
        if type(dict_screens[key]) is QCheckBox:
            print("It's a checkbox!!!")
            if dict_screens[key].isChecked():
                print("ticked!")
                desktop_choosed_str = str(key)
                number_desktop = desktop_choosed_str[-1]
                print(list_of_monitor[int(number_desktop)])
                subfolder = "~/Pictures/Smart-Wallpaper/Public/"
                my_custom_subfolder = os.path.expanduser(subfolder)
                file_picked = random.choice(os.listdir(my_custom_subfolder))
                while file_picked.startswith("."):
                    file_picked = random.choice(os.listdir(my_custom_subfolder))
                    print(file_picked)
                print(file_picked)
                print(str(my_custom_subfolder))
                script_to_run = 'tell application "System Events" to set picture of desktop "' + \
                                str(list_of_monitor[int(number_desktop)]) + '" to "' + str(my_custom_subfolder) \
                                + file_picked + '"'
                print(script_to_run)
                change_picture = applescript.run(script_to_run)
                print("Exit code is : " + str(change_picture.code))
            else:
                print("not ticked")
        print(ticked_box)


def set_professional(dict_screens, list_of_monitor, ticked_box):
    print(dict_screens)
    for key in dict_screens:
        print(dict_screens[key])
        if type(dict_screens[key]) is QCheckBox:
            print("It's a checkbox!!!")
            if dict_screens[key].isChecked():
                print("ticked!")
                desktop_choosed_str = str(key)
                number_desktop = desktop_choosed_str[-1]
                print(list_of_monitor[int(number_desktop)])
                subfolder = "~/Pictures/Smart-Wallpaper/Professional/"
                my_custom_subfolder = os.path.expanduser(subfolder)
                file_picked = random.choice(os.listdir(my_custom_subfolder))
                while file_picked.startswith("."):
                    file_picked = random.choice(os.listdir(my_custom_subfolder))
                    print(file_picked)
                print(file_picked)
                print(str(my_custom_subfolder))
                script_to_run = 'tell application "System Events" to set picture of desktop "' + \
                                str(list_of_monitor[int(number_desktop)]) + '" to "' + str(my_custom_subfolder) \
                                + file_picked + '"'
                print(script_to_run)
                change_picture = applescript.run(script_to_run)
                print("Exit code is : " + str(change_picture.code))
            else:
                print("not ticked")
        print(ticked_box)


def set_private(dict_screens, list_of_monitor, ticked_box):
    print(dict_screens)
    for key in dict_screens:
        print(dict_screens[key])
        if type(dict_screens[key]) is QCheckBox:
            print("It's a checkbox!!!")
            if dict_screens[key].isChecked():
                print("ticked!")
                desktop_choosed_str = str(key)
                number_desktop = desktop_choosed_str[-1]
                print(list_of_monitor[int(number_desktop)])
                subfolder = "~/Pictures/Smart-Wallpaper/Private/"
                my_custom_subfolder = os.path.expanduser(subfolder)
                file_picked = random.choice(os.listdir(my_custom_subfolder))
                while file_picked.startswith("."):
                    file_picked = random.choice(os.listdir(my_custom_subfolder))
                    print(file_picked)
                print(file_picked)
                print(str(my_custom_subfolder))
                script_to_run = 'tell application "System Events" to set picture of desktop "' + \
                                str(list_of_monitor[int(number_desktop)]) + '" to "' + str(my_custom_subfolder) \
                                + file_picked + '"'
                print(script_to_run)
                change_picture = applescript.run(script_to_run)
                print("Exit code is : " + str(change_picture.code))
            else:
                print("not ticked")
        print(ticked_box)


def set_other(dict_screens, list_of_monitor, ticked_box):
    print(dict_screens)
    for key in dict_screens:
        print(dict_screens[key])
        if type(dict_screens[key]) is QCheckBox:
            print("It's a checkbox!!!")
            if dict_screens[key].isChecked():
                print("ticked!")
                desktop_choosed_str = str(key)
                number_desktop = desktop_choosed_str[-1]
                print(list_of_monitor[int(number_desktop)])
                subfolder = "~/Pictures/Smart-Wallpaper/Other/"
                my_custom_subfolder = os.path.expanduser(subfolder)
                file_picked = random.choice(os.listdir(my_custom_subfolder))
                while file_picked.startswith("."):
                    file_picked = random.choice(os.listdir(my_custom_subfolder))
                    print(file_picked)
                print(file_picked)
                print(str(my_custom_subfolder))
                script_to_run = 'tell application "System Events" to set picture of desktop "' + \
                                str(list_of_monitor[int(number_desktop)]) + '" to "' + str(my_custom_subfolder) \
                                + file_picked + '"'
                print(script_to_run)
                change_picture = applescript.run(script_to_run)
                print("Exit code is : " + str(change_picture.code))
            else:
                print("not ticked")
        print(ticked_box)
