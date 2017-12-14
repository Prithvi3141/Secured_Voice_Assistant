# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addUser.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddUser(object):
    def setupUi(self, AddUser):
        AddUser.setObjectName("AddUser")
        AddUser.resize(700, 500)
        AddUser.setAutoFillBackground(False)
        AddUser.setStyleSheet("")
        self.label = QtWidgets.QLabel(AddUser)
        self.label.setGeometry(QtCore.QRect(160, 20, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.logoutButton = QtWidgets.QPushButton(AddUser)
        self.logoutButton.setGeometry(QtCore.QRect(270, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.formLayoutWidget = QtWidgets.QWidget(AddUser)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 110, 431, 142))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setItalic(True)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.emailIdLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.emailIdLineEdit.setObjectName("emailIdLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.emailIdLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setItalic(True)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)

        self.passwordLineEdit.setObjectName("passwordLineEdit")
        #Editing the below line
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.emailIdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setItalic(True)
        self.emailIdLabel.setFont(font)
        self.emailIdLabel.setObjectName("emailIdLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.emailIdLabel)

        self.retranslateUi(AddUser)
        #self.logoutButton.clicked.connect(AddUser.logout)
        QtCore.QMetaObject.connectSlotsByName(AddUser)

    def retranslateUi(self, AddUser):
        _translate = QtCore.QCoreApplication.translate
        AddUser.setWindowTitle(_translate("AddUser", "Form"))
        self.label.setText(_translate("AddUser", "User Registration !! :)"))
        self.logoutButton.setText(_translate("AddUser", "Register"))
        self.usernameLabel.setText(_translate("AddUser", "Username"))
        self.passwordLabel.setText(_translate("AddUser", "Password"))
        self.emailIdLabel.setText(_translate("AddUser", "Email Id"))

#import homepage_resource_rc
