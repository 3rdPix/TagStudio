"""
Fluent TagStudio UI driver
-------------------
Depends on external package: https://github.com/zhiyiYo/PyQt-Fluent-Widgets/.
This was developed with PyQt6. Porting to PySide6 might need some time.
"""

##########################################
##         Preserving imports           ##
##########################################

# Some of these libraries are not needed for sure
# I'll keep them just in case an import-triggered
# setting is needed

import ctypes
import logging
import math
import os
import sys
import time
import typing
import webbrowser
from datetime import datetime as dt
from pathlib import Path
from queue import Queue
from typing import Optional
from PIL import Image
from humanfriendly import format_timespan

from src.core.enums import SettingItems, SearchMode
from src.core.library import ItemType
from src.core.ts_core import TagStudioCore
from src.core.constants import (
    COLLAGE_FOLDER_NAME,
    BACKUP_FOLDER_NAME,
    TS_FOLDER_NAME,
    VERSION_BRANCH,
    VERSION,
)
from src.core.utils.web import strip_web_protocol

# SIGQUIT is not defined on Windows
if sys.platform == "win32":
    from signal import signal, SIGINT, SIGTERM

    SIGQUIT = SIGTERM
else:
    from signal import signal, SIGINT, SIGTERM, SIGQUIT

ERROR = f"[ERROR]"
WARNING = f"[WARNING]"
INFO = f"[INFO]"

logging.basicConfig(format="%(message)s", level=logging.INFO)

##########################################
##            Actual module             ##
##########################################

# External
from argparse import Namespace
from collections import defaultdict
from PyQt6.QtCore import QSettings
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from qfluentwidgets import RoundMenu
from PyQt6.QtCore import QTimer
from os.path import abspath
from os.path import dirname

# TagStudio


# manually set a workingdir for QtFl
qtfl_dir = abspath(dirname(__file__))
if qtfl_dir not in sys.path:
    sys.path.insert(0, qtfl_dir)

# QtFl
from app import TagStudioApp



class QtFlDriver:
    """
    Main driver for user interface
    """

    def __init__(self, core: TagStudioCore, args: Namespace) -> None:
        self.init_qt()

    def init_qt(self) -> None:
        self.app = TagStudioApp([])

    def start(self) -> None:
        self.app.exec()