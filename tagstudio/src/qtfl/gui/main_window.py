"""
TagStudio main window
---------------------
Container of everything you see
"""
# External
from PyQt6.QtGui import QIcon
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import SplashScreen
from PyQt6.QtCore import QEventLoop
from PyQt6.QtCore import QTimer
from qfluentwidgets import FluentWindow
import logging

# TagStudio
from src.core.constants import VERSION_BRANCH
from src.core.constants import VERSION

# QtFl
from utils.i18n import _
from config import QtFlGuiPaths as pt


class MainWindow(FluentWindow):
    """
    The container for everything visual-related
    """
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName('main_window')

        # Temporarily force splash time
        self.splash_screen = SplashScreen(pt.Resx.ICON_PNG, self)
        self.show()
        self._init_self()
        self.loop_3_seconds()
        self.splash_screen.finish()

    def loop_3_seconds(self) -> None:
        loop = QEventLoop(self)
        QTimer.singleShot(3000, loop.quit)
        loop.exec()

    def _init_self(self) -> None:
        """ Load contents of this specific window """
        self.setWindowIcon(QIcon(pt.Resx.ICON_ICO))
        try:
            with open(pt.Qss.MAIN_WINDOW, 'r', encoding='utf-8') as raw_file:
                self.setStyleSheet(raw_file.read())
        except FileNotFoundError:
            logging.error(f"No Qss for MainWindow was found")
        self.setWindowTitle(f"TagStudio {VERSION}~{VERSION_BRANCH}")