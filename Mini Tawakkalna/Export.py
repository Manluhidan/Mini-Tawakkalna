# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Export.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Export(object):
    def setupUi(self, Export):
        Export.setObjectName("Export")
        Export.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Export)
        self.centralwidget.setObjectName("centralwidget")
        self.bgwidget = QtWidgets.QWidget(self.centralwidget)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255))}")
        self.bgwidget.setObjectName("bgwidget")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 120, 201, 51))
        self.label_2.setStyleSheet("font: 16pt \"Microsoft YaHei UI Light\";;color:rgb(0,0,0);")
        self.label_2.setObjectName("label_2")
        self.Export_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Export_bot.setGeometry(QtCore.QRect(250, 290, 281, 61))
        self.Export_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Export_bot.setObjectName("Export_bot")
        self.exportField = QtWidgets.QLineEdit(self.bgwidget)
        self.exportField.setGeometry(QtCore.QRect(270, 230, 231, 31))
        self.exportField.setObjectName("exportField")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 291, 61))
        self.label.setStyleSheet("font: 40pt \"Microsoft YaHei UI\";;color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255))\n"
"\n"
"")
        self.label.setObjectName("label")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(270, 190, 321, 31))
        self.error.setStyleSheet("font: 8pt \"Microsoft YaHei UI Light\";\n"
"color: red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.Go_Back = QtWidgets.QPushButton(self.bgwidget)
        self.Go_Back.setGeometry(QtCore.QRect(250, 360, 281, 61))
        self.Go_Back.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 147, 154, 255), stop:1 rgba(91, 100, 103, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Go_Back.setObjectName("Go_Back")
        self.browse_bot = QtWidgets.QPushButton(self.bgwidget)
        self.browse_bot.setGeometry(QtCore.QRect(510, 230, 81, 31))
        self.browse_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255));\n"
"border-radius:10px;\n"
"font: 15pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.browse_bot.setObjectName("browse_bot")
        Export.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Export)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Export.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Export)
        self.statusbar.setObjectName("statusbar")
        Export.setStatusBar(self.statusbar)

        self.retranslateUi(Export)
        QtCore.QMetaObject.connectSlotsByName(Export)

    def retranslateUi(self, Export):
        _translate = QtCore.QCoreApplication.translate
        Export.setWindowTitle(_translate("Export", "MainWindow"))
        self.label_2.setText(_translate("Export", "Enter the file\'s name"))
        self.Export_bot.setText(_translate("Export", "Export"))
        self.exportField.setPlaceholderText(_translate("Export", "Enter file name"))
        self.label.setText(_translate("Export", "Tawakkalna"))
        self.Go_Back.setText(_translate("Export", "Go Back"))
        self.browse_bot.setText(_translate("Export", "Browse"))
