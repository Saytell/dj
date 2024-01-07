# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client_form(object):
    def setupUi(self, client_form):
        client_form.setObjectName("client_form")
        client_form.resize(470, 615)
        client_form.setStyleSheet("")
        self.comment = QtWidgets.QPushButton(client_form)
        self.comment.setGeometry(QtCore.QRect(120, 380, 221, 43))
        self.comment.setStyleSheet("QPushButton{\n"
"  display: inline-block;\n"
"  padding: 10px 20px;\n"
"  font-size: 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"  border-radius: 5px;\n"
"  transition: background-color 0.3s ease;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049;\n"
"  border-color: #45a049;\n"
"}\n"
"")
        self.comment.setObjectName("comment")
        self.order = QtWidgets.QPushButton(client_form)
        self.order.setGeometry(QtCore.QRect(120, 330, 221, 43))
        self.order.setStyleSheet("QPushButton{\n"
"  display: inline-block;\n"
"  padding: 10px 20px;\n"
"  font-size: 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"  border-radius: 5px;\n"
"  transition: background-color 0.3s ease;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049;\n"
"  border-color: #45a049;\n"
"}\n"
"")
        self.order.setObjectName("order")
        self.tours = QtWidgets.QPushButton(client_form)
        self.tours.setGeometry(QtCore.QRect(120, 280, 221, 43))
        self.tours.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tours.setStyleSheet("QPushButton{\n"
"  display: inline-block;\n"
"  padding: 10px 20px;\n"
"  font-size: 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"  border-radius: 5px;\n"
"  transition: background-color 0.3s ease;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049;\n"
"  border-color: #45a049;\n"
"}\n"
"")
        self.tours.setObjectName("tours")

        self.retranslateUi(client_form)
        QtCore.QMetaObject.connectSlotsByName(client_form)

    def retranslateUi(self, client_form):
        _translate = QtCore.QCoreApplication.translate
        client_form.setWindowTitle(_translate("client_form", "Frame"))
        self.comment.setText(_translate("client_form", "Оставить комментарий"))
        self.order.setText(_translate("client_form", "Составить тур"))
        self.tours.setText(_translate("client_form", "Туры"))

