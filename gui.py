# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from cProfile import label
from functools import partial
from pprint import pprint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel

class Ui_MainWindow(object):
    def __init__(self):
        self.buttons = []
        self.label = QtWidgets.QLabel()
        self.speed = 15
        self.is_removed = 0
        self.is_run = 0
        self.is_edited = 0
        self.num_buttons =0
        self.dict = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        _translate = QtCore.QCoreApplication.translate

        # Area 0

        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 196, 409))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.runButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_12)
        self.runButton.setObjectName("runButton")
        self.runButton.setText(_translate("MainWindow", "Run"))
        #self.runButton.setStyleSheet("background-color : yellow")
        self.runButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )
        self.verticalLayout_6.addWidget(self.runButton)

        self.editButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_12)
        self.editButton.setObjectName("editButton")
        self.editButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )
        self.editButton.setText(_translate("MainWindow", "Edit"))

        self.verticalLayout_6.addWidget(self.editButton)

        self.removeButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_12)
        self.removeButton.setObjectName("removeButton")
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.removeButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")
        self.removeButton.clicked.connect(self.clickme)
        self.verticalLayout_6.addWidget(self.removeButton)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_12)
        self.horizontalLayout_8.addWidget(self.scrollArea_4)

        

        self.ready_to_select = QtWidgets.QPushButton(self.scrollAreaWidgetContents_12)
        self.ready_to_select.setObjectName("ready to select")
        self.ready_to_select.setText(_translate("MainWindow", "Ready to select"))
        self.ready_to_select.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")
        self.ready_to_select.clicked.connect(self.ready_to_connect)
        self.verticalLayout_6.addWidget(self.ready_to_select)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_12)
        self.horizontalLayout_8.addWidget(self.scrollArea_4)

        # Area 1

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 196, 409))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonClicks)
        self.pushButton.clicked.connect(self.move_image)
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_17.setObjectName("pushButton_3")
        self.pushButton_17.clicked.connect(self.buttonClicks)
        self.verticalLayout_4.addWidget(self.pushButton_17)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.buttonClicks)
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.buttonClicks)
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.buttonClicks)
        self.verticalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.buttonClicks)
        self.verticalLayout_4.addWidget(self.pushButton_10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_9)
        self.horizontalLayout_8.addWidget(self.scrollArea)

        # Area 2

        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 197, 409))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_10)
        self.horizontalLayout_8.addWidget(self.scrollArea_2)

        # Area 3
        

        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 196, 409))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.pixmap = QPixmap('images.jpg')
        self.pixmap = self.pixmap.scaled(QtCore.QSize(100, 100))
        # self.label.move(1000, 1000)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        print(self.label.x())
        print(self.label.y())
        self.verticalLayout_6.addWidget(self.label)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_11)
        self.horizontalLayout_8.addWidget(self.scrollArea_3)

        # Main Window

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 24))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Move"))
        self.pushButton_17.setText(_translate("MainWindow", "Loop"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))

    def buttonClicks(self):
       
        
        
        but = QtWidgets.QPushButton(str(self.num_buttons),self.scrollAreaWidgetContents_10)
        but.setObjectName(str(self.num_buttons))
        but.setStyleSheet("QPushButton""{""background-color : lightblue;""}")
        self.dict[self.num_buttons] = but
        self.num_buttons+=1
        self.buttons.append(but)
        length = len(self.buttons)
  
        #self.buttons[length - 1].setObjectName("pushButton" + str(length + 20))
        self.verticalLayout_5.addWidget(but)

    def move_image(self):
        # self.label.move(self.label.x() + 10, self.label.y() + 10)
        self.label.move(0, self.label.x() + 10)
        print(self.label.x())
        print(self.label.y())

    def to_run_blocks():
        return

    def select_blocks_to_run(self,button_name):
        if self.dict[button_name].styleSheet() == "QPushButton{background-color : lightblue;}":
            self.dict[button_name].setStyleSheet("QPushButton{background-color : green;}")
        elif self.dict[button_name].styleSheet() == "QPushButton{background-color : green;}":
            self.dict[button_name].setStyleSheet("QPushButton{background-color : lightblue;}")
    def ready_to_connect(self):
        if self.ready_to_select.styleSheet() == "QPushButton{background-color : lightblue;}":
            self.ready_to_select.setStyleSheet("QPushButton""{""background-color : green;}")
            for key in self.dict:
                self.dict[key].clicked.connect(partial(self.select_blocks_to_run,key))
        elif self.ready_to_select.styleSheet() == "QPushButton{background-color : green;}":
            self.ready_to_select.setStyleSheet("QPushButton""{""background-color : lightblue;}")
            for key in self.dict:
                self.dict[key].disconnect()
                self.dict[key].setStyleSheet("QPushButton""{""background-color : lightblue;}")
    def donothing(self):
        return                   

    def clickme(self):
        if self.is_removed == 0:
            self.removeButton.setStyleSheet("QPushButton{background-color : green;}")
            self.is_removed = 1
            print(self.removeButton.styleSheet())
        else:
            self.removeButton.setStyleSheet("QPushButton{background-color : lightblue;}")
            self.is_removed = 0

                
        print("pressed")                     

        # printing pressed       





    def keyPressEvent(self, event):
  
        # get the current co-ordinates of the label
        # X Co-ordinate
        x = self.label.x()
  
        # Y Co-ordinate
        y = self.label.y()
  
        # if up arrow key is pressed
        if event.key() == Qt.Key_Up:
            self.label.move(x, y - self.speed)
  
        # if down arrow key is pressed
        elif event.key() == Qt.Key_Down:
            self.label.move(x, y + self.speed)
  
        # if left arrow key is pressed
        elif event.key() == Qt.Key_Left:
            self.label.move(x - self.speed, y)
  
        # if down arrow key is pressed
        elif event.key() == Qt.Key_Right:
            self.label.move(x + self.speed, y)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
