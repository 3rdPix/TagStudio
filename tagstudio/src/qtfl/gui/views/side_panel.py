from PyQt6.QtWidgets import QFrame
from qfluentwidgets import ComboBox
from qfluentwidgets import ImageLabel
from qfluentwidgets import DisplayLabel
from PyQt6.QtWidgets import QWidget


class SidePanel(QWidget):
    """
    Container for preview image, metadatada editor and other settings
    for the working area of the main window    
    """

    def _load_ui(self) -> None:
        logic_criteria_selector = ComboBox()
        thumbnail_size_selector = ComboBox()
        preview_label = ImageLabel()
        name_label = DisplayLabel()
        information_label = DisplayLabel()
        metadata_editor = QFrame()