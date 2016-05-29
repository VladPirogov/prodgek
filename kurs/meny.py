#!/usr/bin/python
# -*- coding: utf-8 -*-
# quitbutton.py

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox
from PyQt5.QtCore import QCoreApplication
from prodgek import *





class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.ini()
        self.one()
        self.two()
        self.setGeometry(300, 300, 200, 190)
        self.setWindowTitle('main')
        self.show()
    def one(self):
        onebtn = QPushButton('Start', self)
        onebtn.clicked.connect(self.yorm)
        onebtn.resize(onebtn.sizeHint())
        onebtn.move(70, 50)
    def two(self):
        twobtn = QPushButton('Record list', self)
        twobtn.clicked.connect(self.show_result)
        twobtn.resize(twobtn.sizeHint())
        twobtn.move(70, 80)
    def ini(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(70, 120)
    def show_result (self,event):
        f= open('Record lis', 'r')
        z=f.read()
        reply = QMessageBox()
        reply.setText(z)
        reply.exec()
    def yorm(self):
        zetT=False
        game(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    f.close()