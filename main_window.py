#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:55:38 2024

@author: scottmiller
"""


import os
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QTransform, QIcon, QPalette, QColor, QPainter
from hex_pushbutton import HexPushButton
from PyQt5.QtCore import Qt, QSize
from rotatable_label import RotatableLabel



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.hex_Buttons = []
        self.stationButtons = []
        self.trainButtons = []
        self.trainList = []
        self.lastTile = 0
        self.currentStation = "stn 100"
        self.initUI()
        
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
        
        # this is the number of stations per company
        self.stationList = [2,3,3,4,3,4,2,4]
        
        
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
        pad = 0           
        for row in range(16):
            for col in range(2):
                if row%2 == 0 and col == 0:     # if the first row and colum then pad down by 4
                    pad = pad + 4
                    if row > 8:                 # after the fourth company pad an additional 2
                        pad += 2
                # station buttons
                company = row//2
                numberOfStations = self.stationList[company]
                if numberOfStations >= (2*(row%2)) + col + 1:
                    sName = str("stn " + str(company) + str(col+(2*(row%2))))
                    sButton = QPushButton(sName, self)
                    sButton.setObjectName(sName)
                    sButton.setGeometry(1360 + (col*60),pad+(row * 60), 60, 60)
                    sButton.clicked.connect(self.stationButtonClicked)
                    sButton.setText("")
                    sButton.setStyleSheet("border: none;")
                    icon = QIcon(self.getImage(str("s" + str(row//2))))
                    sButton.setIconSize(button.size())
                    sButton.setIcon(icon)
                    self.stationButtons.append(sButton)
                # train buttons
                tName = str("t" + str(row//2) + str(col+(2*(row%2))))
                tButton = QPushButton(tName, self)
                tButton.setObjectName(tName)
                tButton.setGeometry(1480 + (col*107),pad+(row * 60), 100, 60)
                tButton.clicked.connect(self.trainButtonClicked)
                tButton.setText("")
                tButton.setStyleSheet("border: none;")
                icon = QIcon(self.getImage("train1"))
                tButton.setIconSize(button.size())
                tButton.setIcon(icon)
                self.trainButtons.append(tButton)
        self.show()
        for i in range(8):
            self.trainList.append([1,1,1,1])
            
        
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
        
    def stationButtonClicked(self):
        button_name = self.sender().objectName()        # find out which station was clicked
        print("Station: ", button_name)
        print("Current station " + self.currentStation)
        stationSlot = 100
        print(self.currentStation[4:])
        if int(self.currentStation[4:]) < 100:
            stationSlot = self.findStation()
            print("Station slot = " + str(stationSlot))
            company = self.currentStation[4]
            icon = QIcon(self.getImage(str("s" + company)))
            self.stationButtons[stationSlot].setIcon(icon)
        self.currentStation = button_name
        stationSlot = self.findStation()
        self.stationButtons[stationSlot].setIcon(QIcon())
        
    def findStation(self):
        i = 0
        for stationTest in self.stationButtons:
            #print(stationTest.objectName())
            if stationTest.objectName() == self.currentStation:
                stationSlot = i
            i += 1
        return stationSlot
        
        
    def trainButtonClicked(self):
        button_name = self.sender().objectName()
        number = button_name[1:]
        company = int(number[:1])
        card = int(number[1:])
        trainList = self.trainList[company]             # get the train list for the company
        activeTrain = trainList[card]                   # get the clicked card for that company and
        activeTrain = activeTrain + 1                   # increment the train value
        if activeTrain > 7: 
            activeTrain = 1
 
        self.trainList[company][card] = activeTrain                         # set the value in that company train list for export
        slot = (company * 4) + card                                         # find which slot in the trainbuttons is active
        icon = QIcon(self.getImage("train" + str(activeTrain)))             # get the new card icon
        self.trainButtons[slot].setIcon(icon)                               # update the pushbutton icon
        if activeTrain == 3:
            train_button = self.trainButtons[slot]
            icon = QIcon(self.getImage("train" + str(activeTrain)))         # get the new card icon
            color = QColor(255, 0, 0, 64)  # Red color
            pixmap = icon.pixmap(icon.availableSizes()[0])                  # Get the first available size
            # Blend the color with the icon pixmap
            pixmap_with_color = QPixmap(pixmap.size())
            pixmap_with_color.fill(Qt.transparent)                          # Fill pixmap with transparency
            painter = QPainter(pixmap_with_color)
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)  # Blend mode
            painter.drawPixmap(0, 0, pixmap)
            painter.setCompositionMode(QPainter.CompositionMode_SourceAtop)  # Apply color atop the pixmap
            painter.fillRect(pixmap.rect(), color)
            painter.end()
            train_button.setIcon(QIcon(pixmap_with_color))                  # Set the modified pixmap with color to the button
