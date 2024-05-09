# Form implementation generated from reading ui file 'golfgui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 450)
        Dialog.setMinimumSize(QtCore.QSize(700, 450))
        Dialog.setMaximumSize(QtCore.QSize(700, 450))
        self.stacked_widget = QtWidgets.QStackedWidget(parent=Dialog)
        self.stacked_widget.setGeometry(QtCore.QRect(0, 0, 700, 390))
        self.stacked_widget.setMinimumSize(QtCore.QSize(700, 390))
        self.stacked_widget.setMaximumSize(QtCore.QSize(700, 390))
        self.stacked_widget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.stacked_widget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.stacked_widget.setLineWidth(0)
        self.stacked_widget.setObjectName("stacked_widget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setMinimumSize(QtCore.QSize(700, 390))
        self.page_home.setMaximumSize(QtCore.QSize(700, 390))
        self.page_home.setObjectName("page_home")
        self.label_title = QtWidgets.QLabel(parent=self.page_home)
        self.label_title.setGeometry(QtCore.QRect(30, 10, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_index = QtWidgets.QLabel(parent=self.page_home)
        self.label_index.setGeometry(QtCore.QRect(230, 250, 241, 41))
        self.label_index.setObjectName("label_index")
        self.label_handicap = QtWidgets.QLabel(parent=self.page_home)
        self.label_handicap.setGeometry(QtCore.QRect(180, 140, 341, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_handicap.setFont(font)
        self.label_handicap.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_handicap.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_handicap.setObjectName("label_handicap")
        self.stacked_widget.addWidget(self.page_home)
        self.page_post_score = QtWidgets.QWidget()
        self.page_post_score.setMinimumSize(QtCore.QSize(700, 390))
        self.page_post_score.setMaximumSize(QtCore.QSize(700, 390))
        self.page_post_score.setObjectName("page_post_score")
        self.label_title_2 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_title_2.setGeometry(QtCore.QRect(30, 0, 641, 51))
        self.label_title_2.setObjectName("label_title_2")
        self.label_course_name = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_course_name.setGeometry(QtCore.QRect(30, 60, 111, 21))
        self.label_course_name.setObjectName("label_course_name")
        self.line_edit_course_name = QtWidgets.QLineEdit(parent=self.page_post_score)
        self.line_edit_course_name.setGeometry(QtCore.QRect(140, 60, 221, 21))
        self.line_edit_course_name.setText("")
        self.line_edit_course_name.setObjectName("line_edit_course_name")
        self.label_par = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_par.setGeometry(QtCore.QRect(30, 110, 111, 21))
        self.label_par.setObjectName("label_par")
        self.line_edit_front = QtWidgets.QLineEdit(parent=self.page_post_score)
        self.line_edit_front.setGeometry(QtCore.QRect(140, 120, 51, 21))
        self.line_edit_front.setObjectName("line_edit_front")
        self.label_front = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_front.setGeometry(QtCore.QRect(140, 100, 51, 21))
        self.label_front.setObjectName("label_front")
        self.label_back = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_back.setGeometry(QtCore.QRect(220, 100, 51, 21))
        self.label_back.setObjectName("label_back")
        self.line_edit_back = QtWidgets.QLineEdit(parent=self.page_post_score)
        self.line_edit_back.setGeometry(QtCore.QRect(220, 120, 51, 21))
        self.line_edit_back.setObjectName("line_edit_back")
        self.label_enter_scores = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_enter_scores.setGeometry(QtCore.QRect(260, 160, 181, 21))
        self.label_enter_scores.setObjectName("label_enter_scores")
        self.num_hole_1 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_1.setGeometry(QtCore.QRect(30, 220, 61, 31))
        self.num_hole_1.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_1.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_1.setWrapping(True)
        self.num_hole_1.setFrame(True)
        self.num_hole_1.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_1.setMaximum(20)
        self.num_hole_1.setObjectName("num_hole_1")
        self.num_hole_2 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_2.setGeometry(QtCore.QRect(90, 220, 61, 31))
        self.num_hole_2.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_2.setWrapping(True)
        self.num_hole_2.setFrame(True)
        self.num_hole_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_2.setMaximum(20)
        self.num_hole_2.setObjectName("num_hole_2")
        self.num_hole_3 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_3.setGeometry(QtCore.QRect(150, 220, 61, 31))
        self.num_hole_3.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_3.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_3.setWrapping(True)
        self.num_hole_3.setFrame(True)
        self.num_hole_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_3.setMaximum(20)
        self.num_hole_3.setObjectName("num_hole_3")
        self.num_hole_4 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_4.setGeometry(QtCore.QRect(210, 220, 61, 31))
        self.num_hole_4.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_4.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_4.setWrapping(True)
        self.num_hole_4.setFrame(True)
        self.num_hole_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_4.setMaximum(20)
        self.num_hole_4.setObjectName("num_hole_4")
        self.num_hole_5 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_5.setGeometry(QtCore.QRect(270, 220, 61, 31))
        self.num_hole_5.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_5.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_5.setWrapping(True)
        self.num_hole_5.setFrame(True)
        self.num_hole_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_5.setMaximum(20)
        self.num_hole_5.setObjectName("num_hole_5")
        self.num_hole_6 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_6.setGeometry(QtCore.QRect(330, 220, 61, 31))
        self.num_hole_6.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_6.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_6.setWrapping(True)
        self.num_hole_6.setFrame(True)
        self.num_hole_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_6.setMaximum(20)
        self.num_hole_6.setObjectName("num_hole_6")
        self.num_hole_7 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_7.setGeometry(QtCore.QRect(390, 220, 61, 31))
        self.num_hole_7.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_7.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_7.setWrapping(True)
        self.num_hole_7.setFrame(True)
        self.num_hole_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_7.setMaximum(20)
        self.num_hole_7.setObjectName("num_hole_7")
        self.num_hole_8 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_8.setGeometry(QtCore.QRect(450, 220, 61, 31))
        self.num_hole_8.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_8.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_8.setWrapping(True)
        self.num_hole_8.setFrame(True)
        self.num_hole_8.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_8.setMaximum(20)
        self.num_hole_8.setObjectName("num_hole_8")
        self.num_hole_9 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_9.setGeometry(QtCore.QRect(510, 220, 61, 31))
        self.num_hole_9.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_9.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_9.setWrapping(True)
        self.num_hole_9.setFrame(True)
        self.num_hole_9.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_9.setMaximum(20)
        self.num_hole_9.setObjectName("num_hole_9")
        self.label_1 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_1.setGeometry(QtCore.QRect(30, 190, 51, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_4.setGeometry(QtCore.QRect(210, 190, 51, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_5.setGeometry(QtCore.QRect(270, 190, 51, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_6.setGeometry(QtCore.QRect(330, 190, 51, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_7.setGeometry(QtCore.QRect(390, 190, 51, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_8.setGeometry(QtCore.QRect(450, 190, 51, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_9.setGeometry(QtCore.QRect(510, 190, 51, 21))
        self.label_9.setObjectName("label_9")
        self.num_hole_14 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_14.setGeometry(QtCore.QRect(270, 290, 61, 31))
        self.num_hole_14.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_14.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_14.setWrapping(True)
        self.num_hole_14.setFrame(True)
        self.num_hole_14.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_14.setMaximum(20)
        self.num_hole_14.setObjectName("num_hole_14")
        self.num_hole_10 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_10.setGeometry(QtCore.QRect(30, 290, 61, 31))
        self.num_hole_10.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_10.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_10.setWrapping(True)
        self.num_hole_10.setFrame(True)
        self.num_hole_10.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_10.setMaximum(20)
        self.num_hole_10.setObjectName("num_hole_10")
        self.num_hole_16 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_16.setGeometry(QtCore.QRect(390, 290, 61, 31))
        self.num_hole_16.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_16.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_16.setWrapping(True)
        self.num_hole_16.setFrame(True)
        self.num_hole_16.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_16.setMaximum(20)
        self.num_hole_16.setObjectName("num_hole_16")
        self.num_hole_17 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_17.setGeometry(QtCore.QRect(450, 290, 61, 31))
        self.num_hole_17.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_17.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_17.setWrapping(True)
        self.num_hole_17.setFrame(True)
        self.num_hole_17.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_17.setMaximum(20)
        self.num_hole_17.setObjectName("num_hole_17")
        self.label_16 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_16.setGeometry(QtCore.QRect(390, 260, 51, 21))
        self.label_16.setObjectName("label_16")
        self.label_10 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_10.setGeometry(QtCore.QRect(30, 260, 51, 21))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_12.setGeometry(QtCore.QRect(150, 260, 51, 21))
        self.label_12.setObjectName("label_12")
        self.num_hole_13 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_13.setGeometry(QtCore.QRect(210, 290, 61, 31))
        self.num_hole_13.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_13.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_13.setWrapping(True)
        self.num_hole_13.setFrame(True)
        self.num_hole_13.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_13.setMaximum(20)
        self.num_hole_13.setObjectName("num_hole_13")
        self.label_18 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_18.setGeometry(QtCore.QRect(510, 260, 51, 21))
        self.label_18.setObjectName("label_18")
        self.num_hole_15 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_15.setGeometry(QtCore.QRect(330, 290, 61, 31))
        self.num_hole_15.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_15.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_15.setWrapping(True)
        self.num_hole_15.setFrame(True)
        self.num_hole_15.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_15.setMaximum(20)
        self.num_hole_15.setObjectName("num_hole_15")
        self.label_11 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_11.setGeometry(QtCore.QRect(90, 260, 51, 21))
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_15.setGeometry(QtCore.QRect(330, 260, 51, 21))
        self.label_15.setObjectName("label_15")
        self.label_14 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_14.setGeometry(QtCore.QRect(270, 260, 51, 21))
        self.label_14.setObjectName("label_14")
        self.num_hole_18 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_18.setGeometry(QtCore.QRect(510, 290, 61, 31))
        self.num_hole_18.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_18.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_18.setWrapping(True)
        self.num_hole_18.setFrame(True)
        self.num_hole_18.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_18.setMaximum(20)
        self.num_hole_18.setObjectName("num_hole_18")
        self.label_13 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_13.setGeometry(QtCore.QRect(210, 260, 51, 21))
        self.label_13.setObjectName("label_13")
        self.label_17 = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_17.setGeometry(QtCore.QRect(450, 260, 51, 21))
        self.label_17.setObjectName("label_17")
        self.num_hole_11 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_11.setGeometry(QtCore.QRect(90, 290, 61, 31))
        self.num_hole_11.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_11.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_11.setWrapping(True)
        self.num_hole_11.setFrame(True)
        self.num_hole_11.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_11.setMaximum(20)
        self.num_hole_11.setObjectName("num_hole_11")
        self.num_hole_12 = QtWidgets.QSpinBox(parent=self.page_post_score)
        self.num_hole_12.setGeometry(QtCore.QRect(150, 290, 61, 31))
        self.num_hole_12.setStyleSheet("font: 8pt \"MS Gothic\";")
        self.num_hole_12.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.num_hole_12.setWrapping(True)
        self.num_hole_12.setFrame(True)
        self.num_hole_12.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.num_hole_12.setMaximum(20)
        self.num_hole_12.setObjectName("num_hole_12")
        self.label_total_score = QtWidgets.QLabel(parent=self.page_post_score)
        self.label_total_score.setGeometry(QtCore.QRect(290, 340, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_total_score.setFont(font)
        self.label_total_score.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_total_score.setObjectName("label_total_score")
        self.button_post = QtWidgets.QPushButton(parent=self.page_post_score)
        self.button_post.setGeometry(QtCore.QRect(590, 220, 91, 51))
        self.button_post.setStyleSheet("")
        self.button_post.setObjectName("button_post")
        self.button_clear = QtWidgets.QPushButton(parent=self.page_post_score)
        self.button_clear.setGeometry(QtCore.QRect(590, 290, 91, 31))
        self.button_clear.setStyleSheet("")
        self.button_clear.setObjectName("button_clear")
        self.stacked_widget.addWidget(self.page_post_score)
        self.page_stats = QtWidgets.QWidget()
        self.page_stats.setMinimumSize(QtCore.QSize(700, 390))
        self.page_stats.setMaximumSize(QtCore.QSize(700, 390))
        self.page_stats.setObjectName("page_stats")
        self.label_title_stats = QtWidgets.QLabel(parent=self.page_stats)
        self.label_title_stats.setGeometry(QtCore.QRect(270, 0, 161, 51))
        self.label_title_stats.setObjectName("label_title_stats")
        self.label_num_scores = QtWidgets.QLabel(parent=self.page_stats)
        self.label_num_scores.setGeometry(QtCore.QRect(40, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_num_scores.setFont(font)
        self.label_num_scores.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_num_scores.setObjectName("label_num_scores")
        self.label_high_score = QtWidgets.QLabel(parent=self.page_stats)
        self.label_high_score.setGeometry(QtCore.QRect(230, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_high_score.setFont(font)
        self.label_high_score.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_high_score.setObjectName("label_high_score")
        self.label_low_score = QtWidgets.QLabel(parent=self.page_stats)
        self.label_low_score.setGeometry(QtCore.QRect(370, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_low_score.setFont(font)
        self.label_low_score.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_low_score.setObjectName("label_low_score")
        self.label_average_score = QtWidgets.QLabel(parent=self.page_stats)
        self.label_average_score.setGeometry(QtCore.QRect(510, 60, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_average_score.setFont(font)
        self.label_average_score.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_average_score.setObjectName("label_average_score")
        self.table_stats = QtWidgets.QTableWidget(parent=self.page_stats)
        self.table_stats.setGeometry(QtCore.QRect(30, 110, 640, 261))
        self.table_stats.setMinimumSize(QtCore.QSize(640, 261))
        self.table_stats.setMaximumSize(QtCore.QSize(640, 261))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        self.table_stats.setFont(font)
        self.table_stats.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.table_stats.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.table_stats.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.table_stats.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.table_stats.setLineWidth(0)
        self.table_stats.setMidLineWidth(0)
        self.table_stats.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_stats.setTabKeyNavigation(False)
        self.table_stats.setProperty("showDropIndicator", False)
        self.table_stats.setAlternatingRowColors(False)
        self.table_stats.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.table_stats.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.table_stats.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.table_stats.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.table_stats.setShowGrid(True)
        self.table_stats.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.table_stats.setWordWrap(True)
        self.table_stats.setCornerButtonEnabled(True)
        self.table_stats.setRowCount(0)
        self.table_stats.setColumnCount(5)
        self.table_stats.setObjectName("table_stats")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_stats.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_stats.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_stats.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_stats.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_stats.setHorizontalHeaderItem(4, item)
        self.table_stats.horizontalHeader().setDefaultSectionSize(120)
        self.table_stats.horizontalHeader().setMinimumSectionSize(120)
        self.table_stats.verticalHeader().setDefaultSectionSize(55)
        self.table_stats.verticalHeader().setMinimumSectionSize(55)
        self.stacked_widget.addWidget(self.page_stats)
        self.button_post_score = QtWidgets.QPushButton(parent=Dialog)
        self.button_post_score.setGeometry(QtCore.QRect(300, 400, 101, 41))
        self.button_post_score.setObjectName("button_post_score")
        self.button_stats = QtWidgets.QPushButton(parent=Dialog)
        self.button_stats.setGeometry(QtCore.QRect(430, 400, 101, 41))
        self.button_stats.setObjectName("button_stats")
        self.button_home = QtWidgets.QPushButton(parent=Dialog)
        self.button_home.setGeometry(QtCore.QRect(170, 400, 101, 41))
        self.button_home.setObjectName("button_home")

        self.retranslateUi(Dialog)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "Golf Handicap Calculator"))
        self.label_index.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Handicap Index</span></p></body></html>"))
        self.label_handicap.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">N/A</p></body></html>"))
        self.label_title_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">POST A SCORE</span></p></body></html>"))
        self.label_course_name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Course Name:</span></p></body></html>"))
        self.label_par.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Enter Par:</span></p></body></html>"))
        self.label_front.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Front</span></p></body></html>"))
        self.label_back.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Back</span></p></body></html>"))
        self.label_enter_scores.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ENTER SCORES</span></p></body></html>"))
        self.label_1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">2</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">5</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">6</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">7</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">8</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">9</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">16</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">10</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">12</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">18</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">11</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">15</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">14</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">13</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">17</span></p></body></html>"))
        self.label_total_score.setText(_translate("Dialog", "TOTAL: N/A"))
        self.button_post.setText(_translate("Dialog", "POST"))
        self.button_clear.setText(_translate("Dialog", "CLEAR"))
        self.label_title_stats.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">STATS</span></p></body></html>"))
        self.label_num_scores.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Num of Scores: N/A</span></p></body></html>"))
        self.label_high_score.setText(_translate("Dialog", "<html><head/><body><p>High: N/A</p></body></html>"))
        self.label_low_score.setText(_translate("Dialog", "<html><head/><body><p>Low: N/A</p></body></html>"))
        self.label_average_score.setText(_translate("Dialog", "<html><head/><body><p>Average: N/A</p></body></html>"))
        self.table_stats.setSortingEnabled(False)
        item = self.table_stats.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Course Name"))
        item = self.table_stats.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Score"))
        item = self.table_stats.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Course Par"))
        item = self.table_stats.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "To Par"))
        item = self.table_stats.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Handicap"))
        self.button_post_score.setText(_translate("Dialog", "POST SCORE"))
        self.button_stats.setText(_translate("Dialog", "STATS"))
        self.button_home.setText(_translate("Dialog", "HOME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
