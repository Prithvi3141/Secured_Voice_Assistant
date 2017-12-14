# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(787, 525)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.capturePhoto = QtWidgets.QPushButton(Form)
        self.capturePhoto.setGeometry(QtCore.QRect(320, 380, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.capturePhoto.setFont(font)
        self.capturePhoto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.capturePhoto.setMouseTracking(True)
        self.capturePhoto.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.capturePhoto.setAutoDefault(False)
        self.capturePhoto.setDefault(False)
        self.capturePhoto.setFlat(False)
        self.capturePhoto.setObjectName("capturePhoto")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 571, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        #self.capturePhoto.clicked.connect(Form.recognizeFace)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.capturePhoto.setText(_translate("Form", "Login"))
        #self.label.setText(_translate("Form", "Picture is not upto the required quality. It could be due to poor ambient light "))


