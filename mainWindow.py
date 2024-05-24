#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:55:38 2024

@author: scottmiller
"""


import os
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QTransform, QIcon, QPalette, QColor, QPainter
from hexPushbutton import HexPushButton
from Board import Board
from PyQt5.QtCore import Qt, QSize


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.hexButtons = []                   # set up these global variables before the initUI
        self.stationButtons = []
        self.trainButtons = []
        self.companyButtons = []
        self.trainList = []
        self.lastHex = 0
        self.currentStation = "stn 100"
        self.currentCompany = 0
        self.stationClicked = False
        self.stationPlaced = False
        self.currentTile = [0,0,0]
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
        self.tileDictionary = {
            1:"t1", 2:"t2", 3:"t3", 4:"t4", 7:"t7", 8:"t8", 9:"t9", 
            14:"t14", 15:"t15", 16:"t16", 18:"t18", 19:"t19",
            20:"t20", 23:"t23", 24:"t24", 25:"t25", 26:"t26", 27:"t27", 28:"t28", 29:"t29", 
            39:"t39", 40:"t40", 41:"t41", 42:"t42", 43:"t43", 44:"t44", 45:"t45", 46:"t46", 47:"t47",
            53:"t53", 54:"t54,", 55:"t55", 56:"t56", 57:"t57", 58:"t58", 59:"t59",
            61:"t61", 62:"t62", 63:"t63", 64:"t64", 65:"t65", 66:"t66", 67:"t67", 68:"t68", 69:"t69", 70:"t70"
            }
        
        # this is the number of stations per company
        self.stationList = [2,3,3,4,3,4,2,4]
        
        # make the QPushbuttons for the hexes
        for row in range(11):
            for col in range(12):
                if map[row][col] == 1:
                    shift = 0
                    if (row+1) % 2 == 0:
                        shift = 50
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
                    button = HexPushButton(name, self, self.board, self)         
                    button.resize(117,116)
                    button.move(-25+(100*col)+shift, 13+(87 * row))
                    self.hexButtons.append(button) 
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
        
        for i in range(9):
            self.trainList.append([1,1,1,1])
        
        # set up company QPushbuttons
        companyList = ["BMlogo", "BOlogo", "COlogo", "CPlogo", "Elogo", "NYClogo", "NYNHlogo", "PRRlogo"]
        for i in range(8):
            cName = str("co" + str(i+1))
            cButton = QPushButton(cName, self)
            cButton.setObjectName(cName)
            cButton.setGeometry(1245, 125*i, 125,125)
            cButton.clicked.connect(self.companyButtonClicked)
            cButton.setText("")
            cButton.setStyleSheet("border: none;")
            self.companyButtons.append(cButton)
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
        if tileNumber > 0:                                      # if it is a new hex
            self.currentTile = [tileNumber, location, angle]    # variable to know if any tiles have been clicked and what the tile info is
            print("tileNumber = " + str(tileNumber))
            tileName = self.tileDictionary[tileNumber]
            icon = QIcon(self.getImage(tileName))
        else:                                                   # if it is an old icon that needs to be made blank
            icon = QIcon()
        hex_widget = self.hexButtons[location]
        if angle > 0:
            transform = QTransform()
            transform.rotate(angle * 60)
            original_pixmap = icon.pixmap(QSize(115, 115))
            rotated_pixmap = original_pixmap.transformed(transform, Qt.SmoothTransformation)
            final_pixmap = QPixmap(QSize(115, 115))                         # new QPixmap with the desired size
            final_pixmap.fill(Qt.transparent)                               # transparent color
            xOffset = (final_pixmap.width() - rotated_pixmap.width()) / 2   # draw the rotated pixmap to center it in the final pixmap
            yOffset = (final_pixmap.height() - rotated_pixmap.height()) / 2
            painter = QPainter(final_pixmap)                                # Draw the rotated pixmap onto the final pixmap
            painter.drawPixmap(int(xOffset), int(yOffset), rotated_pixmap)
            painter.end() 
            hex_widget.setIcon(QIcon(final_pixmap))
            hex_widget.setIconSize(QSize(115, 115))                         # Set the size of the icon
        else:
            hex_widget.setIcon(icon)
            hex_widget.setIconSize(QSize(115, 115))                         # Set the size of the icon
        
        
    def stationButtonClicked(self):
        buttonName = self.sender().objectName()                 # find out which station was clicked
        print("Station: ", buttonName)
        print("Current station " + self.currentStation)
        if int(self.currentCompany) == int(buttonName[4]) + 1:      # check to see if the button clicked matches the current company
            self.stationClicked = True
            stationSlot = 100
            print(self.currentStation[4:])
            if int(self.currentStation[4:]) < 100:
                stationSlot = self.findStation()
                print("Station slot = " + str(stationSlot))
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                self.stationButtons[stationSlot].setIcon(icon)
            self.currentStation = buttonName
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
        buttonName = self.sender().objectName()
        number = buttonName[1:]
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
        if activeTrain > 1:
            self.colorTrains(company, slot, card, activeTrain)
            
            
    def companyButtonClicked(self):
        buttonName = self.sender().objectName()
        company = int(buttonName[-1])
        print("Current Company = " + str(company))
        if company != self.currentCompany:
            self.currentCompany = company
            # this is where the code to let the board know that the tile has been finalized would go
            self.lastHex = 0
            if self.stationClicked == True and self.stationPlaced == False:  # if a station was clicked and not placed then replace it
                stationSlot = self.findStation()
                print("Station slot = " + str(stationSlot))
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                self.stationButtons[stationSlot].setIcon(icon)
            if self.currentTile != [0,0,0]:
                print("tile = " + str(self.currentTile[0]))
                print ("location =  " + str(self.currentTile[1]))
                print("angle = " + str(self.currentTile[2]))
                
                self.board.updateHexWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2])
                self.currentTile = [0,0,0]
                
    def colorTrains(self, company, slot, card, tValue):
        colorList = [(255,0,0,64), (0,255,0,64), (0,0,255,64),(255,255,255,64)]
        train_button = self.trainButtons[slot]
        icon = QIcon(self.getImage("train" + str(tValue)))               # get the new card icon
        color = QColor(*colorList[card])
        pixmap = icon.pixmap(icon.availableSizes()[0])                   # Get the first available size
        # Blend the color with the icon pixmap
        pixmap_with_color = QPixmap(pixmap.size())
        pixmap_with_color.fill(Qt.transparent)                           # Fill pixmap with transparency
        painter = QPainter(pixmap_with_color)
        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)  # Blend mode
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceAtop)  # Apply color atop the pixmap
        painter.fillRect(pixmap.rect(), color)
        painter.end()
        train_button.setIcon(QIcon(pixmap_with_color))                   # Set the modified pixmap with color to the button


    def colorTiles(self, tileNumber, location, angle, train): 
        colorList = [(255,255,0,128), (240,227,25,200), (240,227,25,200),(240,227,25,200)]
        color = QColor(*colorList[train])
        tileName = self.tileDictionary[tileNumber]
        icon = QIcon(self.getImage(tileName))
        hex_widget = self.hexButtons[location]
        # Blend the color with the icon pixmap       
        pixmap = icon.pixmap(icon.availableSizes()[0])                   # Get the first available size
        pixmap_with_color = QPixmap(pixmap.size())
        pixmap_with_color.fill(Qt.transparent)                           # Fill pixmap with transparency
        painter = QPainter(pixmap_with_color)
        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)  # Blend mode
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceAtop)  # Apply color atop the pixmap
        painter.fillRect(pixmap.rect(), color)
        painter.end()
        
        hex_widget.setIcon(QIcon(pixmap_with_color)) 
        hex_widget.setIconSize(QSize(115, 115))                         # Set the size of the icon
        
        