# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateNewQuestionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(826, 523)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 5, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.Answer2 = QtWidgets.QTextEdit(Form)
        self.Answer2.setObjectName("Answer2")
        self.gridLayout.addWidget(self.Answer2, 10, 0, 1, 3)
        self.Question = QtWidgets.QTextEdit(Form)
        self.Question.setObjectName("Question")
        self.gridLayout.addWidget(self.Question, 3, 0, 3, 3)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 11, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 3, 1, 2)
        self.Answer1 = QtWidgets.QTextEdit(Form)
        self.Answer1.setObjectName("Answer1")
        self.gridLayout.addWidget(self.Answer1, 8, 3, 1, 3)
        self.Answer3 = QtWidgets.QTextEdit(Form)
        self.Answer3.setObjectName("Answer3")
        self.gridLayout.addWidget(self.Answer3, 10, 3, 1, 3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.Answer0 = QtWidgets.QTextEdit(Form)
        self.Answer0.setObjectName("Answer0")
        self.gridLayout.addWidget(self.Answer0, 8, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Odpověď 1:"))
        self.label_4.setText(_translate("Form", "Odpověď 3:"))
        self.label_6.setText(_translate("Form", "Cesta k obrázku:"))
        self.pushButton.setText(_translate("Form", "Vybrat obrázek"))
        self.label_3.setText(_translate("Form", "Odpověď 2:"))
        self.pushButton_2.setText(_translate("Form", "Přidat"))
        self.label.setText(_translate("Form", "Otázka:"))
        self.label_2.setText(_translate("Form", "Odpověď 0:"))
        self.label_7.setText(_translate("Form", "Správná odpověď:"))

