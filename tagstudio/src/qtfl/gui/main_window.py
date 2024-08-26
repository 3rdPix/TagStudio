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
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from qfluentwidgets import CommandBar
from qframelesswindow import FramelessWindow
from qfluentwidgets import TransparentDropDownPushButton
from qfluentwidgets import RoundMenu
from qfluentwidgets import Action
from PyQt6.QtWidgets import QSpacerItem
from qfluentwidgets import PillToolButton
from qfluentwidgets import SearchLineEdit
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QFrame
from qfluentwidgets import ComboBox
from qfluentwidgets import ImageLabel
from qfluentwidgets import DisplayLabel

# TagStudio
from src.core.constants import VERSION_BRANCH
from src.core.constants import VERSION

# QtFl
from utils.i18n import _
from config import QtFlGuiPaths as pt
from gui.views import SidePanel
from gui.views import WorkingArea

class MainWindow(FramelessWindow):
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
        self.construye_la_interfaz_loco()
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

    def construye_la_interfaz_loco(self) -> None:
        window_layout: QVBoxLayout = QVBoxLayout(self)
        
        self.command_bar: CommandBar = CommandBar(self)
        window_layout.addSpacing(20) # needed to not collide with exit button
        window_layout.addWidget(self.command_bar)
        window_layout.addStretch()
        
        # File button
        file_button = TransparentDropDownPushButton(
            QIcon(pt.Resx.ICON_ICO), _("COMMANDBAR_FILE_BUTTON"))
        file_menu = RoundMenu()
        file_menu.addActions([
            Action(FIF.ADD, _("COMMANDBAR_FILE_MENU_ADD")),
            Action(FIF.SAVE, _("COMMANDBAR_FILE_MENU_SAVE")),
            Action(FIF.BOOK_SHELF, _("COMMANDBAR_FILE_MENU_SAVE_BACKUP"))])
        file_menu.addSeparator()
        file_menu.addAction(Action(FIF.UPDATE, _("COMMANDBAR_FILE_MENU_REFRESH")))
        file_menu.addSeparator()
        file_menu.addAction(Action(FIF.CLOSE, _("COMMANDBAR_FILE_MENU_CLOSE")))
        file_button.setMenu(file_menu)
        self.command_bar.addWidget(file_button)

        # Edit button
        edit_button = TransparentDropDownPushButton(
            FIF.EDIT, _("COMMANDBAR_EDIT_BUTTON"))
        edit_menu = RoundMenu()
        edit_menu.addAction(Action(FIF.TAG, _("COMMANDBAR_EDIT_MENU_NEW")))
        edit_menu.addSeparator()
        edit_menu.addActions([
            Action(FIF.CHECKBOX, _("COMMANDBAR_EDIT_MENU_SELECTALL")),
            Action(FIF.CLEAR_SELECTION, _("COMMANDBAR_EDIT_MENU_CLEARSELECT"))])
        edit_menu.addSeparator()
        edit_menu.addActions([
            Action(FIF.APPLICATION, _("COMMANDBAR_EDIT_MENU_MANAGE_EXNTENSION")),
            Action(FIF.IOT, _("COMMANDBAR_EDIT_MENU_MANAGE_TAGS"))])
        edit_button.setMenu(edit_menu)
        self.command_bar.addWidget(edit_button)

        # Tools button
        tools_button = TransparentDropDownPushButton(
            FIF.DEVELOPER_TOOLS, _("COMMANDBAR_TOOLS_BUTTON"))
        tools_menu = RoundMenu()
        tools_menu.addActions([
            Action(FIF.UNPIN, _("COMMANDBAR_TOOLS_MENU_FIX_ENTRIES")),
            Action(FIF.UNPIN, _("COMMANDBAR_TOOLS_MENU_FIX_DUPLICATE")),
            Action(FIF.LAYOUT, _("COMMANDBAR_TOOLS_MENU_NEW_COLLAGE"))])
        tools_button.setMenu(tools_menu)
        self.command_bar.addWidget(tools_button)

        # Macros button
        macros_button = TransparentDropDownPushButton(
            FIF.DICTIONARY, _("COMMANDBAR_MACROS_BUTTON"))
        macros_menu = RoundMenu()
        macros_menu.addActions([
            Action(_("COMMANDBAR_MACROS_MENU_AUTOFILL")),
            Action(_("COMMANDBAR_MACROS_MENU_SORT")),
            Action(_("COMMANDBAR_MACROS_MENU_FOLDERS"))])
        macros_button.setMenu(macros_menu)
        self.command_bar.addWidget(macros_button)

        # Window button
        window_button = TransparentDropDownPushButton(
            FIF.FIT_PAGE, _("COMMANDBAR_WINDOW_BUTTON"))
        window_menu = RoundMenu()
        window_menu.addActions(
            [Action(_("COMMANDBAR_WINDOW_MENU_OPEN_AT_START"), checkable=True),
            Action(_("COMMANDBAR_WINDOW_MENU_SHOW_RECENT"), checkable=True)])
        window_button.setMenu(window_menu)
        self.command_bar.addWidget(window_button)

        # Help button
        help_button = TransparentDropDownPushButton(
            FIF.HELP, _("COMMANDBAR_HELP_BUTTON"))
        help_menu = RoundMenu()
        help_menu.addAction(Action(
            FIF.GITHUB, _("COMMANDBAR_HELP_MENU_GITHUB")))
        help_button.setMenu(help_menu)
        self.command_bar.addWidget(help_button)

        self.command_bar.addSeparator()

        # Navigation
        extender_frame = QFrame()
        frame_horizontal_extender = QHBoxLayout(extender_frame)
        navigate_back_button = PillToolButton(FIF.LEFT_ARROW)
        navigate_forw_button = PillToolButton(FIF.RIGHT_ARROW)
        search_bar = SearchLineEdit()
        search_bar.setPlaceholderText(_("SEARCHBAR_PLACEHOLDER"))
        frame_horizontal_extender.addWidget(navigate_back_button, 0)
        frame_horizontal_extender.addWidget(navigate_forw_button, 0)
        frame_horizontal_extender.addWidget(search_bar, 1)
        self.command_bar.addWidget(extender_frame)

        # Tag Env
        working_area = WorkingArea()
        
        # Side panel
        side_panel = SidePanel()

        mainwindow_lowerhalf_layout = QHBoxLayout()
        mainwindow_lowerhalf_layout.addWidget(working_area, 3)
        mainwindow_lowerhalf_layout.addWidget(side_panel, 1)
        window_layout.addLayout(mainwindow_lowerhalf_layout)