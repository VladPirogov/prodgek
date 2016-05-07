#!/usr/bin/python
# -*- coding: utf-8 -*-
# quitbutton.py

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.ini()
        self.one()
        self.two()
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('main')
        self.show()
    def one(self):

        onebtn = QPushButton('Start', self)
        onebtn.clicked.connect(QCoreApplication.instance().quit)
        onebtn.resize(onebtn.sizeHint())
        onebtn.move(70, 50)

    def two(self):

        twobtn = QPushButton('Record list', self)
        twobtn.clicked.connect(QCoreApplication.instance().quit)
        twobtn.resize(twobtn.sizeHint())
        twobtn.move(70, 80)

    def ini(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(70, 120)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())