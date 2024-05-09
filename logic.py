from PyQt6.QtWidgets import *
from golfgui import *
import csv


def get_to_par(score, course_par):
    num = int(score - course_par)
    if num < 0:
        return num
    if num > 0:
        return f'+{num}'
    if num == 0:
        return num


class Logic(QMainWindow, Ui_Dialog):
    HANDICAP_INDEX = "N/A"

    def __init__(self):
        super().__init__()
        self.setupUi(self)

#       Handicap Initiation
        self.get_handicap()
        self.label_handicap.setText(self.HANDICAP_INDEX)
#       Screens/Updates
        self.button_home.clicked.connect(lambda: self.home_page())
        self.button_post_score.clicked.connect(lambda: self.post_page())
        self.button_stats.clicked.connect(lambda: self.stats_page())
        self.button_stats.clicked.connect(lambda: self.stats_data())
#       Posting Scores
        self.button_post.clicked.connect(lambda: self.post_score())

    def home_page(self):
        self.label_handicap.setText(self.HANDICAP_INDEX)
        self.stacked_widget.setCurrentIndex(0)

    def post_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def stats_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def stats_data(self):
        rows = 0
        with open('round_history.csv', 'r', newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
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

    def post_score(self):
        with open('round_history.csv', 'a', newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            name = str(self.line_edit_course_name.text())
            score = int(self.get_score())
            course_par = int(self.line_edit_front.text()) + int(self.line_edit_back.text())
            to_par = get_to_par(score, course_par)
            handicap = self.HANDICAP_INDEX
            csv_writer.writerow([name, score, course_par, to_par, handicap])

            self.label_total_score.setText(str(score))
            self.get_handicap()


    def get_score(self):
        h1 = int(self.num_hole_1.value())
        h2 = int(self.num_hole_2.value())
        h3 = int(self.num_hole_3.value())
        h4 = int(self.num_hole_4.value())
        h5 = int(self.num_hole_5.value())
        h6 = int(self.num_hole_6.value())
        h7 = int(self.num_hole_7.value())
        h8 = int(self.num_hole_8.value())
        h9 = int(self.num_hole_9.value())
        h10 = int(self.num_hole_10.value())
        h11 = int(self.num_hole_11.value())
        h12 = int(self.num_hole_12.value())
        h13 = int(self.num_hole_13.value())
        h14 = int(self.num_hole_14.value())
        h15 = int(self.num_hole_15.value())
        h16 = int(self.num_hole_16.value())
        h17 = int(self.num_hole_17.value())
        h18 = int(self.num_hole_18.value())
        return int(h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10
                   + h11 + h12 + h13 + h14 + h15 + h16 + h17 + h18)

    def get_handicap(self):
        to_par_list = []
        with open('round_history.csv', 'r', newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                to_par_list.append(int(line[3]))
            try:
                temp_num = sum(to_par_list) / len(to_par_list)
            except ZeroDivisionError:
                pass
            if len(to_par_list) > 0:
                if temp_num < 0:
                    self.HANDICAP_INDEX = f'+{temp_num * (-1):.1f}'
                if temp_num > 0:
                    self.HANDICAP_INDEX = f'{temp_num:.1f}'
                if temp_num == 0:
                    self.HANDICAP_INDEX = f'{int(temp_num)}'
            else:
                self.HANDICAP_INDEX = 'N/A'
