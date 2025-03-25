import sys
from PyQt5.QtWidgets import QApplication, QMainWindow # type: ignore
from ui.rsa_ui import Ui_MainWindow # type: ignore


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
