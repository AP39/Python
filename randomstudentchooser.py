""" This app utilizes PyQt5 and allows a user to choose a random number within an input range.
    The user can sort numbers by all, evens or odds.
"""


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QShortcut
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import time

student_nums = []
students_picked = []

class Picker(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
#Defines the window and button configs
        self.textbox = QLineEdit(self)
        self.textbox.move(160, 50)
        self.textbox.resize(100,40)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Type number of students here.  Then click all, evens or odds.')
        self.nameLabel.move(40, 10)
        self.nameLabel.resize(350,40)

        btn1 = QPushButton("Choose Random Student", self)
        btn1.move(35, 190)
        btn1.resize(350,64)

        btn2 = QPushButton("Exit", self)
        btn2.move(160, 380)

        btn3 = QPushButton("Reset Student List", self)
        btn3.move(35, 270)
        btn3.resize(350,64)

        button1 = QPushButton('All', self)
        button1.move(30,110)

        button2 = QPushButton('Evens', self)
        button2.move(160,110)

        button3 = QPushButton('Odds', self)
        button3.move(285,110)

        btn1.clicked.connect(self.button1Clicked)
        btn2.clicked.connect(self.button2Clicked)
        btn3.clicked.connect(self.button3Clicked)
        button1.clicked.connect(self.on_click1)
        button2.clicked.connect(self.on_click2)
        button3.clicked.connect(self.on_click3)

        self.statusBar()

        self.setGeometry(450, 450, 420, 450)
        self.setWindowTitle("Ace's Student Chooser")
        self.show()
#sets actions for buttons
    def button1Clicked(self):

        if len(student_nums) > 0:
            choice = random.choice(student_nums)
            student_nums.remove(choice)
            students_picked.append(choice)
            sender = self.sender()
            self.statusBar().showMessage(f"The next student is student number {choice}")
            time.sleep(1.6)

            if len(students_picked) <= 10:
                self.statusBar().showMessage(f"Students Picked {students_picked}")

            else:
                length = len(students_picked)
                self.statusBar().showMessage(f"Students Picked {students_picked[length-10:length]}")

        else:
            alert = QMessageBox()
            alert.setWindowTitle("Ace Says...")
            alert.setText("All students have been chosen!")
            alert.exec_()


    def button2Clicked(self):
        exit(0)

    def button3Clicked(self):

        while len(students_picked) > 0:
            x = students_picked.pop(0)
            student_nums.append(x)
        self.statusBar().showMessage(f"All students are now available!")

    def on_click1(self):
        textboxValue = self.textbox.text()
        buttonCondition = "all"
        try:
            c1 = int(textboxValue)
            temp = 1
            while len(students_picked) > 0:
                trash = students_picked.pop(0)
            while len(student_nums) > 0:
                trash = student_nums.pop(0)
            while temp <= c1:
                student_nums.append(temp)
                temp += 1
            if buttonCondition == "evens" or buttonCondition == "odds":
                self.statusBar().showMessage(f"Ready to randomize {c1} students by {buttonCondition}!")
            else:
                self.statusBar().showMessage(f"Ready to randomize {c1} students!")
        except ValueError:
            self.statusBar().showMessage("Please enter a valid number")
            pass

    def on_click2(self):
        textboxValue = self.textbox.text()
        buttonCondition = "evens"
        try:
            c1 = int(textboxValue)
            temp = 1
            while len(students_picked) > 0:
                trash = students_picked.pop(0)
            while len(student_nums) > 0:
                trash = student_nums.pop(0)
            while temp <= c1:
                if temp % 2 == 0:
                    student_nums.append(temp)
                    temp += 1
                else:
                    temp += 1
            if buttonCondition == "evens" or buttonCondition == "odds":
                self.statusBar().showMessage(f"Ready to randomize {c1} students by {buttonCondition}!")
            else:
                self.statusBar().showMessage(f"Ready to randomize {c1} students!")
        except ValueError:
            self.statusBar().showMessage("Please enter a valid number")
            pass

    def on_click3(self):
        textboxValue = self.textbox.text()
        buttonCondition = "odds"
        try:
            c1 = int(textboxValue)
            temp = 1
            while len(students_picked) > 0:
                trash = students_picked.pop(0)
            while len(student_nums) > 0:
                trash = student_nums.pop(0)
            while temp <= c1:
                if temp % 2 != 0:
                    student_nums.append(temp)
                    temp += 1
                else:
                    temp += 1
            if buttonCondition == "evens" or buttonCondition == "odds":
                self.statusBar().showMessage(f"Ready to randomize {c1} students by {buttonCondition}!")
            else:
                self.statusBar().showMessage(f"Ready to randomize {c1} students!")
        except ValueError:
            self.statusBar().showMessage("Please enter a valid number")
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Picker()
    sys.exit(app.exec_())
