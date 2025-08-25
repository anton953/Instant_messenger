import sys

from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from code_client.interfase.left_layout.left_lay import LeftWindow
from code_client.interfase.right_layout.right_lay import RightLay


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Instant")        
        self.setGeometry(300, 300, 800, 500)


        self.main_lay = QHBoxLayout(self)

        self.main_lay.addLayout(LeftWindow())
        self.main_lay.addLayout(RightLay())

        central_widget = QWidget()
        central_widget.setLayout(self.main_lay)
        self.setCentralWidget(central_widget)