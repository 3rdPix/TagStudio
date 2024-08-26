from config import QtFlGuiPaths as pt
from json import load
import logging


try:
    with open(pt.GUI.PREFERENCES, 'r') as configs_file:
        gui_settings: dict = load(configs_file)
except FileNotFoundError:
    logging.error("Couldn't load gui settings")
LOCALE = gui_settings.get('locale')