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
    def __init__(self):
        self.dict = {}
    
    def addVariable(self, varName, val):
        self.dict[varName] = val
    
    def getVariable(self, varName):
        return self.dict.get(varName)
    
    def setVariable(self, varName, value):
        self.dict[varName] = value
    
    def remVariable(self, varName):
        temp = self.getVariable(varName)

        if (temp != None):
            del self.dict[varName]

class operators:
    def add(self, a, b):
        return int(a) + int(b)
    
    def sub(self, a,b):
        return int(a) - int(b)
    
    def div(self, a, b):
        if (int(b) != 0):
            return int(a)/int(b)
        else:
            return "dividing by 0!"
    
    def mul(self,a,b):
        return int(a) * int(b)
        

    
class loop:

    def __init__(self,button_list):
        self.run_stack = []
        self.list_loop_buttons = []
        self.button_list = button_list
    def add_loop_in_stack(self):
        self.list_loop_buttons = self.list_loop_buttons[::-1]
        print(self.list_loop_buttons)
        x = self.list_loop_buttons[0].split()
        val = int(x[1])
        print('val of loop:'+ str(val))
        for j in range(val):  
            for i in range(1,len(self.list_loop_buttons)-1):
                self.run_stack.append(self.list_loop_buttons[i])
        self.list_loop_buttons = []        
        
    def exec_run_stack(self):
        count = 0
        for i in range(len(self.run_stack)):
            x = self.run_stack[i].split()
            if x[0] !='Loop':
                #print("exec")
                count = count + 1
            if x[0]=='Move':
                pass

        print(count)

    def add_button_list_in_run_stack(self):
        for i in  range(len(self.button_list)):
            x = self.button_list[i].split()
            print(x)
            if x[0] !='End':
                self.run_stack.append(self.button_list[i])
            else:
                self.list_loop_buttons.append(self.button_list[i])
                while(len(self.list_loop_buttons)!=0):
                    line = self.run_stack.pop()
                    p = line.split()
                    if(p[0]=='Loop'):
                        self.list_loop_buttons.append(line)
                        self.add_loop_in_stack()
                        break
                    else:
                        self.list_loop_buttons.append(line)
                        continue 
