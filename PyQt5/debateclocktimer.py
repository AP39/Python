"""
A GUI python program that can be used as a clock for classroom or club debate timing.
Functionality includes multiple time choices, a warning bell at 15 seconds left,
and a final bell when the time is finished.
"""

import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, \
    QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout, QPushButton
from playsound import playsound

temp = 0

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.lcd = QLCDNumber(self)
        self.lcd.display(temp)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(240)
        self.slider.valueChanged.connect(self.lcd.display)

        button1 = QPushButton('1 Min', self)
        button1.move(130,150)

        button2 = QPushButton('1:30 Min', self)
        button2.move(260,150)

        button3 = QPushButton('2 Min', self)
        button3.move(385,150)

        button4 = QPushButton('2:30 Min', self)
        button4.move(130,200)

        button5 = QPushButton('3 Min', self)
        button5.move(260,200)

        button6 = QPushButton('3:30 Min', self)
        button6.move(385,200)

        btn4 = QPushButton("Reset", self)
        btn4.move(135, 610)
        btn4.resize(350,64)

        btn2 = QPushButton("Exit", self)
        btn2.move(260, 710)

        btn3 = QPushButton("Ring Warning Bell", self)
        btn3.move(135, 410)
        btn3.resize(350,64)

        btn5 = QPushButton("Ring Final Bell", self)
        btn5.move(135, 510)
        btn5.resize(350,64)

        btn1 = QPushButton("Start", self)
        btn1.move(135, 310)
        btn1.resize(350,64)

        btn5.clicked.connect(self.button5Clicked)
        btn4.clicked.connect(self.button4Clicked)
        btn2.clicked.connect(self.button2Clicked)
        btn3.clicked.connect(self.button3Clicked)
        btn1.clicked.connect(self.button1Clicked)
        button1.clicked.connect(self.on_click1)
        button2.clicked.connect(self.on_click2)
        button3.clicked.connect(self.on_click3)
        button4.clicked.connect(self.on_click4)
        button5.clicked.connect(self.on_click5)
        button6.clicked.connect(self.on_click6)

        hbox = QHBoxLayout()
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle("Alex's Debate Clock")
        self.resize(1920, 950)

    def on_click1(self):
        temp = 60
        self.lcd.display(temp)

    def on_click2(self):
        temp = 90
        self.lcd.display(temp)

    def on_click3(self):
        temp = 120
        self.lcd.display(temp)

    def on_click4(self):
        temp = 150
        self.lcd.display(temp)

    def on_click5(self):
        temp = 180
        self.lcd.display(temp)

    def on_click6(self):
        temp = 210
        self.lcd.display(temp)

    def button4Clicked(self):
        self.lcd.display(temp)

    def button5Clicked(self):
        playsound("endbell.mp3")

    def button2Clicked(self):
        exit(0)

    def button3Clicked(self):
        playsound("bell.mp3")

    def button1Clicked(self):
        self.tick_timer()

    def tick_timer(self):
        lcd_value = self.lcd.value()
        if lcd_value > 1:
            self.lcd.display(lcd_value - 1)
            QTimer().singleShot(1000, self.tick_timer)
            if lcd_value == 16:
                playsound("bell.mp3")
        if lcd_value == 1:
            playsound("endbell.mp3")
            self.lcd.display(temp)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
