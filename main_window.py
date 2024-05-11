#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:55:38 2024

@author: scottmiller
"""


import os
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QTransform
from hex_pushbutton import HexPushButton
from PyQt5.QtCore import Qt
from rotatable_label import RotatableLabel



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.hex_Buttons = []
        self.initUI()
        self.lastTile = 0
        
        
    def initUI(self):
        self.setGeometry(0, 0, 1692, 1000) #1245
        self.setWindowTitle('1830 Game')

        
        # Load map image
        current_dir = os.path.dirname(os.path.abspath(__file__))
        map_relative_path = os.path.join("resources", "map1830.jpg")
        map_image_path = os.path.join(current_dir, map_relative_path)
        map_pixmap = QPixmap(map_image_path)
        map_label = QLabel(self)
        map_label.setGeometry(0,0,1245,1000)
        map_label.setPixmap(map_pixmap)

        
        
        # Load sidebar image
        sidebar_relative_path = os.path.join("resources", "sideBar.jpg")
        sidebar_image_path = os.path.join(current_dir, sidebar_relative_path)
        sidebar_pixmap = QPixmap(sidebar_image_path)
        sidebar_label = QLabel(self)
        sidebar_label.setGeometry(1245,0,447,1000)
        sidebar_label.setPixmap(sidebar_pixmap)

        

               
        # This a a list of all valid hexes that can be clicked
        map = [
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,1,1,1,0],
            [0,0,0,1,1,1,1,0,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,1,1,1,1,1,1,1],
            [0,1,0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,1,0,0],
            [1,1,1,1,1,0,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,0,0,0,0]
            ]

        # this is a list of all tile names from 1 to 70 in ascending order
        self.tileList = [
            "t1", "t2", "t3", "t4", "t7", "t8", "t9", 
            "t14", "t15", "t16", "t18", "t19",
            "t20", "t23", "t24", "t25", "t26", "t27", "t28", "t29", 
            "t39", "t40", "t41", 't42', "t43", "t44", "t45", "t46", "t47",
            "t53", "t54,", "t55", "t56", "t57", "t58", "t59",
            "t61", "t62", "t63", "t64", "t65", "t66", "t67", "t68", "t69", "t70"
            ]
        
        
        buttonSize = 121
        buttonRatio = buttonSize / 120
        
        self.labels = []                        # list of all rotatable laels
        
        # make the labels
        for i in range(1,12):
            for j in range(1,13):
                label = RotatableLabel(self)
                if i % 2 == 0:
                    label.setGeometry(-123+(j*100)+50,-74+(i*87),115,115)
                else:
                    label.setGeometry(-123+(j*100),-74+(i*87),115,115)
                self.labels.append(label)
                
        # make the QPushbuttons for the hexes
        for row in range(11):
            for col in range(12):
                if map[row][col] == 1:
                    shift = 0
                    if (row+1) % 2 == 0:
                        shift = 52
                    if row+1 < 10:
                        sRow = "0" +str(row+1)
                    else:
                        sRow = str(row+1)
                    if (row+1) % 2 == 0:
                        mCol = (col+1)*2
                    else:
                        mCol = 1 + (col*2)
                    if mCol < 10:
                        sCol = "0" + str(mCol)
                    else:
                        sCol = str(mCol)
                    name = sRow + sCol
                    button = HexPushButton(name, self, self)
                    self.hex_Buttons.append(button)
                    
                    
                    button.resize(buttonSize, int(buttonSize*.96))
                    button.move(-26+(int(100 * buttonRatio) * col)+shift, 14+(int(90 * buttonRatio*.96)) * row)

        self.show()
        
    # method for getting the image files
    def getImage(self, imageName):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join("resources", imageName)
        image_path = os.path.join(current_dir, relative_path)
        pixmap = QPixmap(image_path)
        return pixmap
    
    # method for getting and displaying tiles gotten from theBoard
    def displayTile(self, tileNumber, location, angle):
        if tileNumber > 0:
            tileName = self.tileList[tileNumber]
            pixmap = self.getImage(tileName)
        else:
            pixmap = QPixmap() 
            print("Pixmap set to None")
        label_widget = self.labels[location - 1]
        label_widget.setPixmap(pixmap)
        label_widget.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        label_widget.rotate(angle)
        
     

        
