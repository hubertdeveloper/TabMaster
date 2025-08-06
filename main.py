from PySide6.QtWidgets import QApplication
import sys
from modules.main_window import TabMaster

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabMaster()
    window.show()
    sys.exit(app.exec())