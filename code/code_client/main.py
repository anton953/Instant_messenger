import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl


app = QApplication(sys.argv)
    
engine = QQmlApplicationEngine()

engine.load(QUrl.fromLocalFile("code/code_client/interface/QML/main_window.qml"))

    
if not engine.rootObjects():
    sys.exit(-1)
    
if __name__ == "__main__":
    sys.exit(app.exec())