from PyQt6.QtWidgets import *
from golfgui import *
import csv


def get_to_par(score, course_par):
    """
    Function that returns the amount of strokes the person is away from par
    :param score:
    :param course_par:
    :return: Number
    """
    num = int(score - course_par)
    if num < 0:
        return num
    if num > 0:
        return f'+{num}'
    if num == 0:
        return num


class Logic(QMainWindow, Ui_Dialog):
    """
    Class that holds all logic for the GUI
    """
    HANDICAP_INDEX = "N/A"
    ROW_HISTORY: int = 0

    def __init__(self):
        """
        Function that initializes the starting values and button functionalities
        """
        super().__init__()
        self.setupUi(self)

#       Showing Buttons
        self.button_home.show()
        self.button_post_score.show()
        self.button_stats.show()
#       Handicap Initiation
        self.get_handicap()
#       Hiding Error Messages
        self.label_name_error.hide()
        self.label_numeric_error.hide()
#       Screens/Updates
        self.button_home.clicked.connect(lambda: self.home_page())
        self.button_post_score.clicked.connect(lambda: self.post_page())
        self.button_stats.clicked.connect(lambda: self.stats_page())
        self.button_stats.clicked.connect(lambda: self.stats_data())
        self.button_stats.clicked.connect(lambda: self.get_score_stats())
        self.button_delete_history.clicked.connect(lambda: self.delete_page())
#       Posting Scores
        self.button_post.clicked.connect(lambda: self.post_score())
#       Clear Button
        self.button_clear.clicked.connect(lambda: self.clear())
#       History Delete Buttons
        self.button_delete_yes.clicked.connect(lambda: self.delete_yes())
        self.button_delete_no.clicked.connect(lambda: self.home_page())

    def delete_page(self):
        """
        Changes the screen to the delete page
        """
        self.button_home.hide()
        self.button_post_score.hide()
        self.button_stats.hide()
        self.stacked_widget.setCurrentIndex(3)

    def home_page(self):
        """
        Changes the screen to home page
        """
        self.button_home.show()
        self.button_post_score.show()
        self.button_stats.show()
        self.get_handicap()
        self.stacked_widget.setCurrentIndex(0)

    def post_page(self):
        """
        Changes screen to post page
        """
        self.get_handicap()
        self.stacked_widget.setCurrentIndex(1)

    def stats_page(self):
        """
        Changes screen to stats page
        """
        self.get_handicap()
        self.stacked_widget.setCurrentIndex(2)

    def stats_data(self):
        """
        Transfers info from a csv file to the table on the stats page
        """
        rows: int = 0
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
            self.ROW_HISTORY = rows

    def delete_yes(self):
        """
        Function that deletes all info on the csv file and deletes history on the gui's stats table
        """
        with open('round_history.csv', 'w', newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(["Name", "Score", "Course Par", "To Par", "Handicap"])
        for num in range(0, self.ROW_HISTORY):
            self.table_stats.removeRow(0)
        self.home_page()

    def post_score(self):
        """
        Function that writes user input onto a csv file and handles exceptions
        """
        self.label_numeric_error.hide()
        self.label_name_error.hide()
        with open('round_history.csv', 'a', newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            name: str = str(self.line_edit_course_name.text()).strip()
            val: bool = self.check_name(name)
            if val:
                return
            score: int = int(self.get_score())
            try:
                if int(self.line_edit_front.text()) < 0 or int(self.line_edit_back.text()) < 0:
                    raise ValueError
                course_par = int(self.line_edit_front.text()) + int(self.line_edit_back.text())
            except ValueError:
                self.label_numeric_error.show()
                return
            to_par = get_to_par(score, course_par)
            handicap = self.HANDICAP_INDEX
            csv_writer.writerow([name, score, course_par, to_par, handicap])
            self.label_numeric_error.hide()

            self.label_total_score.setText(f'TOTAL: {str(score)}')
        self.get_handicap()

    def check_name(self, name) -> bool:
        """
        function that checks if name is valid then returns True or False
        :param name:
        :return: bool
        """
        if name == "":
            self.label_name_error.show()
            return True
        else:
            self.label_name_error.hide()
            return False

    def get_score(self) -> int:
        """
        Function that adds all hole scores and returns total score as an int
        :return: Integer
        """
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
        """
        Function that updates the handicap
        """
        to_par_list = []
        with open('round_history.csv', 'r', newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                to_par_list.append(int(line[3]))
            try:
                temp_num: float = sum(to_par_list) / len(to_par_list)
            except ZeroDivisionError:
                pass
            if len(to_par_list) > 1:
                if temp_num < 0:
                    self.HANDICAP_INDEX = f'+{temp_num * (-1):.1f}'
                if temp_num > 0:
                    self.HANDICAP_INDEX = f'{temp_num:.1f}'
                if temp_num == 0:
                    self.HANDICAP_INDEX = f'{int(temp_num)}'
            else:
                self.HANDICAP_INDEX = 'N/A'
            self.label_handicap.setText(self.HANDICAP_INDEX)

    def get_score_stats(self):
        """
        Function that updates the scoring stats on the stats page
        """
        score_list: list[int] = []
        with open('round_history.csv', 'r', newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                score_list.append(int(line[1]))
            try:
                max_score = int(max(score_list))
                min_score = int(min(score_list))
                num_score = int(len(score_list))
                average_score = f'{sum(score_list) / len(score_list):.1f}'
            except ValueError:
                max_score = 'N/A'
                min_score = 'N/A'
                num_score = 'N/A'
                average_score = "N/A"
            self.label_high_score.setText(f'High: {max_score}')
            self.label_low_score.setText(f'Low: {min_score}')
            self.label_num_scores.setText(f'Num of Scores: {num_score}')
            self.label_average_score.setText(f'Average: {average_score}')

    def clear(self):
        """
        Function that sets everything on the post page back to its default value
        """
        self.num_hole_1.setValue(0)
        self.num_hole_2.setValue(0)
        self.num_hole_3.setValue(0)
        self.num_hole_4.setValue(0)
        self.num_hole_5.setValue(0)
        self.num_hole_6.setValue(0)
        self.num_hole_7.setValue(0)
        self.num_hole_8.setValue(0)
        self.num_hole_9.setValue(0)
        self.num_hole_10.setValue(0)
        self.num_hole_11.setValue(0)
        self.num_hole_12.setValue(0)
        self.num_hole_13.setValue(0)
        self.num_hole_14.setValue(0)
        self.num_hole_15.setValue(0)
        self.num_hole_16.setValue(0)
        self.num_hole_17.setValue(0)
        self.num_hole_18.setValue(0)
        self.line_edit_front.setText("")
        self.line_edit_back.setText("")
        self.line_edit_course_name.setText("")
        self.label_total_score.setText("TOTAL: N/A")
