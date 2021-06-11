# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 650)
        MainWindow.setMinimumSize(QtCore.QSize(790, 650))
        MainWindow.setMaximumSize(QtCore.QSize(790, 650))
        MainWindow.setStyleSheet(".QPushButton {\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
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
"    color: white;\n"
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
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 511, 521))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(540, 10, 241, 271))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 221, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 221, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 211, 20))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(10, 130, 61, 26))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 101, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 221, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 200, 221, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 221, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(540, 290, 241, 241))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 100, 221, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 221, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 221, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 70, 221, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 140, 221, 25))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 180, 221, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 210, 221, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 542, 761, 51))
        self.progressBar.setMaximum(2)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFIle.addAction(self.actionNew)
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Слово"))
        self.label_2.setText(_translate("MainWindow", "Переклад"))
        self.label_3.setText(_translate("MainWindow", "Номер слова"))
        self.pushButton.setText(_translate("MainWindow", "Додати слово"))
        self.pushButton_2.setText(_translate("MainWindow", "Змінити слово"))
        self.pushButton_3.setText(_translate("MainWindow", "Видалити слово"))
        self.pushButton_4.setText(_translate("MainWindow", "Почати"))
        self.radioButton.setText(_translate("MainWindow", "Переклад за словом"))
        self.radioButton_2.setText(_translate("MainWindow", "Слово за перекладом"))
        self.radioButton_3.setText(_translate("MainWindow", "Випадково"))
        self.pushButton_5.setText(_translate("MainWindow", "Прийняти"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


