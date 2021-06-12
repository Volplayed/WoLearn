# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'askWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 133)
        MainWindow.setMinimumSize(QtCore.QSize(392, 133))
        MainWindow.setMaximumSize(QtCore.QSize(392, 133))
        MainWindow.setStyleSheet(".QPushButton {\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"    background-color: rgb(245, 121, 0);\n"
"\n"
"}\n"
"\n"
".QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"}\n"
"\n"
".QSpinBox {\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"    background-color: rgb(136, 138, 133);\n"
"\n"
"}\n"
"\n"
".QLineEdit {\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"\n"
".QTextEdit {\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
".QRadioButton {\n"
"    font-weight:bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"\n"
".QMainWindow {\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"\n"
".QFrame {\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
".QProgressBar {\n"
"    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25) inset;\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"\n"
".QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00490196 rgba(114, 200, 30, 255), stop:1 rgba(43, 89, 0, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 371, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 50, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 50, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ви впевнені"))
        self.label.setText(_translate("MainWindow", "Ви впевнені, що хочете очистити всі зміни?"))
        self.pushButton.setText(_translate("MainWindow", "Не зберігати"))
        self.pushButton_2.setText(_translate("MainWindow", "Зберегти і вийти"))
        self.pushButton_3.setText(_translate("MainWindow", "Скасувати"))

