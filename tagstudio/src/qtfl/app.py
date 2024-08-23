from typing import List
from PyQt6.QtWidgets import QApplication
from gui import MainWindow

class TagStudioApp(QApplication):

    def __init__(self, argv: List[str]) -> None:
        super().__init__(argv)

        self.main_window = MainWindow()