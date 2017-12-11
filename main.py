"""
    ITU projekt - Autoskola
    Autori: xkukan00, xmoros01, xpolak34
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import glob
import json
import mainWindow
import CreateNewQuestionWindow


class newQuestionWin(CreateNewQuestionWindow.Ui_Form):
    def initButtons(self):
        self.pushButton.clicked.connect(self.openFileBrowser)

    def openFileBrowser(self):
        filters = "Images (*.png *.xpm *.jpg)"
        selected_filter = "Images (*.png *.xpm *.jpg)"
        dialog = QtWidgets.QFileDialog()
        # returns tuple (folder path, sth)
        folder_path = dialog.getOpenFileName(None, "Select image file", None, filters, selected_filter)[0]
        self.lineEdit.setText(folder_path)


class mainWin(mainWindow.Ui_Form):
    # name
    name = "Kuky"
    # python dict with opened test
    openedTest = None
    # current question index
    currentIndex = 0
    # arr of answers
    answers = []
    # all questions (file questions.JSON)
    allQuestions = []
    # list of new test's questions
    newQuestions = []


    def initWindow(self):
        self.changePage("Menu")
        self.newQuestionWindow = QtWidgets.QWidget()
        self.newQuestionUi = newQuestionWin()
        self.newQuestionUi.setupUi(self.newQuestionWindow)
        self.newQuestionUi.initButtons()
        self.newQuestionUi.pushButton_2.clicked.connect(self.saveNewQuestion)
        self.initButtons()
        # self.newQuestionWindow.show()

    def saveNewQuestion(self):
        ans0 = self.newQuestionUi.Answer0.toPlainText()
        ans1 = self.newQuestionUi.Answer1.toPlainText()
        ans2 = self.newQuestionUi.Answer2.toPlainText()
        ans3 = self.newQuestionUi.Answer3.toPlainText()
        question = self.newQuestionUi.Question.toPlainText()
        corrAns = int(self.newQuestionUi.spinBox.value().__str__())
        picture = self.newQuestionUi.lineEdit.text()
        newQuestion = {
                      "correctAns": corrAns,
                      "answers": [ans0, ans1, ans2, ans3],
                      "imagePath": picture if picture != "" else None,
                      "question": question
                      }
        self.newQuestionHandler("addNew", newQuestion)
        self.newQuestionWindow.hide()

    def openNewQuestion(self):
        self.newQuestionUi.Answer0.setText("")
        self.newQuestionUi.Answer1.setText("")
        self.newQuestionUi.Answer2.setText("")
        self.newQuestionUi.Answer3.setText("")
        self.newQuestionUi.Question.setText("")
        self.newQuestionUi.spinBox.setValue(0)
        self.newQuestionWindow.show()

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
        self.BackToMenuBtn_3.clicked.connect(lambda: self.changePage("Menu"))
        self.showUserBtn.clicked.connect(self.showUserHistory)
        self.CreateTestBtn.clicked.connect(lambda: self.changePage("CreateNew"))
        self.CreateNewQuestionBtn.clicked.connect(self.openNewQuestion)
        self.AddQuestionBtn.clicked.connect(lambda: self.newQuestionHandler("addExisting"))
        self.RemoveQuestionBtn_2.clicked.connect(lambda: self.newQuestionHandler("removeFromAll"))
        self.SaveNewTestBtn.clicked.connect(lambda: self.newQuestionHandler("saveNewTest"))
        self.RemoveQuestionBtn.clicked.connect(lambda: self.newQuestionHandler("removeFromNew"))


    def newQuestionHandler(self, whatToDo, arg = None):
        if whatToDo == "addNew":
            self.allQuestions.append(arg)
            newItem = QtWidgets.QListWidgetItem()
            newItem.setText(arg["question"])
            self.AllQuestionsList.addItem(newItem)
            with open("questions.JSON") as allQ:
                allQDict = json.load(allQ)
                allQDict["list"] = self.allQuestions
                with open("questions.JSON", "w") as fw:
                    fw.write(json.dumps(allQDict, indent=2))

        elif whatToDo == "init":
            self.newTestFileName = ""
            self.newQuestions.clear()
            with open("questions.JSON") as f:
                if f is None:
                    self.allQuestions = []
                else:
                    self.allQuestions = json.load(f)["list"]
            self.AllQuestionsList.clear()
            self.AllQuestionsList.addItems([x["question"] for x in self.allQuestions])
            self.NewTestList.clear()

        elif whatToDo == "addExisting":
            print("adding Existing")
            selectedLines = [x.row() for x in self.AllQuestionsList.selectedIndexes()]
            for line in selectedLines:
                self.newQuestions.append(self.allQuestions[line])
            self.NewTestList.addItems([self.allQuestions[line]["question"] for line in selectedLines])

        elif whatToDo == "removeFromAll":
            if self.AllQuestionsList.currentItem() is None:
                return
            with open("questions.JSON") as allQ:
                allQDict = json.load(allQ)
                selectedLines = [x.row() for x in self.AllQuestionsList.selectedIndexes()]
                selectedLines.sort(reverse=True) # will delete from the end
                for line in selectedLines:
                    del allQDict["list"][line]
                self.AllQuestionsList.clear()
                self.AllQuestionsList.addItems([x["question"] for x in allQDict["list"]])
                self.allQuestions = allQDict["list"]
                with open("questions.JSON", "w") as fw:
                    fw.write(json.dumps(allQDict, indent=2))

        elif whatToDo == "removeFromNew":
            if self.NewTestList.currentItem() is None:
                return

            selectedLines = [x.row() for x in self.NewTestList.selectedIndexes()]
            selectedLines.sort(reverse=True) # will delete from the end
            for line in selectedLines:
                del self.newQuestions[line]
            self.NewTestList.clear()
            self.NewTestList.addItems([x["question"] for x in self.newQuestions])

        elif whatToDo == "saveNewTest":
            if self.newTestFileName == "":
                dialog = QtWidgets.QFileDialog()
                self.newTestFileName = dialog.getSaveFileName(None, 'Uložit jako')[0]

            with open(self.newTestFileName + ".json", "w") as fw:
                saveDic = {"list": self.newQuestions}
                fw.write(json.dumps(saveDic, indent=2))

    def showResultAnswer(self):
        index = 0
        if self.ResultsListWidget.currentRow() is not None:
            index = self.ResultsListWidget.currentRow()
        questions = self.openedTest["list"]
        self.ResultsQuestion.setText(questions[index]["question"])
        self.ResultsYourAnswer.setText(questions[index]["answers"][self.answers[index]])
        self.ResultsCorrectAnswer.setText(questions[index]["answers"][int(questions[index]["correctAns"])])
        if questions[index]["imagePath"] is not None:
            pixmap = QtGui.QPixmap(questions[index]["imagePath"])
            self.ResultsImage.setPixmap(pixmap.scaled(250, 250))
        else:
            self.ResultsImage.clear()

    def changePage(self, pageName):
        if pageName == "Test":
            self.stackedWidget.setCurrentWidget(self.TestPage)
            self.currentIndex = 0
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
        elif pageName == "CreateNew":
            self.stackedWidget.setCurrentWidget(self.CreateNewPage)
            self.newQuestionHandler("init")

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
            if len(itemText) == 30:
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
        allTests = glob.glob("*.json")
        if "history.json" in allTests:
            allTests.remove("history.json")
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
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mainWin()
    ui.setupUi(Form)
    ui.initWindow()
    Form.show()
    sys.exit(app.exec_())
