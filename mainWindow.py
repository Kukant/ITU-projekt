# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(892, 622)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 120))
        self.stackedWidget.setObjectName("stackedWidget")
        self.TestPage = QtWidgets.QWidget()
        self.TestPage.setObjectName("TestPage")
        self.gridLayout = QtWidgets.QGridLayout(self.TestPage)
        self.gridLayout.setObjectName("gridLayout")
        self.NextBtn = QtWidgets.QPushButton(self.TestPage)
        self.NextBtn.setObjectName("NextBtn")
        self.gridLayout.addWidget(self.NextBtn, 6, 4, 1, 1)
        self.AnswerB = QtWidgets.QPushButton(self.TestPage)
        self.AnswerB.setMinimumSize(QtCore.QSize(0, 120))
        self.AnswerB.setCheckable(False)
        self.AnswerB.setChecked(False)
        self.AnswerB.setObjectName("AnswerB")
        self.gridLayout.addWidget(self.AnswerB, 2, 3, 1, 1)
        self.AnswerA = QtWidgets.QPushButton(self.TestPage)
        self.AnswerA.setMinimumSize(QtCore.QSize(0, 120))
        self.AnswerA.setObjectName("AnswerA")
        self.gridLayout.addWidget(self.AnswerA, 2, 2, 1, 1)
        self.AnswerC = QtWidgets.QPushButton(self.TestPage)
        self.AnswerC.setMinimumSize(QtCore.QSize(0, 120))
        self.AnswerC.setObjectName("AnswerC")
        self.gridLayout.addWidget(self.AnswerC, 3, 2, 1, 1)
        self.PreviousBtn = QtWidgets.QPushButton(self.TestPage)
        self.PreviousBtn.setObjectName("PreviousBtn")
        self.gridLayout.addWidget(self.PreviousBtn, 6, 0, 1, 1)
        self.AnswerD = QtWidgets.QPushButton(self.TestPage)
        self.AnswerD.setMinimumSize(QtCore.QSize(0, 120))
        self.AnswerD.setObjectName("AnswerD")
        self.gridLayout.addWidget(self.AnswerD, 3, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 4, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 4, 2, 1)
        self.PictureLabel = QtWidgets.QLabel(self.TestPage)
        self.PictureLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.PictureLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.PictureLabel.setText("")
        self.PictureLabel.setObjectName("PictureLabel")
        self.gridLayout.addWidget(self.PictureLabel, 0, 4, 1, 1)
        self.QuestionText = QtWidgets.QTextBrowser(self.TestPage)
        self.QuestionText.setObjectName("QuestionText")
        self.gridLayout.addWidget(self.QuestionText, 0, 1, 1, 3)
        self.stackedWidget.addWidget(self.TestPage)
        self.MenuPage = QtWidgets.QWidget()
        self.MenuPage.setObjectName("MenuPage")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MenuPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.StartTestBtn = QtWidgets.QPushButton(self.MenuPage)
        self.StartTestBtn.setObjectName("StartTestBtn")
        self.verticalLayout_2.addWidget(self.StartTestBtn)
        self.CreateTestBtn = QtWidgets.QPushButton(self.MenuPage)
        self.CreateTestBtn.setObjectName("CreateTestBtn")
        self.verticalLayout_2.addWidget(self.CreateTestBtn)
        self.HistoryBtn = QtWidgets.QPushButton(self.MenuPage)
        self.HistoryBtn.setObjectName("HistoryBtn")
        self.verticalLayout_2.addWidget(self.HistoryBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.stackedWidget.addWidget(self.MenuPage)
        self.ChooseTestPage = QtWidgets.QWidget()
        self.ChooseTestPage.setObjectName("ChooseTestPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ChooseTestPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.ChooseTestPage)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.ChooseTestPage)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.GenerateTestBtn = QtWidgets.QPushButton(self.ChooseTestPage)
        self.GenerateTestBtn.setObjectName("GenerateTestBtn")
        self.verticalLayout.addWidget(self.GenerateTestBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.stackedWidget.addWidget(self.ChooseTestPage)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NextBtn.setText(_translate("Form", "Následující"))
        self.AnswerB.setText(_translate("Form", "B: sgsdggsdgsdgsdgsdgsdg\n"
"asfasfasfasfsafasf\n"
"afdsfsdgsgsdgsgdsg"))
        self.AnswerA.setText(_translate("Form", "A: sgsdggsdgsdgsdgsdgsdg\n"
"asfasfasfasfsafasf\n"
"afdsfsdgsgsdgsgdsg"))
        self.AnswerC.setText(_translate("Form", "C: sgsdggsdgsdgsdgsdgsdg\n"
"asfasfasfasfsafasf\n"
"afdsfsdgsgsdgsgdsg"))
        self.PreviousBtn.setText(_translate("Form", "Předchozí"))
        self.AnswerD.setText(_translate("Form", "D: sgsdggsdgsdgsdgsdgsdg\n"
"asfasfasfasfsafasf\n"
"afdsfsdgsgsdgsgdsg"))
        self.QuestionText.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nejaky hodne dlohy text</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">s enterma</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a tak.... a otaznikem na konci ?</p></body></html>"))
        self.StartTestBtn.setText(_translate("Form", "Spustit test"))
        self.CreateTestBtn.setText(_translate("Form", "Vytvořit test"))
        self.HistoryBtn.setText(_translate("Form", "Historie"))
        self.label.setText(_translate("Form", "Vyberte si test:"))
        self.GenerateTestBtn.setText(_translate("Form", "Spustit test"))

