"""
    ITU projekt - Autoskola
    Autori: xkukan00, xmoros01, xpolak34

"""
from PyQt5 import QtCore, QtGui, QtWidgets
import glob
import json
from mainWindow import Ui_Form


class mainWindow(Ui_Form):
    # python dict with opened test
    openedTest = None
    currentIndex = 0
    # current question index

    def initWindow(self):
        self.changePage("Menu")
        self.initButtons()

    def initButtons(self):
        self.StartTestBtn.clicked.connect(lambda: self.changePage("ChooseTest"))
        self.GenerateTestBtn.clicked.connect(self.generateTest)

    def changePage(self, pageName):
        if pageName == "Test":
            self.stackedWidget.setCurrentWidget(self.TestPage)
        elif pageName == "Menu":
            self.stackedWidget.setCurrentWidget(self.MenuPage)
        elif pageName == "ChooseTest":
            self.stackedWidget.setCurrentWidget(self.ChooseTestPage)
            self.chooseTestGenerator()

    def generateTest(self):
        if self.listWidget.currentItem() is not None:
            fileName = self.listWidget.currentItem().text()
            self.openedTest = json.load(open(fileName))
            self.setQuestion(self.currentIndex)
            self.changePage("Test")

    def chooseTestGenerator(self):
        allTests = glob.glob("*.JSON")
        self.listWidget.addItems(allTests)

    def setQuestion(self, index):
        if index < 0 or index >= len(self.openedTest["list"]):
            return
        question = self.openedTest["list"][index]

        self.AnswerA.setText(question["answers"][0])
        self.AnswerB.setText(question["answers"][1])
        self.AnswerC.setText(question["answers"][2])
        self.AnswerD.setText(question["answers"][3])

        self.QuestionText.setText(question["question"])
        if question["imagePath"] is not None:
            pixmap = QtGui.QPixmap(question["imagePath"])
            self.PictureLabel.setPixmap(pixmap.scaled(300, 300))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mainWindow()
    ui.setupUi(Form)
    ui.initWindow()
    Form.show()
    sys.exit(app.exec_())
