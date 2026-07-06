import sys
import json
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QFileDialog,
    QTableWidget, QTableWidgetItem,
    QHeaderView, QCheckBox
)


class Schedule(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("백지 일과표")
        self.resize(700, 700)

        layout = QVBoxLayout()

        self.table = QTableWidget(24, 3)
        self.table.setHorizontalHeaderLabels(["시간", "할 일", "완료"])

        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        for i in range(24):
            self.table.setItem(i, 0, QTableWidgetItem(f"{i:02d}:00"))

            checkbox = QCheckBox()
            self.table.setCellWidget(i, 2, checkbox)

        layout.addWidget(self.table)

        save_btn = QPushButton("저장")
        load_btn = QPushButton("불러오기")

        save_btn.clicked.connect(self.save_data)
        load_btn.clicked.connect(self.load_data)

        layout.addWidget(save_btn)
        layout.addWidget(load_btn)

        self.setLayout(layout)

    def save_data(self):

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "저장",
            "",
            "JSON (*.json)"
        )

        if not filename:
            return

        data = []

        for row in range(24):

            work = ""

            if self.table.item(row, 1):
                work = self.table.item(row, 1).text()

            checked = self.table.cellWidget(row, 2).isChecked()

            data.append({
                "time": f"{row:02d}:00",
                "work": work,
                "checked": checked
            })

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "불러오기",
            "",
            "JSON (*.json)"
        )

        if not filename:
            return

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        for row, item in enumerate(data):

            self.table.setItem(row, 1, QTableWidgetItem(item["work"]))

            self.table.cellWidget(row, 2).setChecked(item["checked"])


app = QApplication(sys.argv)

window = Schedule()
window.show()

app.exec()