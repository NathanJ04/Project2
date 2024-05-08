from PyQt6.QtWidgets import *
from golfgui import *

class Logic(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_home.clicked.connect(lambda: self.home_page())
        self.button_post_score.clicked.connect(lambda: self.post_page())
        self.button_stats.clicked.connect(lambda: self.stats_page())

    def home_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def post_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def stats_page(self):
        self.stacked_widget.setCurrentIndex(2)
