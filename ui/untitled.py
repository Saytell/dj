# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(545, 499)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(100, 10, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login = QtWidgets.QLineEdit(Frame)
        self.login.setGeometry(QtCore.QRect(200, 210, 151, 31))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(Frame)
        self.password.setGeometry(QtCore.QRect(200, 250, 151, 31))
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(140, 210, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(130, 260, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.autorization = QtWidgets.QPushButton(Frame)
        self.autorization.setGeometry(QtCore.QRect(200, 330, 141, 41))
        self.autorization.setObjectName("autorization")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Авторизация"))
        self.label_2.setText(_translate("Frame", "Логин"))
        self.label_3.setText(_translate("Frame", "Пароль"))
        self.autorization.setText(_translate("Frame", "Авторизоваться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())