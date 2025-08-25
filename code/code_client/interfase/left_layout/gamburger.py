import sys

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton
)


class Gamburger(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Нажми меня", self)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Кнопка нажата!")