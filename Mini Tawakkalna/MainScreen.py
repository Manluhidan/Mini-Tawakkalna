# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgwidget = QtWidgets.QWidget(self.centralwidget)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255))}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 291, 61))
        self.label.setStyleSheet("font: 40pt \"Microsoft YaHei UI\";;color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255))\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 351, 51))
        self.label_2.setStyleSheet("font: 20pt \"Microsoft YaHei UI Light\";;color:rgb(0,0,0);")
        self.label_2.setObjectName("label_2")
        self.Check_in = QtWidgets.QPushButton(self.bgwidget)
        self.Check_in.setGeometry(QtCore.QRect(260, 230, 281, 61))
        self.Check_in.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Check_in.setObjectName("Check_in")
        self.ImCheck = QtWidgets.QPushButton(self.bgwidget)
        self.ImCheck.setGeometry(QtCore.QRect(260, 310, 281, 61))
        self.ImCheck.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.ImCheck.setObjectName("ImCheck")
        self.Import = QtWidgets.QPushButton(self.bgwidget)
        self.Import.setGeometry(QtCore.QRect(210, 390, 171, 61))
        self.Import.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Import.setObjectName("Import")
        self.Export = QtWidgets.QPushButton(self.bgwidget)
        self.Export.setGeometry(QtCore.QRect(430, 390, 171, 61))
        self.Export.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(0, 129, 94, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Export.setObjectName("Export")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tawakkalna"))
        self.label_2.setText(_translate("MainWindow", "Check in or Immunity Check"))
        self.Check_in.setText(_translate("MainWindow", "Check in"))
        self.ImCheck.setText(_translate("MainWindow", "Immunity Check"))
        self.Import.setText(_translate("MainWindow", "Import"))
        self.Export.setText(_translate("MainWindow", "Export"))
