"""
    ITU projekt - Autoskola
    Autori: xkukan00, xmoros01, xpolak34

"""
from PyQt5 import QtCore, QtGui, QtWidgets
import glob
import json
import mainWindow
import CreateNewQuestionWindow

class newQuestionWin(CreateNewQuestionWindow.Ui_Form):
    pass

class mainWindow(mainWindow.Ui_Form):
    # name
    name = "Kuky"
    # python dict with opened test
    openedTest = None
    # current question index
    currentIndex = 0
    # arr of answers
    answers = []

    def initWindow(self):
        self.changePage("Menu")
        self.initButtons()

    def initButtons(self):
        self.StartTestBtn.clicked.connect(lambda: self.changePage("ChooseTest"))
        self.GenerateTestBtn.clicked.connect(self.generateTest)
        self.AnswerA.clicked.connect(lambda: self.selectAnswer(0))
        self.AnswerB.clicked.connect(lambda: self.selectAnswer(1))
        self.AnswerC.clicked.connect(lambda: self.selectAnswer(2))
        self.AnswerD.clicked.connect(lambda: self.selectAnswer(3))
        self.NextBtn.clicked.connect(lambda: self.setQuestion(self.currentIndex + 1))
        self.PreviousBtn.clicked.connect(lambda: self.setQuestion(self.currentIndex - 1))
        self.BackToTestBtn.clicked.connect(lambda: self.changePage("Test"))
        self.EndTestBtn.clicked.connect(lambda: self.changePage("Results"))
        self.ResultsListWidget.doubleClicked.connect(self.showResultAnswer)
        self.HistoryBtn.clicked.connect(lambda: self.changePage("History"))
        self.BackToMenuBtn.clicked.connect(lambda: self.changePage("Menu"))
        self.BackToMenuBtn_2.clicked.connect(lambda: self.changePage("Menu"))
        self.showUserBtn.clicked.connect(self.showUserHistory)

    def showResultAnswer(self):
        index = 0
        if self.ResultsListWidget.currentRow() is not None:
            index = self.ResultsListWidget.currentRow()
        questions = self.openedTest["list"]
        self.ResultsQuestion.setText(questions[index]["question"])
        self.ResultsYourAnswer.setText(questions[index]["answers"][self.answers[index]])
        self.ResultsCorrectAnswer.setText(questions[index]["answers"][questions[index]["correctAns"]])
        if questions[index]["imagePath"] is not None:
            pixmap = QtGui.QPixmap(questions[index]["imagePath"])
            self.ResultsImage.setPixmap(pixmap.scaled(250, 250))
        else:
            self.ResultsImage.clear()

    def changePage(self, pageName):
        if pageName == "Test":
            self.stackedWidget.setCurrentWidget(self.TestPage)
        elif pageName == "Menu":
            self.stackedWidget.setCurrentWidget(self.MenuPage)
        elif pageName == "ChooseTest":
            self.stackedWidget.setCurrentWidget(self.ChooseTestPage)
            self.chooseTestGenerator()
        elif pageName == "Results":
            self.stackedWidget.setCurrentWidget(self.ResultsPage)
            self.generateResults()
            self.showResultAnswer()
        elif pageName == "EndTest":
            self.stackedWidget.setCurrentWidget(self.EndTestPage)
        elif pageName == "History":
            self.stackedWidget.setCurrentWidget(self.HistoryPage)
            self.generateHistory()

    def showUserHistory(self):
        user = self.usersComboBox.currentText()
        if user == "Všichni":
            self.generateHistory()
        else:
            with open("history.json") as history:
                if history is None:
                    return
                history = json.load(history)
                userHistory = []
                for record in history["list"]:
                    if record["name"] == user:
                        userHistory.append(record)
                self.generateHistoryTable(userHistory)

    def generateHistory(self):
        with open("history.json") as history:
            if history is None:
                return
            history = json.load(history)
            allUsers = ["Všichni"]
            for record in history["list"]:
                if record["name"] not in allUsers:
                    allUsers.append(record["name"])

            self.usersComboBox.clear()
            self.usersComboBox.addItems(allUsers)
            self.generateHistoryTable(history["list"])

    def generateHistoryTable(self, listOfResults):
        self.historyTable.clearContents()
        for i, record in enumerate(listOfResults):
            if i == 20:
                break
            name = QtWidgets.QTableWidgetItem()
            name.setText(record["name"])
            self.historyTable.setItem(i, 0, name)
            score = QtWidgets.QTableWidgetItem()
            score.setText(str(record["score"] * 100)[0:5] + " %")
            if record["score"] > 0.75:
                score.setBackground(QtGui.QColor(178, 255, 178))
            else:
                score.setBackground(QtGui.QColor(255, 178, 178))
            self.historyTable.setItem(i, 1, score)


    def generateResults(self):
        # add result to result file
        self.addToHistory()
        self.ResultsListWidget.clear()

        for i, question in enumerate(self.openedTest["list"]):
            itemText = question["question"][0:30]
            if len(itemText) == 15:
                itemText = itemText + "..."
            item = QtWidgets.QListWidgetItem(itemText)
            if question["correctAns"] == self.answers[i]: # if true
                item.setBackground(QtGui.QColor(178, 255, 178))
            else:
                item.setBackground(QtGui.QColor(255, 178, 178))
            self.ResultsListWidget.addItem(item)

    def generateTest(self):
        if self.nameLineEdit.text() == "":
            return
        else:
            self.name = self.nameLineEdit.text()
        if self.listWidget.currentItem() is not None:
            fileName = self.listWidget.currentItem().text()
            self.openedTest = json.load(open(fileName))
            self.setQuestion(self.currentIndex)
            self.changePage("Test")
            # init answer array
            self.answers = [None] * len(self.openedTest["list"])

    def chooseTestGenerator(self):
        self.nameLineEdit.setText("")
        self.listWidget.clear()
        allTests = glob.glob("*.JSON")
        self.listWidget.addItems(allTests)

    def setQuestion(self, index):
        if index < 0 or index > len(self.openedTest["list"]):
            return
        if index == len(self.openedTest["list"]):
            self.changePage("EndTest")
            return

        self.currentIndex = index
        question = self.openedTest["list"][index]

        self.AnswerA.setText(question["answers"][0])
        self.AnswerB.setText(question["answers"][1])
        self.AnswerC.setText(question["answers"][2])
        self.AnswerD.setText(question["answers"][3])

        self.QuestionText.setText(question["question"])
        if question["imagePath"] is not None:
            pixmap = QtGui.QPixmap(question["imagePath"])
            self.PictureLabel.setPixmap(pixmap.scaled(300, 300))
        else:
            self.PictureLabel.clear()

    def selectAnswer(self, answerNum):
        self.answers[self.currentIndex] = answerNum
        self.setQuestion(self.currentIndex + 1)

    def addToHistory(self):
        with open("history.json") as file:
            if file is None:  # create new file
                fileDict = {"list": []}
            else:
                fileDict = json.load(file)
            score = len([x for i, x in enumerate(self.answers) if x == self.openedTest["list"][i]["correctAns"]]) / \
                    len(self.openedTest["list"])
            fileDict["list"].insert(0, {"name": self.name, "score": score})
            with open("history.json", "w") as f:
                f.write(json.dumps(fileDict, indent=2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mainWindow()
    ui.setupUi(Form)
    ui.initWindow()
    Form.show()
    sys.exit(app.exec_())
