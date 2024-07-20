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
        self.cityButtons = []
        self.oneCityIndex = 0
        self.twoCityIndex = 0
        self.endTurn = True
        
        self.lastHex = 0
        self.currentStation = "stn 100"
        self.currentStationNumber = 0
        self.currentCompany = 9
        self.stationClicked = False
        self.stationPlaced = False
        self.currentTile = [0,0,0]
        self.initUI()
        self.lastcityButton = ""
        
    def initUI(self):
        self.setGeometry(0, 0, 1692, 1000) #1245
        self.setWindowTitle('1830 Game Helper')
  
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
            53:"t53", 54:"t54", 55:"t55", 56:"t56", 57:"t57", 58:"t58", 59:"t59",
            61:"t61", 62:"t62", 63:"t63", 64:"t64", 65:"t65", 66:"t66", 67:"t67", 68:"t68", 69:"t69", 
            70:"t70", 80:"t80", 81:"t81", 82:"t82", 83:"t83"
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
                    location = str(sRow + sCol)
                    self.checkForCity(location, col, row, shift)     # check to see if the hex has a city on it
        pad = 0 
        
        # set uo side bar train and company buttons
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
        
        for i in range(10):
            self.trainList.append([1,1,1,1])
        
        # set up sude bar company QPushbuttons
        companyList = ["BMlogo", "BOlogo", "COlogo", "CPlogo", "Elogo", "NYClogo", "NYNHlogo", "PRRlogo"]
        for i in range(8):
            cName = str("co" + str(i+1))
            cButton = QPushButton(cName, self)
            cButton.setObjectName(cName)
            cButton.setGeometry(1237, 125*i, 125,125)
            cButton.clicked.connect(self.companyButtonClicked)
            cButton.setText("")
            cButton.setStyleSheet("border: none;")
            cButton.setIconSize(QSize(125,125))
            self.companyButtons.append(cButton)
        self.show()
        
        
    def checkForCity(self, location, col, row, shift):
        oneCityAdj = [(0,0), (2,0), (0,0), (0,0), (0,0), (2,-2), (5,-5), (2,-1), (2,-2), (5,-5), (0,5), (-15,-15)]  
        hex = self.board.findHexName(location)
        if hex and hex.city_count == 1:
            print("city found at: " + str(location))
            if hex.rr_start == 100:
                for i in range(2):
                    if i == 1:
                        adjX = oneCityAdj[self.oneCityIndex][0]
                        adjY = oneCityAdj[self.oneCityIndex][1]
                    else:
                        adjX = 0
                        adjY = 0
                    cityName = str("city" + str(location) + str(i))
                    cityButton = QPushButton(cityName, self)
                    cityButton.setObjectName(cityName)
                    cityButton.setGeometry(12+(100*col)+shift+adjX, 53+(87 * row)+ adjY, 40, 40)
                    cityButton.clicked.connect(self.cityButtonClicked)    
                    cityButton.setText("")  
                    if i == 0:
                        cityButton.setStyleSheet("border: 2px solid red;")
                    else:
                        cityButton.setStyleSheet("border: 2px solid blue;")
                    icon = QIcon()
                    cityButton.setIconSize(cityButton.size())
                    cityButton.setIcon(icon)
                    if i == 0:
                        cityButton.setEnabled(False)
                    self.cityButtons.append(cityButton)
                    if i > 0:
                        self.oneCityIndex +=1
        twoCityAdj =[[(-26,16),(-19,-24)], [(-28,5),(15,16)], [(-23,3),(16,-25)], [(-2,17),(18,-25)], [(-12,21),(17,-30)]]
        if hex and hex.city_count == 2:
            print(f"2 cities at {location}")
            for i in range(2):
                adjX = twoCityAdj[self.twoCityIndex][i][0]
                adjY = twoCityAdj[self.twoCityIndex][i][1]
                cityName = str("city" + str(location)+ str(i))
                print(cityName)
                cityButton = QPushButton(cityName, self)
                cityButton.setObjectName(cityName)
                cityButton.setGeometry(12+(100*col)+shift+adjX, 53+(87 * row)+ adjY, 40, 40)
                cityButton.clicked.connect(self.cityButtonClicked)    
                cityButton.setText("")   
                cityButton.setStyleSheet("border: 2px solid red;")
                icon = QIcon()
                cityButton.setIconSize(cityButton.size())
                cityButton.setIcon(icon)
                self.cityButtons.append(cityButton)
                if i > 0:
                    self.twoCityIndex +=1
    
    # method for getting the image files
    def getImage(self, imageName):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join("resources", imageName)
        image_path = os.path.join(current_dir, relative_path)
        pixmap = QPixmap(image_path)
        return pixmap
    
    
    # method for getting and displaying tiles gotten from theBoard
    def displayTile(self, tileNumber, location, angle):
        self.resetCityButton()
        if tileNumber > 0:                                      # if it is a new hex
            self.currentTile = [tileNumber, location, angle]    # variable to know if any tiles have been clicked and what the tile info is
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
        buttonName = self.sender().objectName()                     # find out which station was clicked
        print("Station: ", buttonName)
        print("Current station " + self.currentStation)
        if int(self.currentCompany) == int(buttonName[4]) + 1:      # check to see if the button clicked matches the current company
            self.stationClicked = True
            stationSlot = 100
            print(self.currentStation[4:])
            if int(self.currentStation[4:]) < 100:                  # this lets stations in the same company reset if another station is clicked
                stationSlot = self.findStation()
                print("Station slot = " + str(stationSlot))
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                if self.lastcityButton != "": 
                    self.stationButtons[stationSlot].setIcon(icon)      # resets a station back to its original icon
                    icon = QIcon()
                    stationSlot = self.findCityButton(self.lastcityButton)
                    self.cityButtons[stationSlot].setIcon(icon)
                    self.currentStation = "stn 100"
                    self.stationClicked = False
                    self.lastcityButton = ""
                    return
            self.currentStation = buttonName
            stationSlot = self.findStation()
            self.stationButtons[stationSlot].setIcon(QIcon())
        
        
    def findStation(self):
        i = 0
        for stationTest in self.stationButtons:
            if stationTest.objectName() == self.currentStation:
                stationSlot = i
            i += 1
        #print("station slot = " + str(stationSlot))         
        return stationSlot
        
        
    def trainButtonClicked(self):
        buttonName = self.sender().objectName()
        number = buttonName[1:]
        company = int(number[:1])
        card = int(number[1:])
        if company == self.currentCompany - 1:
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
            self.board.largestTrain = 1
            for i in range(8):
                for j in range(4):
                    if self.trainList[i][j] > self.board.largestTrain:
                        self.board.largestTrain = self.trainList[i][j]
            print("Largest Train = " + str(self.board.largestTrain))
            self.endTurn = True         # this forced the method to choose new hex rather than same hex since there may be upgrade tiles now available
            
            
    def companyButtonClicked(self):
        buttonName = self.sender().objectName()
        print("Company button: " + buttonName)
        pixmap =QIcon(self.getImage(buttonName))    
        company = int(buttonName[-1])
        print("Current Company = " + str(company))
        if company != self.currentCompany:
            for cButton in self.companyButtons:
                icon = QIcon ()
                cButton.setIcon(icon)
            self.sender().setIcon(pixmap)
            self.currentCompany = company
            
            # this is where the code to let the board know that the tile has been finalized would go
            self.lastcityButton = ""                               # set the station token back to blank as the "turn" is ended
            self.lastHex = -1                                   # set to -1 not 0 so that if hex 0 is clicked it will register as a new hex and not be rejected
            self.endTurn = True
            
            if self.stationClicked == True and self.stationPlaced == False:  # if a station was clicked and not placed then replace it
                stationSlot = self.findStation()
                print("Station slot = " + str(stationSlot))
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                self.stationButtons[stationSlot].setIcon(icon)
                self.currentStation = "stn 100"
            if self.currentTile != [0,0,0]:
                print("tile = " + str(self.currentTile[0]))
                print ("location =  " + str(self.currentTile[1]))
                print("angle = " + str(self.currentTile[2]))
                station = int(self.currentStation[4:])
                print("station = " + str(station))
                self.board.updateHexWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], self.currentStationNumber, station)
                self.currentTile = [0,0,0]
            self.currentStation = "stn 100"
            
                
    def cityButtonClicked(self, company):
        buttonName = self.sender().objectName()
        print("buttonName: " + str(buttonName))
        print("lastcityButton =  " + str(self.lastcityButton))
        if self.lastcityButton != "":                           # used to blank out a station icon if another station is clicked before finalizing with company
            self.resetCityButton()
        if int(self.currentStation[4:]) < 100:                  # if a station icon was clicked set the station token to that icon
            hexName = buttonName[4:8]
            hex = self.board.findHexName(hexName)               # get the hex for the loaction of the station
            hexName = hex.hex_name                              # find the name of the hex
            curTile = self.currentTile[1]                       # get the current tile's numeric value (ie 58)
            curHex = self.board.hexDictionary[curTile]          # use the dictionary to find the corresponding name
            if curHex == hexName:                               # if the two match then the tile we just selected is the one with the station on it
                self.setCityButton(buttonName)                     # if so set the icon, this method section is needed since the hex's tile has not been set yet            
            if hex.hexTile:                                     # if there's a tile here
                for hList in hex.entryExitStation:              # check to see if the hex's station has been set yet
                    if int(hList[3]) == 100:                    # if 100 then no station has been placed yet, prevents overwritting previous stations
                        self.setCityButton(buttonName)
                
                        
    def setCityButton(self, buttonName):                        # method for setting the icon of a station token
        if self.currentStation != "stn 100":
            stationSlot = self.findCityButton(buttonName)
            icon = QIcon(self.getImage(str("s" + self.currentStation[4])))
            self.cityButtons[stationSlot].setIcon(icon)
            self.lastcityButton = buttonName                     # used to reset this station t0 blank if another station is clicked before finalized
            self.stationPlaced = True
           
            
    def resetCityButton(self):
        print("in reset token")
        icon = QIcon()
        if self.lastcityButton != "":
            stationSlot = self.findCityButton(self.lastcityButton)
            self.cityButtons[stationSlot].setIcon(icon)
            self.stationPlaced = False
            self.lastcityButton = ""
            
            
    def activateSecondCity(self, hex, tileNumber):
        print(f"Hex {hex} and tileNumber {tileNumber}")
        print(f"hexPB name = {hex.name}")
        city0 = self.findCityObj(str("city" + hex.name + "0"))
        print(f" ******* {city0}")
        city0.setEnabled(True)
        city1 = self.findCityObj(str("city" + hex.name + "1"))
        hexCol =int( hex.name[-2:])-1
        hexRow = int(hex.name[:2])-1
        print(f"col =  {hexCol} row = {hexRow}")
        shift = 0
        if (hexRow) % 2 == 0:
            shift = 50
        city0.setGeometry(12+(50*hexCol)+shift, 33+(87 * hexRow), 40, 40)
        city1.setGeometry(12+(50*hexCol)+shift, 73+(87 * hexRow), 40, 40)
        
        
                        
    def findCityButton(self, cityButton):
        i = 0
        stattionSlot = 0
        for stationTest in self.cityButtons:
            if stationTest.objectName() == cityButton:
                stationSlot = i
            i += 1
        return stationSlot
    
    
    def findCityObj(self, cityName):
        for city in self.cityButtons:
            if city.objectName() == cityName:
                return city
                
    
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
        
        