from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
import sys


class TabMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabMaster")  # Nazwa programu
        self.setGeometry(100, 100, 900, 600)  # Pozycja x,y + szerokość i wysokość

        # --- Ustawienie ikony okna ---
        self.setWindowIcon(QIcon("assets/logo.png"))

        # --- Główny widget centralny ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouty główne
        main_layout = QHBoxLayout(central_widget)  # Główny poziomy układ

        # --- Lewy panel z przyciskami ---
        left_menu = QVBoxLayout()
        main_layout.addLayout(left_menu)

        # --- Tworzenie przycisków P1-P3 ---
        for i in range(1, 4):
            btn = QPushButton(f"P{i}")
            btn.setFixedWidth(120)  # szerokość lewego panelu
            btn.clicked.connect(lambda checked, n=i: self.show_tab(n))
            left_menu.addWidget(btn)
            left_menu.addSpacing(50)  # odstęp po każdym przycisku
            left_menu.setContentsMargins(10, 20, 10, 20)  # left, top, right, bottom

        # Rozciągnięcie przycisków do góry
        left_menu.addStretch()

        # --- Centralna treść (Label) ---
        self.content_label = QLabel("Witaj w TabMaster!")
        self.content_label.setAlignment(Qt.AlignHCenter)
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
                text-align: center;
                font-size: 18px;
            }
        """)

        def show_tab(self, tab_number):
            self.centralWidget().layout().itemAt(0).widget().setText(
                f"Wybrano zakładkę P{tab_number}"
            )

    def show_tab(self, tab_number):
        self.content_label.setText(f"Aktualnie wybrano zakładkę P{tab_number}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabMaster()
    window.show()
    sys.exit(app.exec())
