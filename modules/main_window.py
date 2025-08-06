from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QSizePolicy
)
import sys
import os
from modules.tab_stan_tonera import TabStanTonera

class TabMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabMaster")
        self.setGeometry(100, 100, 900, 600)

        base_path = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.normpath(os.path.join(base_path, "..", "assets", "logo.png"))
        self.setWindowIcon(QIcon(logo_path))

        # Centralny widget i layout poziomy
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Lewy panel - layout pionowy z przyciskami
        left_menu = QVBoxLayout()
        left_menu.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # przyciski u góry i do lewej

        left_menu_widget = QWidget()
        left_menu_widget.setLayout(left_menu)
        left_menu_widget.setMinimumWidth(180)  # minimalna szerokość panelu
        main_layout.addWidget(left_menu_widget)

        # Logo jako przycisk (HOME)
        logo_btn = QPushButton()
        logo_btn.setIcon(QIcon(logo_path))
        logo_btn.setIconSize(QSize(64, 64))
        logo_btn.setFixedSize(80, 80)
        logo_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                padding: 0px;
                margin: 0px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 30);
            }
        """)
        logo_btn.clicked.connect(self.show_home)
        left_menu.addWidget(logo_btn)
        left_menu.addSpacing(20)

        # Przyciski na panelu
        przyciski = [
            ("Strona główna", 0),
            ("Stan tonerów", 2),
            ("Inny widok", 3)
        ]

        for nazwa, nr in przyciski:
            btn = QPushButton(nazwa)
            btn.setFixedHeight(40)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # przycisk rozciąga się na szerokość
            btn.clicked.connect(lambda checked, n=nr: self.show_tab(n))
            left_menu.addWidget(btn)
            left_menu.addSpacing(15)

        left_menu.addStretch()

        # Centralna zawartość
        self.current_widget = None
        self.main_layout = main_layout

        # Style aplikacji
        self.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #4a90e2, stop:1 #357ABD
                );
                color: white;
                border: 2px solid #2b5797;
                border-radius: 10px;
                padding: 8px 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #5aa0f2, stop:1 #4689d0
                );
            }
            QPushButton:pressed {
                background-color: #2b5797;
                padding-left: 10px;
                padding-top: 10px;
            }
        """)

        # Pokaż startową stronę
        self.show_home()

    def show_home(self):
        self.show_tab(0)

    def show_tab(self, tab_number):
        if self.current_widget:
            self.main_layout.removeWidget(self.current_widget)
            self.current_widget.setParent(None)

        if tab_number == 2:
            self.current_widget = TabStanTonera()
        else:
            label = QLabel(f"Aktualnie wybrano zakładkę P{tab_number}")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 24px; padding: 20px;")
            self.current_widget = label

        self.main_layout.addWidget(self.current_widget, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabMaster()
    window.show()
    sys.exit(app.exec())
