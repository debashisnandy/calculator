# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 170, 411, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_4.addWidget(self.pushButton_13)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_4.addWidget(self.pushButton_16)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 450, 411, 61))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_5.addWidget(self.pushButton_19)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_5.addWidget(self.pushButton_18)
        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_5.addWidget(self.pushButton_17)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 411, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 50, 411, 121))
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_14.setFixedHeight(50)
        self.pushButton.setFixedHeight(50)
        self.pushButton_2.setFixedHeight(50)
        self.pushButton_3.setFixedHeight(50)
        self.pushButton_4.setFixedHeight(50)
        self.pushButton_5.setFixedHeight(50)
        self.pushButton_6.setFixedHeight(50)
        self.pushButton_7.setFixedHeight(50)
        self.pushButton_8.setFixedHeight(50)
        self.pushButton_9.setFixedHeight(50)
        self.pushButton_10.setFixedHeight(50)
        self.pushButton_11.setFixedHeight(50)
        self.pushButton_12.setFixedHeight(50)
        self.pushButton_16.setFixedHeight(50)
        self.pushButton_17.setFixedHeight(50)
        self.pushButton_18.setFixedHeight(50)
        self.pushButton_19.setFixedHeight(50)
        self.pushButton_13.setFixedHeight(50)
        self.pushButton_15.setFixedHeight(50)
        self.pushButton_17.setFixedWidth(100)
        self.pushButton_18.setFixedWidth(100)
        self.valiInt = QtGui.QIntValidator()
        regxx = QRegExp("[0-9+*/%-]+")
        self.sspeci = QtGui.QRegExpValidator(regxx,self.lineEdit)
        self.lineEdit.setValidator(self.sspeci)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_12.setText(_translate("MainWindow", "7"))
        self.pushButton_11.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "9"))
        self.pushButton_9.setText(_translate("MainWindow", "x"))
        self.pushButton_4.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton.setText(_translate("MainWindow", "3"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "-"))
        self.pushButton_14.setText(_translate("MainWindow", "AC"))
        self.pushButton_13.setText(_translate("MainWindow", "+/-"))
        self.pushButton_16.setText(_translate("MainWindow", "%"))
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_19.setText(_translate("MainWindow", "0"))
        self.pushButton_18.setText(_translate("MainWindow", "."))
        self.pushButton_17.setText(_translate("MainWindow", "="))