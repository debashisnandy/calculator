from GUI_Home.MyCalUi import *

strValue= ""
ansWer = ""
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda :self.button_cliked("3"))
        self.pushButton_4.clicked.connect(lambda: self.button_cliked("1"))
        self.pushButton_3.clicked.connect(lambda: self.button_cliked("2"))
        self.pushButton_7.clicked.connect(lambda: self.button_cliked("4"))
        self.pushButton_8.clicked.connect(lambda: self.button_cliked("5"))
        self.pushButton_6.clicked.connect(lambda: self.button_cliked("6"))
        self.pushButton_12.clicked.connect(lambda: self.button_cliked("7"))
        self.pushButton_11.clicked.connect(lambda: self.button_cliked("8"))
        self.pushButton_10.clicked.connect(lambda: self.button_cliked("9"))
        self.pushButton_2.clicked.connect(lambda: self.button_cliked("+"))
        self.pushButton_5.clicked.connect(lambda: self.button_cliked("-"))
        self.pushButton_9.clicked.connect(lambda: self.button_cliked("*"))
        self.pushButton_15.clicked.connect(lambda: self.button_cliked("/"))
        self.pushButton_16.clicked.connect(lambda: self.button_cliked("%"))
        self.pushButton_18.clicked.connect(lambda: self.button_cliked("."))
        self.pushButton_19.clicked.connect(lambda: self.button_cliked("0"))
        self.pushButton_13.clicked.connect(self.change_tosomthing)
        self.pushButton_17.clicked.connect(self.Show_answer)
        self.pushButton_14.clicked.connect(self.clear_all)


    def clear_all(self):
        global strValue,ansWer
        strValue , ansWer = "",""
        self.lineEdit.setText("")

    def button_cliked(self, mystrValue):
        global strValue

        if not strValue:
            self.lineEdit.setText(mystrValue)
            strValue=mystrValue
        else:
            strValue = strValue + mystrValue
            self.lineEdit.setText(strValue)

    def Show_answer(self):
        global strValue, ansWer
        try:
            strValue = self.lineEdit.text()
            if '%' in strValue:
                s = strValue.split('%')
                y = s[0]
                i = len(y)
                x = " "

                while i > -1:

                    if y[i - 1] == '+' or y[i - 1] == '-' or y[i - 1] == '*' or y[i - 1] == '/':
                        z = y[:i - 1]
                        break
                    x = x + y[i - 1]
                    i -= 1
                x = x[::-1]
                z = str(eval(z))
                z = "(" + z + "/100)*" + x
                ansWer = str(eval(z))
            else:
                myValue = eval(str(strValue))
                ansWer = str(myValue)
            strValue = ansWer
            self.textBrowser.setText("Answer:- " + ansWer)
        except:
            self.lineEdit.setText("You can not divided any number by 0")

    def change_tosomthing(self):

        global ansWer,strValue
        try:
            myval = int(self.lineEdit.text())
            if myval<0:
                myval = abs(myval)
                strValue = str(myval)
                ansWer= strValue
                self.lineEdit.setText(strValue)
            else:
                myval = int("-" + self.lineEdit.text())
                strValue = str(myval)
                ansWer = strValue
                self.lineEdit.setText(strValue)
        except:
            self.lineEdit.setText(strValue)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    Height = rect.height()
    Width = rect.width()
    window = MyApp()
    window.setWindowTitle("Image Editor")
    window.show()
    sys.exit(app.exec_())