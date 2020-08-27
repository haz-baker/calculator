# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_layout_v2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from calc_functions import *

class Ui_Dialog(object):

    #defining variables
    op = None
    operator = ""
    num1 = ""
    num2 = ""
    numb = []


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(216, 215)
        Dialog.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"color: rgb(255, 255, 255);")

        self.Button_7 = QtWidgets.QPushButton(Dialog)
        self.Button_7.setGeometry(QtCore.QRect(10, 50, 51, 41))
        self.Button_7.setObjectName("Button_7")

        self.Button_8 = QtWidgets.QPushButton(Dialog)
        self.Button_8.setGeometry(QtCore.QRect(60, 50, 51, 41))
        self.Button_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.Button_8.setObjectName("Button_8")

        self.Button_9 = QtWidgets.QPushButton(Dialog)
        self.Button_9.setGeometry(QtCore.QRect(110, 50, 51, 41))
        self.Button_9.setObjectName("Button_9")
        self.Button_4 = QtWidgets.QPushButton(Dialog)
        self.Button_4.setGeometry(QtCore.QRect(10, 90, 51, 41))
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(Dialog)
        self.Button_5.setGeometry(QtCore.QRect(60, 90, 51, 41))
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(Dialog)
        self.Button_6.setGeometry(QtCore.QRect(110, 90, 51, 41))
        self.Button_6.setObjectName("Button_6")
        self.Button_1 = QtWidgets.QPushButton(Dialog)
        self.Button_1.setGeometry(QtCore.QRect(10, 130, 51, 41))
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(Dialog)
        self.Button_2.setGeometry(QtCore.QRect(60, 130, 51, 41))
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(Dialog)
        self.Button_3.setGeometry(QtCore.QRect(110, 130, 51, 41))
        self.Button_3.setObjectName("Button_3")
        self.Button_0 = QtWidgets.QPushButton(Dialog)
        self.Button_0.setGeometry(QtCore.QRect(10, 170, 51, 41))
        self.Button_0.setObjectName("Button_0")
        self.Button_equals = QtWidgets.QPushButton(Dialog)
        self.Button_equals.setGeometry(QtCore.QRect(60, 170, 101, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Button_equals.setPalette(palette)
        self.Button_equals.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_equals.setObjectName("Button_equals")
        self.Button_add = QtWidgets.QPushButton(Dialog)
        self.Button_add.setGeometry(QtCore.QRect(160, 170, 51, 41))
        self.Button_add.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_add.setObjectName("Button_add")
        self.Button_sub = QtWidgets.QPushButton(Dialog)
        self.Button_sub.setGeometry(QtCore.QRect(160, 130, 51, 41))
        self.Button_sub.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_sub.setObjectName("Button_sub")
        self.Button_divide = QtWidgets.QPushButton(Dialog)
        self.Button_divide.setGeometry(QtCore.QRect(160, 90, 51, 41))
        self.Button_divide.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_divide.setObjectName("Button_divide")
        self.Button_multi = QtWidgets.QPushButton(Dialog)
        self.Button_multi.setGeometry(QtCore.QRect(160, 50, 51, 41))
        self.Button_multi.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_multi.setObjectName("Button_multi")
        self.Button_clear = QtWidgets.QPushButton(Dialog)
        self.Button_clear.setGeometry(QtCore.QRect(160, 10, 51, 41))
        self.Button_clear.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_clear.setObjectName("Button_clear")
        self.display = QtWidgets.QLabel(Dialog)
        self.display.setGeometry(QtCore.QRect(10, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.display.setFont(font)
        self.display.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.display.setObjectName("display")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # all clicked commands for each button connecting to the commands for calculator functions
        self.Button_clear.clicked.connect(self.clear)
        self.Button_0.clicked.connect(self.press_0)
        self.Button_1.clicked.connect(self.press_1)
        self.Button_2.clicked.connect(self.press_2)
        self.Button_3.clicked.connect(self.press_3)
        self.Button_4.clicked.connect(self.press_4)
        self.Button_5.clicked.connect(self.press_5)
        self.Button_6.clicked.connect(self.press_6)
        self.Button_7.clicked.connect(self.press_7)
        self.Button_8.clicked.connect(self.press_8)
        self.Button_9.clicked.connect(self.press_9)
        self.Button_add.clicked.connect(self.plus)
        self.Button_sub.clicked.connect(self.minus)
        self.Button_multi.clicked.connect(self.times)
        self.Button_divide.clicked.connect(self.divide)
        self.Button_equals.clicked.connect(self.sum)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_7.setText(_translate("Dialog", "7"))
        self.Button_8.setText(_translate("Dialog", "8"))
        self.Button_9.setText(_translate("Dialog", "9"))
        self.Button_4.setText(_translate("Dialog", "4"))
        self.Button_5.setText(_translate("Dialog", "5"))
        self.Button_6.setText(_translate("Dialog", "6"))
        self.Button_1.setText(_translate("Dialog", "1"))
        self.Button_2.setText(_translate("Dialog", "2"))
        self.Button_3.setText(_translate("Dialog", "3"))
        self.Button_0.setText(_translate("Dialog", "0"))
        self.Button_equals.setText(_translate("Dialog", "="))
        self.Button_add.setText(_translate("Dialog", "+"))
        self.Button_sub.setText(_translate("Dialog", "-"))
        self.Button_divide.setText(_translate("Dialog", "/"))
        self.Button_multi.setText(_translate("Dialog", "*"))
        self.Button_clear.setText(_translate("Dialog", "clear"))
        self.display.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:28pt;\">0</span></p></body></html>"))


    def clear(self): # clear command for the calculator display
        self.display.setText("0") # sets display to 0

    def press_0 (self): # connecting function for button 0
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "0", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.numb2 = numbers2(self.op, "0",self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_1 (self): # connecting function for button 1
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "1", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers2(self.op, "1", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_2 (self):  # connecting function for button 2
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "2", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers2(self.op, "2", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_3 (self):  # connecting function for button 3
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "3", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers2(self.op, "3", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_4 (self):  # connecting function for button 4
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "4", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers1(self.op, "4", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_5 (self):  # connecting function for button 5
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "5", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers1(self.op, "5",self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_6 (self):  # connecting function for button 6
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "6", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers1(self.op, "6", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_7 (self):  # connecting function for button 7
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "7", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers1(self.op, "7", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_8 (self):  # connecting function for button 8
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "8", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers1(self.op, "8", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added

    def press_9 (self):  # connecting function for button 9
        # if statements to know if to add input to num1 or num2 variable
        if self.op == None:
            self.num1 = numbers1(self.op, "9", self.num1) # calls function to add to num1
            self.display.setText(self.num1) # sets display to numbers currently being added

        elif self.op!= None:
            self.num2 = numbers1(self.op, "9", self.num2) # calls function to add to num2
            self.display.setText(self.num2) # sets display to numbers currently being added


    def plus (self): # additon function
        self.operator = "+" # setting operator function to '+'
        self.op = 1 # setting op check variable to true

    def minus (self): # subtraction function
        self.operator = "-" # setting operator function to '-'
        self.op = 1 # setting op check variable to true

    def times (self): # multiplication function
        self.operator = "*" # setting operator function to '*'
        self.op = 1 # setting op check variable to true

    def divide (self): # division function
        self.operator = "/" # setting operator function to '/'
        self.op = 1 # setting op check variable to true

    def sum (self):
        if self.operator == "*":
            self.answer = times(self.num1, self.num2)


        elif self.operator == "/":
            self.answer = divide(self.num1, self.num2)


        elif self.operator == "+":
            self.answer = add(self.num1, self.num2)


        elif self.operator == "-":
            self.answer = sub(self.num1, self.num2)


        self.display.setText(str(self.answer))
        self.operator = None
        self.op = None
        self.num1 = ""
        self.num2 = ""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
