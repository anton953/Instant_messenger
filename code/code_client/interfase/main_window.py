



from PyQt6.QtWidgets import QMainWindow, QPushButton

# Only needed for access to command line arguments
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Instant")
        button = QPushButton("ok")

        # Set the central widget of the Window.
        self.setCentralWidget(button)