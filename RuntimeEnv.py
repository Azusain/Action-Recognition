import ui_main as uim


class RunningEnv:
    def __init__(self):
        self.detectedList = uim.ui.detected_list
        # self.detectedList = QListWidget()
        self.detectedList.addItems(["No detected objects"])
        self.activated = False
        self.show_cv_window = False
        self.webcam = None
        self.conf_file_path = "./configurations/startup.cfg"
        self.conf_list = {}
        self.parse_conf_file()

    def parse_conf_file(self):
        with open(self.conf_file_path, 'r') as f:
            while True:
                k_raw = f.readline()
                if k_raw == "":
                    break
                k = k_raw.replace(":", "")
                v = f.readline()
                self.conf_list[k.replace("\n", "")] = v.replace("\n", "")
        print(self.conf_list)

    def update_interface(self):
        uim.ui.src_path = self.conf_list['source']
        uim.ui.src_path = self.conf_list['output']
