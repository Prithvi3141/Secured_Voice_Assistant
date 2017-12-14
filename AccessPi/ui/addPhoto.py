# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddPhoto(object):
    def setupUi(self, AddPhoto):
        AddPhoto.setObjectName("AddPhoto")
        AddPhoto.resize(787, 525)
        AddPhoto.setAutoFillBackground(False)
        AddPhoto.setStyleSheet("")
        self.capturePhoto = QtWidgets.QPushButton(AddPhoto)
        self.capturePhoto.setGeometry(QtCore.QRect(350, 420, 141, 31))
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
        self.label = QtWidgets.QLabel(AddPhoto)
        self.label.setGeometry(QtCore.QRect(110, 10, 571, 31))
        self.label.setObjectName("label")

        self.retranslateUi(AddPhoto)
        #self.capturePhoto.clicked.connect(Form.recognizeFace)
        QtCore.QMetaObject.connectSlotsByName(AddPhoto)

    def retranslateUi(self, AddPhoto):
        _translate = QtCore.QCoreApplication.translate
        AddPhoto.setWindowTitle(_translate("AddPhoto", "AddPhoto"))
        self.capturePhoto.setText(_translate("AddPhoto", "Add Photo"))
        #self.label.setText(_translate("Form", "Picture is not upto the required quality. It could be due to poor ambient light "))


