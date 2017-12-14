# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(700, 500)
        Dashboard.setAutoFillBackground(False)
        Dashboard.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dashboard)
        self.label.setGeometry(QtCore.QRect(20, 20, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dashboard)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 641, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.registerButton = QtWidgets.QPushButton(Dashboard)
        self.registerButton.setGeometry(QtCore.QRect(450, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.registerButton.setFont(font)
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerButton.setObjectName("registerButton")
        self.label_3 = QtWidgets.QLabel(Dashboard)
        self.label_3.setGeometry(QtCore.QRect(30, 340, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dashboard)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 641, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_2")
        self.logoutButton = QtWidgets.QPushButton(Dashboard)
        self.logoutButton.setGeometry(QtCore.QRect(260, 380, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")

        self.retranslateUi(Dashboard)
        #self.registerButton.clicked.connect(Dashboard.registerUser)
        #self.logoutButton.clicked.connect(Dashboard.logout)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Form"))
        #self.label.setText(_translate("Dashboard", "Hello prithvi3141"))
        #self.label_2.setText(_translate("Dashboard", "You have been granted access to Book My Show, \n"
#"a Secure Voice Assisted movie show booking website"))
        self.registerButton.setText(_translate("Dashboard", "Register"))
        #self.label_3.setText(_translate("Dashboard", "Do you want to add a new user?"))
        self.logoutButton.setText(_translate("Dashboard", "Logout"))

#import homepage_resource_rc
