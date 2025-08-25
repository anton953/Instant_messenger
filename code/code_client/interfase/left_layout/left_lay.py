import sys

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from code_client.interfase.left_window.gamburger import Gamburger
from code_client.interfase.left_window.list_chats import ListChats

class LeftWindow(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addWidget(Gamburger)
        self.addWidget(ListChats)