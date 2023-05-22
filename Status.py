from PySide6.QtWidgets import QListWidget
import ui_main as uim


class RunningEnv:
    def __init__(self):
        self.detectedList = uim.ui.detected_list
        # self.detectedList = QListWidget()
        self.detectedList.addItems(["A", "B", "C"])
        self.activated = False
        self.show_cv_window = False
        self.webcam = None
        self.model_info = {
            "name": None,
            "stride": None
        }

