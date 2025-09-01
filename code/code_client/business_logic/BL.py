from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
import sys
#commit

class BusinessLogic():
    def __init__(self):
        self.interface_init()
        # self.main_while()
        

    def server_get_info(self):
        pass

    def interface_init(self):


        app = QApplication(sys.argv)
    
        engine = QQmlApplicationEngine()

        engine.load(QUrl.fromLocalFile("code/code_client/interface/QML/main_window.qml"))

    
        if not engine.rootObjects():
            sys.exit(-1)
    

        sys.exit(app.exec())

    def main_while():
        while True:
            pass