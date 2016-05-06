#!/usr/bin/python
# -*- coding: utf-8 -*-
# quitbutton.py

import sys
from PyQt4 import QtGui, QtCore
class MainWindow(QtGui.QMainWindow):
    def __init__(self):


        QtGui.QWidget.__init__(self, parent=None)

        self.setGeometry(400,100, 650, 600)
        self.setWindowTitle('32KGame')

        quit = QtGui.QPushButton(u'Close', self)
        quit.setGeometry(260, 400, 150, 100) #1.X 2.Y 3.Len 4.size
        self.connect(quit, QtCore.SIGNAL('clicked()'),
        QtGui.qApp, QtCore.SLOT('quit()'))

        open = QtGui.QPushButton(u"Start",self)
        open.setGeometry(260, 10, 150, 100)
        self.connect(open, QtCore.SIGNAL('clicked()'),
        QtGui.qApp, QtCore.SLOT('start()'))


        options = QtGui.QPushButton(u"Options",self)
        options.setGeometry(260, 140, 150, 100)
        self.connect(options, QtCore.SIGNAL('clicked()'),
        QtGui.qApp, QtCore.SLOT('Options()'))

faq = QtGui.QPushButton(u"Options",self)
faq.setGeometry(260, 270, 150, 100)
self.connect(faq, QtCore.SIGNAL('clicked()'),
QtGui.qApp, QtCore.SLOT('FAQ()'))
