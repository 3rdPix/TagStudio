# Copyright (C) 2024 Travis Abendshien (CyanVoxel).
# Licensed under the GPL-3.0 License.
# Created for TagStudio: https://github.com/CyanVoxel/TagStudio

"""TagStudio launcher."""

from src.core.ts_core import TagStudioCore
#from src.cli.ts_cli import CliDriver  # type: ignore
#from src.qt.ts_qt import QtDriver
from src.qtfl.ts_qtfl import QtFlDriver
import argparse
import traceback
from typing import Protocol

class UIDriver(Protocol):

    def __init__(self, core, args) -> None: ...
    def start() -> None: ...


def main():
    # appid = "cyanvoxel.tagstudio.9"
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    # Parse arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--open",
        dest="open",
        type=str,
        help="Path to a TagStudio Library folder to open on start.",
    )
    parser.add_argument(
        "-o",
        dest="open",
        type=str,
        help="Path to a TagStudio Library folder to open on start.",
    )
    parser.add_argument(
        "-c",
        "--config-file",
        dest="config_file",
        type=str,
        help="Path to a TagStudio .ini or .plist config file to use.",
    )

    # parser.add_argument('--browse', dest='browse', action='store_true',
    #                     help='Jumps to entry browsing on startup.')
    # parser.add_argument('--external_preview', dest='external_preview', action='store_true',
    #                     help='Outputs current preview thumbnail to a live-updating file.')
    parser.add_argument(
        "--debug",
        dest="debug",
        action="store_true",
        help="Reveals additional internal data useful for debugging.",
    )
    parser.add_argument(
        "--ui",
        dest="ui",
        type=str,
        help="User interface option for TagStudio. Options: qt, cli, qtfl (Default: qt)",
    )
    parser.add_argument(
        "--ci",
        action=argparse.BooleanOptionalAction,
        help="Exit the application after checking it starts without any problem. Meant for CI check.",
    )
    args = parser.parse_args()

    core = TagStudioCore()  # The TagStudio Core instance. UI agnostic.
    
    # Driver selection based on parameters.
    # will default to Qt if none is given
    driver_instance: UIDriver
    ui_name: str
    match args.ui:
        
        case "cli":
            driver_instance = CliDriver(core, args)
            ui_name = "CLI"

        case "qtfl":
            driver_instance = QtFlDriver(core, args)
            ui_name = "QtFl"

        case _:
            driver_instance = QtDriver(core, args)
            ui_name = "Qt"

    # Run the chosen frontend driver.
    try:
        driver_instance.start()
    except Exception:
        traceback.print_exc()
        print(f"\nTagStudio Frontend ({ui_name}) Crashed! Press Enter to Continue...")
        input()


if __name__ == "__main__":
    main()
