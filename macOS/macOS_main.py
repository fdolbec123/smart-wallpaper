from PyQt5.QtWidgets import *
def main():
    print("We are on macOS!!!")
    main_app = QApplication()
    main_window = QWidget()
    main_window.show()

    main_app.exec_()


def initial_setup():
    pass
    # In case we need to do an inital setup, for example, create a folder in the ~/Pictures/ folder...
