from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
import sys


class TabMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabMaster")
        self.setGeometry(100, 100, 900, 600)

        # --- Ustawienie ikony okna ---
        self.setWindowIcon(QIcon("assets/logo.png"))

        # --- Główny widget centralny ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # --- Lewy panel z przyciskami ---
        left_menu = QVBoxLayout()
        main_layout.addLayout(left_menu)

        # --- Logo jako przycisk (HOME) ---
        logo_btn = QPushButton()
        logo_pixmap = QPixmap(r"assets/logo.png")
        logo_btn.setIcon(QIcon(logo_pixmap))
        logo_btn.setIconSize(QSize(64, 64))
        logo_btn.setFixedSize(80, 80)
        logo_btn.setStyleSheet("border: none;")
        logo_btn.clicked.connect(self.show_home)
        left_menu.addWidget(logo_btn)

        # --- Tworzenie przycisków P1-P3 ---
        for i in range(1, 4):
            btn = QPushButton(f"P{i}")
            btn.setFixedWidth(120)
            btn.clicked.connect(lambda checked, n=i: self.show_tab(n))
            left_menu.addWidget(btn)
            left_menu.addSpacing(20)

        left_menu.addStretch()

        # --- Centralna treść (Label) ---
        self.content_label = QLabel()
        self.content_label.setAlignment(Qt.AlignCenter)
        self.content_label.setStyleSheet("font-size: 24px; padding: 20px;")
        main_layout.addWidget(self.content_label)

        # --- Style aplikacji ---
        self.setStyleSheet("""
            QPushButton {
                background-color: #2b5797;
                color: white;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #1a356e;
            }
            QLabel {
                font-size: 18px;
            }
        """)

        self.show_home()

    def show_home(self):
        self.content_label.setText("Ekran główny aplikacji")

    def show_tab(self, tab_number):
        self.content_label.setText(f"Aktualnie wybrano zakładkę P{tab_number}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabMaster()
    window.show()
    sys.exit(app.exec())
