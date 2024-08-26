"""
GUI Paths
---------
Handled from here to every module
"""
from dataclasses import dataclass
from os.path import join
from os.path import abspath
from os.path import dirname


# start from tagstudio/
base_directory: str = abspath(join(dirname(__file__), '..', '..', '..'))
def build_path(*args) -> str:
    return join(base_directory, *args)


class QtFlGuiPaths:
    """
    Main class containing paths to project files
    """

    @dataclass
    class Resx:
        ICON_ICO: str = build_path('resources', 'icon.ico')
        ICON_PNG: str = build_path('resources', 'icon.png')
        LOCALES: str = build_path('resources', 'qtfl', 'locale')
    
    @dataclass
    class Qss:
        MAIN_WINDOW: str = build_path('resources', 'qtfl', 'qss', 'main_window.qss')

    @dataclass
    class GUI:
        PREFERENCES: str = build_path('src', 'qtfl', 'config', 'preferences.json')
