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
        Form.resize(883, 733)
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
        self.gridLayout.addWidget(self.NextBtn, 5, 4, 1, 1)
        self.PreviousBtn = QtWidgets.QPushButton(self.TestPage)
        self.PreviousBtn.setObjectName("PreviousBtn")
        self.gridLayout.addWidget(self.PreviousBtn, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 4, 2, 1)
        self.PictureLabel = QtWidgets.QLabel(self.TestPage)
        self.PictureLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.PictureLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.PictureLabel.setText("")
        self.PictureLabel.setObjectName("PictureLabel")
        self.gridLayout.addWidget(self.PictureLabel, 0, 4, 1, 1)
        self.AnswerC = QtWidgets.QPushButton(self.TestPage)
        self.AnswerC.setMinimumSize(QtCore.QSize(250, 120))
        self.AnswerC.setMaximumSize(QtCore.QSize(300, 16777215))
        self.AnswerC.setObjectName("AnswerC")
        self.gridLayout.addWidget(self.AnswerC, 2, 0, 1, 1)
        self.AnswerB = QtWidgets.QPushButton(self.TestPage)
        self.AnswerB.setMinimumSize(QtCore.QSize(250, 120))
        self.AnswerB.setMaximumSize(QtCore.QSize(300, 16777215))
        self.AnswerB.setCheckable(False)
        self.AnswerB.setChecked(False)
        self.AnswerB.setObjectName("AnswerB")
        self.gridLayout.addWidget(self.AnswerB, 1, 2, 1, 1)
        self.AnswerD = QtWidgets.QPushButton(self.TestPage)
        self.AnswerD.setMinimumSize(QtCore.QSize(250, 120))
        self.AnswerD.setMaximumSize(QtCore.QSize(300, 16777215))
        self.AnswerD.setObjectName("AnswerD")
        self.gridLayout.addWidget(self.AnswerD, 2, 2, 1, 1)
        self.AnswerA = QtWidgets.QPushButton(self.TestPage)
        self.AnswerA.setMinimumSize(QtCore.QSize(250, 120))
        self.AnswerA.setMaximumSize(QtCore.QSize(300, 16777215))
        self.AnswerA.setObjectName("AnswerA")
        self.gridLayout.addWidget(self.AnswerA, 1, 0, 1, 1)
        self.QuestionText = QtWidgets.QTextBrowser(self.TestPage)
        self.QuestionText.setObjectName("QuestionText")
        self.gridLayout.addWidget(self.QuestionText, 0, 0, 1, 4)
        self.stackedWidget.addWidget(self.TestPage)
        self.MenuPage = QtWidgets.QWidget()
        self.MenuPage.setObjectName("MenuPage")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MenuPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.MenuPage)
        self.ChooseTestPage = QtWidgets.QWidget()
        self.ChooseTestPage.setObjectName("ChooseTestPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ChooseTestPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.ChooseTestPage)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.ChooseTestPage)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.label_5 = QtWidgets.QLabel(self.ChooseTestPage)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.nameLineEdit = QtWidgets.QLineEdit(self.ChooseTestPage)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.verticalLayout.addWidget(self.nameLineEdit)
        self.GenerateTestBtn = QtWidgets.QPushButton(self.ChooseTestPage)
        self.GenerateTestBtn.setObjectName("GenerateTestBtn")
        self.verticalLayout.addWidget(self.GenerateTestBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.stackedWidget.addWidget(self.ChooseTestPage)
        self.EndTestPage = QtWidgets.QWidget()
        self.EndTestPage.setObjectName("EndTestPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.EndTestPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BackToTestBtn = QtWidgets.QPushButton(self.EndTestPage)
        self.BackToTestBtn.setObjectName("BackToTestBtn")
        self.gridLayout_3.addWidget(self.BackToTestBtn, 1, 0, 1, 1)
        self.EndTestBtn = QtWidgets.QPushButton(self.EndTestPage)
        self.EndTestBtn.setObjectName("EndTestBtn")
        self.gridLayout_3.addWidget(self.EndTestBtn, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.EndTestPage)
        self.ResultsPage = QtWidgets.QWidget()
        self.ResultsPage.setObjectName("ResultsPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ResultsPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.ResultsPage)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 3, 1, 1)
        self.llabel = QtWidgets.QLabel(self.ResultsPage)
        self.llabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.llabel.setAutoFillBackground(False)
        self.llabel.setTextFormat(QtCore.Qt.AutoText)
        self.llabel.setObjectName("llabel")
        self.gridLayout_4.addWidget(self.llabel, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.ResultsPage)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 3, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.ResultsPage)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 6, 3, 1, 1)
        self.ResultsCorrectAnswer = QtWidgets.QTextBrowser(self.ResultsPage)
        self.ResultsCorrectAnswer.setObjectName("ResultsCorrectAnswer")
        self.gridLayout_4.addWidget(self.ResultsCorrectAnswer, 4, 3, 2, 2)
        self.ResultsQuestion = QtWidgets.QTextBrowser(self.ResultsPage)
        self.ResultsQuestion.setObjectName("ResultsQuestion")
        self.gridLayout_4.addWidget(self.ResultsQuestion, 2, 3, 1, 1)
        self.ResultsYourAnswer = QtWidgets.QTextBrowser(self.ResultsPage)
        self.ResultsYourAnswer.setObjectName("ResultsYourAnswer")
        self.gridLayout_4.addWidget(self.ResultsYourAnswer, 8, 3, 1, 2)
        self.ResultsImage = QtWidgets.QLabel(self.ResultsPage)
        self.ResultsImage.setMinimumSize(QtCore.QSize(250, 250))
        self.ResultsImage.setObjectName("ResultsImage")
        self.gridLayout_4.addWidget(self.ResultsImage, 2, 4, 1, 1)
        self.BackToMenuBtn_2 = QtWidgets.QPushButton(self.ResultsPage)
        self.BackToMenuBtn_2.setObjectName("BackToMenuBtn_2")
        self.gridLayout_4.addWidget(self.BackToMenuBtn_2, 9, 4, 1, 1)
        self.ResultsListWidget = QtWidgets.QListWidget(self.ResultsPage)
        self.ResultsListWidget.setObjectName("ResultsListWidget")
        self.gridLayout_4.addWidget(self.ResultsListWidget, 1, 2, 9, 1)
        self.stackedWidget.addWidget(self.ResultsPage)
        self.HistoryPage = QtWidgets.QWidget()
        self.HistoryPage.setObjectName("HistoryPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.HistoryPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 0, 5, 1)
        self.usersComboBox = QtWidgets.QComboBox(self.HistoryPage)
        self.usersComboBox.setObjectName("usersComboBox")
        self.gridLayout_5.addWidget(self.usersComboBox, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 4, 3, 1, 1)
        self.showUserBtn = QtWidgets.QPushButton(self.HistoryPage)
        self.showUserBtn.setObjectName("showUserBtn")
        self.gridLayout_5.addWidget(self.showUserBtn, 2, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.HistoryPage)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 0, 1, 2, 2)
        self.BackToMenuBtn = QtWidgets.QPushButton(self.HistoryPage)
        self.BackToMenuBtn.setObjectName("BackToMenuBtn")
        self.gridLayout_5.addWidget(self.BackToMenuBtn, 5, 3, 1, 1)
        self.historyTable = QtWidgets.QTableWidget(self.HistoryPage)
        self.historyTable.setMinimumSize(QtCore.QSize(0, 0))
        self.historyTable.setFrameShape(QtWidgets.QFrame.VLine)
        self.historyTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.historyTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.historyTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.historyTable.setAutoScroll(False)
        self.historyTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.historyTable.setShowGrid(True)
        self.historyTable.setWordWrap(True)
        self.historyTable.setRowCount(20)
        self.historyTable.setColumnCount(2)
        self.historyTable.setObjectName("historyTable")
        self.historyTable.horizontalHeader().setVisible(False)
        self.historyTable.horizontalHeader().setCascadingSectionResizes(False)
        self.historyTable.horizontalHeader().setDefaultSectionSize(200)
        self.historyTable.horizontalHeader().setStretchLastSection(False)
        self.historyTable.verticalHeader().setVisible(False)
        self.historyTable.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_5.addWidget(self.historyTable, 4, 1, 2, 1)
        self.stackedWidget.addWidget(self.HistoryPage)
        self.CreateNewPage = QtWidgets.QWidget()
        self.CreateNewPage.setObjectName("CreateNewPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.CreateNewPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.RemoveQuestionBtn_2 = QtWidgets.QPushButton(self.CreateNewPage)
        self.RemoveQuestionBtn_2.setObjectName("RemoveQuestionBtn_2")
        self.gridLayout_6.addWidget(self.RemoveQuestionBtn_2, 2, 1, 1, 1)
        self.AddQuestionBtn = QtWidgets.QPushButton(self.CreateNewPage)
        self.AddQuestionBtn.setObjectName("AddQuestionBtn")
        self.gridLayout_6.addWidget(self.AddQuestionBtn, 2, 2, 1, 1)
        self.CreateNewQuestionBtn = QtWidgets.QPushButton(self.CreateNewPage)
        self.CreateNewQuestionBtn.setObjectName("CreateNewQuestionBtn")
        self.gridLayout_6.addWidget(self.CreateNewQuestionBtn, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.CreateNewPage)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 5, 1, 1)
        self.SaveNewTestBtn = QtWidgets.QPushButton(self.CreateNewPage)
        self.SaveNewTestBtn.setObjectName("SaveNewTestBtn")
        self.gridLayout_6.addWidget(self.SaveNewTestBtn, 2, 6, 1, 1)
        self.AllQuestionsList = QtWidgets.QListWidget(self.CreateNewPage)
        self.AllQuestionsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.AllQuestionsList.setObjectName("AllQuestionsList")
        self.gridLayout_6.addWidget(self.AllQuestionsList, 1, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.CreateNewPage)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 2)
        self.BackToMenuBtn_3 = QtWidgets.QPushButton(self.CreateNewPage)
        self.BackToMenuBtn_3.setObjectName("BackToMenuBtn_3")
        self.gridLayout_6.addWidget(self.BackToMenuBtn_3, 2, 7, 1, 1)
        self.NewTestList = QtWidgets.QListWidget(self.CreateNewPage)
        self.NewTestList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.NewTestList.setObjectName("NewTestList")
        self.gridLayout_6.addWidget(self.NewTestList, 1, 3, 1, 5)
        self.RemoveQuestionBtn = QtWidgets.QPushButton(self.CreateNewPage)
        self.RemoveQuestionBtn.setObjectName("RemoveQuestionBtn")
        self.gridLayout_6.addWidget(self.RemoveQuestionBtn, 2, 5, 1, 1)
        self.stackedWidget.addWidget(self.CreateNewPage)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NextBtn.setText(_translate("Form", "Následující"))
        self.PreviousBtn.setText(_translate("Form", "Předchozí"))
        self.AnswerC.setText(_translate("Form", "C: sgsdggsdgsdgsdgsdgsdg\n"
"asfasfasfasfsafasf\n"
"afdsfsdgsgsdgsgdsg"))
        self.AnswerB.setText(_translate("Form", "B: sgsdggsdgsdgsdgsdgsdg\n"
"asfasfasfasfsafasf\n"
"afdsfsdgsgsdgsgdsg"))
        self.AnswerD.setText(_translate("Form", "D: sgsdggsdgsdgsdgsdgsdg\n"
"asfasfasfasfsafasf\n"
"afdsfsdgsgsdgsgdsg"))
        self.AnswerA.setText(_translate("Form", "A: sgsdggsdgsdgsdgsdgsdg\n"
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
        self.label_5.setText(_translate("Form", "Zadejte vaše jméno:"))
        self.GenerateTestBtn.setText(_translate("Form", "Spustit test"))
        self.BackToTestBtn.setText(_translate("Form", "Zpět na otázky"))
        self.EndTestBtn.setText(_translate("Form", "Ukončit a vyhodnotit test"))
        self.label_4.setText(_translate("Form", "Správná odpověď:"))
        self.llabel.setText(_translate("Form", "Výsledky"))
        self.label_2.setText(_translate("Form", "Otázka:"))
        self.label_3.setText(_translate("Form", "Vaše odpověď:"))
        self.ResultsImage.setText(_translate("Form", "Obrázek"))
        self.BackToMenuBtn_2.setText(_translate("Form", "Zpět do menu"))
        self.showUserBtn.setText(_translate("Form", "Ukázat"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Historie výsledků</span></p></body></html>"))
        self.BackToMenuBtn.setText(_translate("Form", "Zpět do menu"))
        self.historyTable.setSortingEnabled(False)
        self.RemoveQuestionBtn_2.setText(_translate("Form", "Odstranit"))
        self.AddQuestionBtn.setText(_translate("Form", "Přidat označené otázky"))
        self.CreateNewQuestionBtn.setText(_translate("Form", "Vytvořit novou otázku"))
        self.label_7.setText(_translate("Form", "Otázky v novém testu:"))
        self.SaveNewTestBtn.setText(_translate("Form", "Uložit test"))
        self.label_6.setText(_translate("Form", "Všechny otázky (dvojklik pro zobrazení):"))
        self.BackToMenuBtn_3.setText(_translate("Form", "Zpět do menu"))
        self.RemoveQuestionBtn.setText(_translate("Form", "Odstranit vybrané"))

