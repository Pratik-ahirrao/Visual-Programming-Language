from cProfile import label
from functools import partial
from pprint import pprint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel

class target_object:
    def __init__(self,image_path):
        self.pixmap = QPixmap(image_path)
        self.pixmap = self.pixmap.scaled(QtCore.QSize(100, 100))
        self.initOrt = 0
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
    def setx(self,x):
        self.x = x 
    def sety(self,y):
        self.y = y
    def setx_and_y(self,x,y):
        self.x = x
        self.y = y
    def rotate(self, degree):
       # MUST LOOK INTO THIS 
       self.initOrt += degree
       pixmap_rotated = self.pixmap.transformed(QtGui.QTransform().rotate(self.initOrt),QtCore.Qt.SmoothTransformation)
       self.label.setPixmap(pixmap_rotated) # set rotated pixmap into your QLabel
       # self.setx_and_y(self.label.x(),self.label.y())
       # return self
    def move_right(self, units):
        self.label.move(self.label.x() + units,self.label.y())
    def move_left(self,units):
        self.label.move(self.label.x() + units,self.label.y())

    def move_up(self,units):
        self.label.move(self.label.x(),self.label.y() -units)

    def move_down(self,units):
        self.label.move(self.label.x(),self.label.y() +units)


class loop:
    def loop_val(list_of_buttons):
        pass



class variable:
    def __init__(self,var):
        self.var = var
        
    def getvariable(self):
        return self.var
        
    def incr(self,x):
        self.var = self.var + x





