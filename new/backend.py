from cProfile import label
from functools import partial
from pprint import pprint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel
import numpy as np

def move_right(image_object,units):
    image_object.label.move(image_object.label.x() + units,image_object.label.y())
def move_left(image_object,units):
    image_object.label.move(image_object.label.x() + units,image_object.label.y())

def move_up(image_object,units):
     image_object.label.move(image_object.label.x(),image_object.label.y() -units)

def move_down(image_object,units):
     image_object.label.move(image_object.label.x(),image_object.label.y() +units)


    

class target_object:
    def __init__(self,image_path):
        self.pixmap = QPixmap(image_path)
        self.pixmap = self.pixmap.scaled(QtCore.QSize(100, 100))
        # self.label.move(1000, 1000)
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

    def rotate(self,image_object, degree):
       # MUST LOOK INTO THIS 
        pixmap_rotated = self.pixmap.transformed(QtGui.QTransform().rotate(degree),QtCore.Qt.SmoothTransformation)
        image_object.label.setPixmap(pixmap_rotated) # set rotated pixmap into your QLabel
       # self.setx_and_y(image_object.label.x(),image_object.label.y())
       # return image_object


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





