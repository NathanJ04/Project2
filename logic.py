from PyQt6.QtWidgets import *
from golfgui import *
import csv


class Logic(QMainWindow, Ui_Dialog):
    row_count: int = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_home.clicked.connect(lambda: self.home_page())
        self.button_stats.clicked.connect(lambda: self.stats_data())
        self.button_post_score.clicked.connect(lambda: self.post_page())
        self.button_stats.clicked.connect(lambda: self.stats_page())

    def home_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def post_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def stats_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def stats_data(self):
        rows = 0
        with open('roundhistory.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                self.table_stats.removeRow(rows)
                self.table_stats.insertRow(rows)
                item = QtWidgets.QTableWidgetItem(line[0])
                self.table_stats.setItem(rows, 0, item)
                item = QtWidgets.QTableWidgetItem(line[1])
                self.table_stats.setItem(rows, 1, item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter))
                self.table_stats.setItem(rows, 1, item)
                item = QtWidgets.QTableWidgetItem(line[2])
                self.table_stats.setItem(rows, 2, item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter))
                self.table_stats.setItem(rows, 2, item)
                item = QtWidgets.QTableWidgetItem(line[3])
                self.table_stats.setItem(rows, 3, item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter))
                self.table_stats.setItem(rows, 3, item)
                item = QtWidgets.QTableWidgetItem(line[4])
                self.table_stats.setItem(rows, 4, item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter))
                self.table_stats.setItem(rows, 4, item)
                rows += 1



    def add_info(self, csv_reader):
        for line in csv_reader:
            for value in line:
                print(value)

