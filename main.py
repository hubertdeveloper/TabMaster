from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
import sys


class TabMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabMaster")  # Nazwa programu
        self.setGeometry(100, 100, 900, 600)  # Pozycja x,y + szerokość i wysokość

        # --- Główny widget centralny ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouty główne
        main_layout = QHBoxLayout(central_widget)  # Główny poziomy układ

        # --- Lewy panel z przyciskami ---
        side_panel = QVBoxLayout()
        self.buttons = []
        for i in range(1, 4):  # Na start 3 przyciski
            btn = QPushButton(f"P{i}")
            btn.clicked.connect(lambda _, x=i: self.show_tab(x))
            self.buttons.append(btn)
            side_panel.addWidget(btn)

        # --- Prawa część: treść ---
        self.content_label = QLabel("Wybierz przycisk z lewej strony")
        self.content_label.setStyleSheet("font-size: 18px; margin: 20px;")

        # Dodanie layoutów do głównego
        main_layout.addLayout(side_panel, 1)  # lewy panel wąski
        main_layout.addWidget(self.content_label, 4)  # prawa treść szeroka

    def show_tab(self, index):
        self.content_label.setText(f"Zawartość zakładki P{index}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabMaster()
    window.show()
    sys.exit(app.exec())
