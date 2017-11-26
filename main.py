
from PyQt5 import QtCore, QtGui, QtWidgets
from mainWindow import Ui_Form


class mainWindow(Ui_Form):
    pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
