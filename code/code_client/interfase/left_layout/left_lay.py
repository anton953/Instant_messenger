import sys

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from interfase.left_layout.gamburger import Gamburger
from interfase.left_layout.list_chats import ListChats

class LeftWindow(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addWidget(Gamburger())
        self.addLayout(ListChats())