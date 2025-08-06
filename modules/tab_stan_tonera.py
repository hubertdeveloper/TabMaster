from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, \
    QHeaderView, QMessageBox
import pandas as pd
import os

class TabStanTonera(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.btn_wczytaj = QPushButton("Wybierz plik Excel")
        self.layout.addWidget(self.btn_wczytaj)
        self.btn_wczytaj.clicked.connect(self.otworz_dialog)

        self.df = None
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Wczytaj domyślny plik przy starcie — poprawnie ustawiona ścieżka
        sciezka = os.path.join(os.path.dirname(__file__), "../data/przykład_toner.xlsx")
        sciezka = os.path.abspath(sciezka)

        if os.path.exists(sciezka):
            try:
                self.wczytaj_excel(sciezka)
            except Exception as e:
                QMessageBox.warning(self, "Uwaga", f"Nie udało się załadować domyślnego pliku:\n{e}")
        else:
            QMessageBox.information(self, "Informacja", f"Plik domyślny nie istnieje:\n{sciezka}")

    def otworz_dialog(self):
        path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik Excel", "data/", "Excel Files (*.xlsx)")
        if path:
            self.wczytaj_excel(path)

    def wczytaj_excel(self, path):
        print("Wybrano:", path)
        try:
            df = pd.read_excel(path, engine="openpyxl")
            print("Wczytano dane:")
            print(df.head())

            # Filtrowanie — jeśli masz kolumny C, M, Y, K
            df_cmyk = df[["Nazwa tonera", "C", "M", "Y", "K", "Pasujące drukarki"]]
            self.df = df_cmyk  # zapisujemy do obiektu

            # Sprawdź, czy któryś z tonerów jest poniżej progu
            prog = 2

            alerty = []
            for _, row in df_cmyk.iterrows():
                nazwa = row["Nazwa tonera"]
                for kolor in ["C", "M", "Y", "K"]:
                    if pd.to_numeric(row[kolor], errors='coerce') < prog:
                        alerty.append(f"{nazwa} [{kolor}] - tylko {row[kolor]} szt.")

            # Jeśli są braki — wyświetl ostrzeżenie
            if alerty:
                QMessageBox.warning(self, "Niski stan tonera", "Wykryto niski poziom:\n\n" + "\n".join(alerty))

            print("Dane po filtrze CMYK:")
            print(self.df)
            df = self.df
            self.table.setColumnCount(len(df.columns))
            self.table.setRowCount(len(df.index))
            self.table.setHorizontalHeaderLabels(df.columns.tolist())
            for i, row in df.iterrows():
                for j, val in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(str(val)))

            self.table.horizontalHeader().setStretchLastSection(True)
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        except Exception as e:
            QMessageBox.critical(self, "Błąd", str(e))