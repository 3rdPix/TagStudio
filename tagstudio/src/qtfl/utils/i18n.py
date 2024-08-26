"""
App internationalization
------------------------
Module that handles the loading of text in different languages.
"""
from config import QtFlGuiPaths as pt
from babel.support import Translations
from config.gui_settings import LOCALE

# Load the translations
locale_path = pt.Resx.LOCALES
lang = Translations.load(locale_path, locales=[LOCALE])
lang.install()
_ = lang.gettext