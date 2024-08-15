#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:55:38 2024
@author: scottmiller
"""

import os
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QTransform, QIcon, QColor, QPainter
from Board import Board
from MouseClickFilter import MouseClickFilter
from CityButton import CityButton
from PyQt5.QtCore import Qt, QSize

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.tileHexagList = []
        self.stationMarkers = []
        self.stationMarkerUsed = []
        self.trainButtons = []
        self.companyButtons = []
        self.trainList = []
        self.cityButtons = []
        self.currentTile = [0,0,0]                  # tile number, name, angle
        self.currentStation = "stn 9"
        self.currentCompany = 9
        self.oneCityIndex = 0
        self.twoCityIndex = 0
        self.endTurn = True
        self.currentCityButton = ""
        self.currentTHName = ""
        self.currentNumberOfCities = 0
        self.stationClicked = False
        self.stationPlaced = False
        self.startUp = True
        self.currentTH = None
        self.initUI()
        self.mouse_filter = MouseClickFilter(self)
        self.installEventFilter(self.mouse_filter)
        self.mouse_filter.mouseClicked.connect(self.onMouseClick)
 
        
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

        # This a a list of all valid hexages that can be clicked
        map = [
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,1,1,1,0],
            [0,0,0,1,1,1,1,0,1,1,1,1],
            [2,1,1,1,1,1,2,1,1,1,1,0],
            [0,1,1,1,0,1,1,1,1,1,1,1],
            [0,1,0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,1,0,0],
            [1,1,1,1,1,0,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,2,0,0,0,0]
            ]

        # this is a list of all tile names from 1 to 70 in ascending order
        self.tileDictionary = {
            1:"t1",   2:"t2",   3:"t3",   4:"t4",   7:"t7",   8:"t8",   9:"t9", 
            14:"t14", 15:"t15", 16:"t16", 18:"t18", 19:"t19",
            20:"t20", 23:"t23", 24:"t24", 25:"t25", 26:"t26", 27:"t27", 28:"t28", 29:"t29", 
            39:"t39", 40:"t40", 41:"t41", 42:"t42", 43:"t43", 44:"t44", 45:"t45", 46:"t46", 47:"t47",
            53:"t53", 54:"t54", 55:"t55", 56:"t56", 57:"t57", 58:"t58", 59:"t59",
            61:"t61", 62:"t62", 63:"t63", 64:"t64", 65:"t65", 66:"t66", 67:"t67", 68:"t68", 69:"t69", 
            70:"t70", 80:"t80", 81:"t81", 82:"t82", 83:"t83"
            }

        self.posDiagList = [
                ["1004"],
                ["0903", "1004", "1006"], 
                ["0802", "0903", "0905", "1006", "1008"],
                ["0802", "0804", "0905", "0907", "1008", "1010"],
                ["0703", "0804", "0806", "0907", "0909", "1010", "1012"],
                ["0703", "0705", "0806", "0808", "0909", "0911", "1012", "1014"],
                ["0604", "0705", "0707", "0808", "0810", "0911", "0913", "1014"],
                ["0503", "0604", "0606", "0707", "0709", "0810", "0913", "0915"],
                ["0503", "0905", "0608", "0709", "0711", "0814", "0915", "0917"],
                ["0404", "0505", "0608", "0610", "0711", "0713", "0814", "0816", "0917"],
                ["0404", "0406", "0507", "0610", "0612", "0713", "0715", "0816", "0818"],
                ["0406", "0408", "0511", "0612", "0614", "0715", "0717", "0818"],
                ["0307", "0408", "0410", "0511", "0513", "0614", "0616", "0717", "0719"],
                ["0307", "0309", "0410", "0412", "0513", "0515", "0616", "0618", "0719"],
                ["0309", "0311", "0412", "0515", "0517", "0618", "0620"],
                ["0210", "0311", "0313", "0416", "0517", "0519", "0620", "0622"],
                ["0210", "0212", "0313", "0416", "0418", "0519", "0521", "0622"],
                ["0212", "0214", "0317", "0418", "0420", "0521", "0523"],
                ["0214", "0216", "0317", "0319", "0420", "0422", "0523"],
                ["0216", "0218", "0319", "0321", "0422"],
                ["0218", "0220", "0321", "0323"],
                ["0220", "0222", "0323"],
                ["0222"]
            ]
        
        self.negDiagList = [
                ["1014", "0917"],
                ["1012", "1014", "0915", "0917", "0818"],
                ["1010", "1012", "0913", "0915", "0816", "0818", "0719", "0622"],
                ["1008", "1010", "0911", "0913", "0814", "0816", "0717", "0719", "0620", "0622", "0523"],
                ["1006", "1008", "0909", "0911", "0814", "0715", "0717", "0618", "0620", "0521", "0523"],
                ["1004", "1006", "0907", "0909", "0810", "0713", "0715", "0616", "0618", "0519", "0521", "0422"],
                ["1004", "0905", "0907", "0808", "0810", "0711", "0713", "0614", "0616", "0517", "0519", "0420", "0422", "0323"],
                ["0903", "0905", "0806", "0808", "0709", "0713", "0612", "0614", "0515", "0517", "0418", "0420", "0321", "0323"],
                ["0903", "0804", "0806", "0707", "0709", "0610", "0612", "0513", "0515", "0416", "0418", "0319", "0321", "0222"],
                ["0802", "0804", "0705", "0707", "0608", "0610", "0511", "0513", "0416", "0317", "0319", "0220", "0222"],
                ["0802", "0703", "0705", "0608", "0511", "0412", "0317", "0218", "0220"],
                ["0703", "0604", "0507", "0410", "0412", "0313", "0216", "0218"],
                ["0604", "0505", "0507", "0408", "0410", "0311", "0313", "0214", "0216"],
                ["0503", "0505", "0406", "0408", "0309", "0311", "0212", "0214"],
                ["0503", "0404", "0406", "0307", "0309", "0210", "0212"],
                ["0404", "0307", "0210"]
            ]
        
        # slope, intercept for the heagon diagonal lines, needed because the artwork is not uniform across the map
        self.negDiagLine = [
                [-0.569,    1302],
                [-0.590,	1259],
                [-0.586,	1199],
                [-0.584,	1138],
                [-0.586,	1082],
                [-0.581,	1020],
                [-0.582,	962],
                [-0.584,	905],
                [-0.584,	848],
                [-0.583,	789],
                [-0.582,	730],
                [-0.583,	674],
                [-0.580,	614],
                [-0.580,	556],
                [-0.579,	499],
                [-0.581,	441],
                [-0.582,    383]
                ]
        
        
        self.posDiagLine = [
                [0.577,	748],
                [0.562,	694],
                [0.566,	634],
                [0.570,	578],
                [0.567,	520],
                [0.570,	460],
                [0.575,	402],
                [0.570,	347],
                [0.573,	289],
                [0.570,	232],
                [0.571,	173],
                [0.565,	119],
                [0.568,	58],
                [0.566,	0],
                [0.570,	-56],
                [0.569,	-112],
                [0.567,	-168],
                [0.569,	-228],
                [0.571,	-286],
                [0.564,	-337],
                [0.566,	-395],
                [0.563,	-451],
                [0.585,	-532]      
            ]
        
        # this is the number of stations per company
        self.stationList = [2,3,3,4,3,4,2,4]
        
        # make the Labels for the hexages
        for row in range(11):
            for col in range(12):
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
                
                if map[row][col] > 0:                   
                    name = sRow + sCol
                    tileHexag = QLabel(self)  
                    #tileHexag.setStyleSheet("background-color: transparent; border: 2px solid red; padding: 0;")
                    tileHexag.setObjectName(name)
                    if row < 6:
                        colSize = 100
                    else:
                        colSize = 101
                    tileHexag.setGeometry(-20 + (colSize * col) + shift, 13+(87 * row), colSize, 115)
                    self.tileHexagList.append(tileHexag)
                    self.checkForCity(name)             # check to see if the hexag has a city on it
                #if map[row][col] == 2:
                    #self.checkForCity(name)              # check to see if the hexag has a city on it

        pad = 0 
        
        for button in self.cityButtons:
            hexagName = button.objectName()
            print(f"buttonName = {button.objectName()}")
            name = hexagName[4:8]
            hexag = self.board.findHexagByName(name)
            numberOfCities = hexag.city_count
            self.displayCity(name, name, numberOfCities, True)

        print("(((((((((((()))))))))))))")
                   
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
                    sName = str("stn " + str(company+1) + str(col+(2*(row%2))))
                    sButton = QPushButton(sName, self)
                    sButton.setObjectName(sName)
                    sButton.setGeometry(1360 + (col*60),pad+(row * 60), 60, 60)
                    sButton.clicked.connect(self.stationMarkerClicked)
                    sButton.setText("")
                    sButton.setStyleSheet("border: none;")
                    icon = QIcon(self.getImage(str("s" + str((row//2)+1))))
                    sButton.setIconSize(QSize(60,60))
                    sButton.setIcon(icon)
                    self.stationMarkers.append(sButton)
                    self.stationMarkerUsed.append([sName, 0])
                    
                # train buttons
                tName = str("t" + str((row//2)+1) + str(col+(2*(row%2))))
                tButton = QPushButton(tName, self)
                tButton.setObjectName(tName)
                tButton.setGeometry(1480 + (col*107),pad+(row * 60), 100, 60)
                tButton.clicked.connect(self.trainButtonClicked)
                tButton.setText("")
                tButton.setStyleSheet("border: none;")
                icon = QIcon(self.getImage("train1"))
                tButton.setIconSize(QSize(100,60))
                tButton.setIcon(icon)
                self.trainButtons.append(tButton)    
        for i in range(10):
            self.trainList.append([1,1,1,1])
        
        # set up side bar company QPushbuttons
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
        specialCity = [["city01190",4],["city06060",3],["city08120",8]]
        for city in specialCity:
            cityButton = CityButton(city[0], self, False, True, city[1])
            self.board.companyStations.append([city[1], city[0][4:8]])
            self.cityButtons.append(cityButton)
            
        self.show()
        self.startUp = False
        self.currentTHName = ""


    # used to show if a hexag has a city on it    
    def checkForCity(self, name):
        hexag = self.board.findHexagByName(name)
        if hexag and hexag.city_count > 0:
            print("city found at: " + str(name))
            #if hexag.rr_start == 100:
            start = hexag.city_count
            if hexag.hexag_name == "0719":
                start = 3
            if start == 2:
                start = 1
            for i in range(start, -1, -1):
                cityName = str("city" + str(name) + str(i))
                cityButton = CityButton(cityName, self, False, False, name, "100", self)
                cityButton.setObjectName(cityName)
                cityButton.clicked.connect(self.cityButtonClicked)  
                cityButton.setText("")
                cityButton.setStyleSheet("QPushButton { color: transparent; border: 2px solid red; }")
                icon = QIcon()
                cityButton.setIconSize(QSize (38,38))
                cityButton.setIcon(icon)
                
                if i == 0:
                    if hexag.rr_start < 100:
                        cityButton.setCompany(hexag.rr_start)
                        print(f"RR start on {name} of company {hexag.rr_start}")
                        cityButton.setCitySet(True)
                    if name == "0523" or name == "0719" or name == "0915" or name == "0519":
                        cityButton.setCitySet(True) 
                    if name == "1115" or name == "0402" or name == "0414":
                        cityButton.setActive(True)
                if i == 1 and name == "0719":
                    cityButton.setActive(True)
                self.cityButtons.append(cityButton)     
            
                
    def onMouseClick(self):
        # Get the mouse coordinates
        x = self.mouse_filter.getLocalX()
        y = self.mouse_filter.getLocalY()
        posDiag = 0
        negDiag = 0
        for i in range(24):
            if 31 + (i*50) > x:
                col = i
                break
        for i in range(23):              #print(self.posDiagLine[i])  
            diag = ((self.posDiagLine[i][0]) * x) + self.posDiagLine[i][1]
            if  diag  < y:
                posDiag= i+1
                break
        for i in range(17):
            diag = ((self.negDiagLine[i][0]) * x) + self.negDiagLine[i][1]
            if diag < y:
                negDiag = i
                break
        if posDiag > 0:
            posList = self.posDiagList[posDiag-1]
        if negDiag > 0:
            negList = self.negDiagList[negDiag-1]
        if posDiag > 0 and negDiag > 0:
            for pSlot in posList:
                for nSlot in negList:
                    if pSlot == nSlot:
                        if int(pSlot[-2:]) == col or int(pSlot[-2:]) == col+1:
                            print(f"tileHexag {nSlot} was clicked ")
                            clickedTileHexag = nSlot
                            for th in self.tileHexagList:
                                thn = th.objectName()
                                if thn == clickedTileHexag:
                                    tileHexagClicked = th
                                    print()
                                    break
                            print(f"clickedTileHexag = {clickedTileHexag} and self.currentTHName = {self.currentTHName}")
                            if clickedTileHexag != self.currentTHName or self.endTurn:
                                self.newTileHexagClicked(tileHexagClicked)
                                self.endTurn = False
                            else:
                                self.sameTileHexagClicked(tileHexagClicked)
                        break
                    
                    
    def newTileHexagClicked(self, tileHexagClicked):
        print(f"******** New Location {tileHexagClicked.objectName()} currentTHName = {self.currentTHName}")
        # check if the player clicked on a second tile this turn, if so we need to either blank out the previous tile or reset it to its original tile
        if self.currentTHName != "":                                        # this case there was a previous tile, -1 because there is a '0' hexag
            oldTH = self.currentTH
            oldTHName = self.currentTHName                                  # restore the last hexag's tile
            locationFirst = int(oldTHName[:2])                              # parsing out the tuple for board to use
            locationSecond = int(oldTHName[2:])
            boardLocation = (locationFirst, locationSecond)
            currentHexag = self.board.findHexagTuple(boardLocation)
            print(f"new tileHexagClicked reset {currentHexag.hexag_name}")
            if currentHexag:
                self.displayTile(currentHexag.hexagTile, currentHexag.angle, oldTH) # tile number, location,angle
            else:
                self.displayTile(0, 0, oldTH)                               # set the previous hexag to blank  
        self.currentTH = tileHexagClicked
        name = tileHexagClicked.objectName()
        self.currentTHName = name                                           # set the currentHexag to this new location
        company = self.currentCompany
        trainList = self.trainList[company]
        locationFirst = int(name[:2])                                       # parsing out the tuple for board to use
        locationSecond = int(name[2:])
        boardLocation = (locationFirst, locationSecond)
        print(f"name {name} boardLocation {boardLocation}")
        self.board.tileList = self.board.checkForPlayableTile(boardLocation)    # ask board for a list of playable tiles to display 
        self.board.tileListIndex = 0
        print(f"the board tile list {self.board.tileList}")
        if self.board.tileList:
            tileNumber = self.board.tileList[0][0]
            angle = self.board.tileList[0][1]
            self.displayTile(tileNumber, angle, tileHexagClicked)    
        
        
    def sameTileHexagClicked(self, tileHexagClicked):
        print("******** Same Location")
        if self.board.tileList:
            self.board.tileListIndex +=1
            if self.board.tileListIndex >= len(self.board.tileList):
                self.board.tileListIndex = 0
            ind = self.board.tileListIndex
            self.displayTile(self.board.tileList[ind][0], self.board.tileList[ind][1], tileHexagClicked)        
                        

    # method for getting the image files
    def getImage(self, imageName):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join("resources", imageName)
        image_path = os.path.join(current_dir, relative_path)
        pixmap = QPixmap(image_path)
        return pixmap
    
    
    # method for getting and displaying tiles gotten from board
    def displayTile(self, tileNumber, angle, tileHexagClicked):
        name = tileHexagClicked.objectName() if tileHexagClicked else ""
        numberOfCities = -1   
        print(f"\ntileNumber: {tileNumber}, name: {name}, angle: {angle}")
        if tileNumber > 0:  # Display tile
            self.currentTile = [tileNumber, name, angle]
            tileName = self.tileDictionary.get(tileNumber, "")
            tile = self.board.allTilesLookUp(tileNumber)
            if tile:
                numberOfCities = tile.city_count
            pixmap = QPixmap(self.getImage(tileName))
        else:  # Clear the tile
            pixmap = QPixmap()
            numberOfCities = 0
    
        # If angle > 0, apply rotation
        if angle > 0 and not pixmap.isNull():
            transform = QTransform()
            transform.rotate(angle * 60)
            rotated_pixmap = pixmap.transformed(transform, Qt.SmoothTransformation)
            final_pixmap = QPixmap(101, 115)
            final_pixmap.fill(Qt.transparent)
            xOffset = (final_pixmap.width() - rotated_pixmap.width()) / 2
            yOffset = (final_pixmap.height() - rotated_pixmap.height()) / 2
            painter = QPainter(final_pixmap)
            painter.drawPixmap(int(xOffset), int(yOffset), rotated_pixmap)
            painter.end()
            pixmap = final_pixmap
    
        # Scale the pixmap and set it on the QLabel
        pixmap = pixmap.scaled(115, 115, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        tileHexagClicked.setPixmap(pixmap)
    
        # Display city information if applicable
        if tileHexagClicked and numberOfCities > -1:
            self.displayCity(name, tileHexagClicked, numberOfCities, False)
        
        
    # called if a station QPushButton is clicked
    def stationMarkerClicked(self):
        buttonName = self.sender().objectName()                                 # find out which station was clicked
        print("Station: ", buttonName)
        print("Current station " + self.currentStation)
        print(f"Button Name {buttonName}")
        if self.stationClicked == True and buttonName != self.currentStation:
            return
        if int(self.currentCompany) == int(buttonName[4]):                      # check to see if the button clicked matches the current company
            for slot in self.stationMarkerUsed:                                 # blocks fro reusing the same station twice
                if slot[0] == buttonName and slot[1] == 1:
                    return
            self.stationClicked = True
            stationSlot = 100
            if int(self.currentStation[4]) < 9:                                # this lets stations in the same company reset if another station is clicked
                stationSlot = self.findStation()
                print("Station slot = " + str(stationSlot))
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                if self.currentCityButton == "": 
                    self.stationMarkers[stationSlot].setIcon(icon)              # resets a station back to its original icon
                    icon = QIcon()
                    self.cityButtons[stationSlot].setIcon(icon)
                    self.currentStation = "stn 9"
                    self.stationClicked = False  
                    return        
                if self.currentStation == buttonName:
                    print("******In attempt to reset station button")
                    self.stationMarkers[stationSlot].setIcon(icon) 
                    stationSlot = self.findCityButton(self.currentCityButton)
                    cityObj = self.cityButtons[stationSlot]
                    hexagName = cityObj.name[4:8]
                    print(f"HexagName = {hexagName}")
                    hexagObj = self.board.findHexagByName(hexagName)
                    hexagTileNumber = hexagObj.hexagTile
                    if hexagTileNumber:
                        hexagTile = self.board.allTilesLookUp(hexagTileNumber)
                    else:
                        hexagTile = self.board.allTilesLookUp(self.currentTile[0])
                    numberOfCities = hexagTile.city_count
                    print(f"Tile Number = {hexagTileNumber} and number of cities = {numberOfCities}")
                    if numberOfCities == 0:
                        if hexagTileNumber == 83 or hexagTileNumber == 82:                     # this is a "00" of NY hex and has b/w markers
                            if int(cityObj.name[8]) == 0:
                                icon = QIcon(self.getImage("w"))
                            else:
                                icon = QIcon(self.getImage("b"))
                        else:
                            icon = QIcon()
                    elif numberOfCities == 1:
                        if hexagName == "0402" or hexagName =="0719" or hexagName == "1115":
                            icon = QIcon()
                        else:           
                            icon = QIcon(self.getImage("greyDot"))
                    elif numberOfCities == 2:
                        icon = QIcon(self.getImage("greyDot"))
                    else:
                        if int(cityObj.name[8]) % 2 == 0:
                            icon = QIcon(self.getImage("w"))
                        else:
                            icon = QIcon(self.getImage("b"))
                    cityObj.setIcon(icon)
                    self.currentCityButton = ""
                    self.currentStation = "stn 9"
                    self.stationClicked = False
                    return      
            self.currentStation = buttonName
            stationSlot = self.findStation()
            self.stationMarkers[stationSlot].setIcon(QIcon())
        
        
    # helper method to find a station from the stationMarkers list   
    def findStation(self):
        print(f" findstation {self.currentStation}")
        i = 0
        for stationTest in self.stationMarkers:
            if stationTest.objectName() == self.currentStation:
                stationSlot = i
            i += 1       
        return stationSlot
        
    
    # called if a train QPushButton is clicked
    def trainButtonClicked(self):
        buttonName = self.sender().objectName()
        number = buttonName[1:]
        company = int(number[:1])
        card = int(number[1:])
        if company == self.currentCompany:
            trainList = self.trainList[company]                                 # get the train list for the company
            activeTrain = trainList[card]                                       # get the clicked card for that company and
            activeTrain = activeTrain + 1                                       # increment the train value
            if activeTrain > 7: 
                activeTrain = 1
            self.trainList[company][card] = activeTrain                         # set the value in that company train list for export
            slot = ((company-1) * 4) + card                                     # find which slot in the trainbuttons is active
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
            self.endTurn = True         # this forced the method to choose new hexag rather than same hexag since there may be upgrade tiles now available
            
            
    def companyButtonClicked(self):                                         # this is where the players actions are finalized and sent to the board
        print(" >>>>>company button presssed<<<<<<")
        buttonName = self.sender().objectName()
        pixmap = QIcon(self.getImage(buttonName))                           # makes a  pixmap with a dark background to show the button is clicked
        company = int(buttonName[-1])
        if company != self.currentCompany:                                  # prevents action if the active company is clicked again
            for cButton in self.companyButtons:                             # turns off all of the buttons
                icon = QIcon ()
                cButton.setIcon(icon)
            self.sender().setIcon(pixmap)                                   # turns on the current button
            self.currentCompany = company
            
            print(f"((((())))) stationClicked = {self.stationClicked} stationPlaced = {self.stationPlaced}")
            if self.stationClicked == True and self.stationPlaced == False:  # if a station was clicked and not placed then replace it
                stationSlot = self.findStation()
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                self.stationMarkers[stationSlot].setIcon(icon)
                self.currentCityButton = ""
                self.currentStation = "stn 9"
                
            # this section is where the board hex gets updated to the new tile and city station    
            # if there is a new tile [tile number, name, angle]  
            if self.currentTile != [0,0,0]:                                                           
                name = self.currentTile[1]
                hexag = self.board.findHexagByName(name)            # find the board hexag being updated
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                print(f"Current tile = {self.currentTile}")
                print(f"hexag = {hexag}")
                print(f"hexagName {hexag.hexag_name}")
                print("tile = " + str(self.currentTile[0]))
                print (f"name = {name}")
                print("angle = " + str(self.currentTile[2]))
                print(f"current station = {self.currentStation}")
                stationCompany = int(self.currentStation[4])       # format is stn XY where X is company and Y is slot(0-3) ie stn 31           
                if self.currentCityButton != "":
                    cityNumber = int(self.currentCityButton[8])     # format is cityxxxxy where xxxx is the location and y the city number
                    print(f"=====current city button = {self.currentCityButton}")
                    cityObj = self.findCityObj(self.currentCityButton)  # this finds and sets the city object so that if cannot be changed again
                    cityObj.setCitySet(True)
                    cityObj.setCompany(stationCompany)
                print(f"station = {self.currentStation}")
                for slot in self.stationMarkerUsed:
                    if slot[0] == self.currentStation:
                        print(f"station slot = {slot}")
                        slot[1] = 1               
                cityButtonName =  self.currentCityButton[4:8] 
                print(f"<<<<>>>>>>currentCityButton = {cityButtonName}")
                if hexag.hexag_name == cityButtonName:                  # if the hexag being updated matches the cityButton
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], cityNumber, stationCompany)
                elif cityButtonName != "":                              # cityButton has been clicked and is on another hexag
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], 100, 100)
                    cbHexag = self.board.findHexagByName(cityButtonName)
                    cbHexagName = cbHexag.hexag_name
                    cbHexagTile = cbHexag.hexagTile
                    cbHexagAngle = cbHexag.angle
                    print(f"hex tile {cbHexagTile} hex angle {cbHexagAngle}")
                    self.board.updateHexagWithTile(cbHexagTile, cbHexagName ,cbHexagAngle, cityNumber, stationCompany)
                else:
                    currentTileNumber = self.currentTile[0]
                    tile = self.board.allTilesLookUp(currentTileNumber)
                    tileCompany = tile.station_list[0][0]
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], 100, tileCompany)
                self.currentTile = [0,0,0]
            # otherwise if a cityButton has been clicked   
            elif self.currentCityButton != "":  
                stationCompany = int(self.currentStation[4])
                cityNumber = int(self.currentCityButton[8])
                cityButtonName =  self.currentCityButton[4:8]
                cbHexag = self.board.findHexagByName(cityButtonName)
                cbHexagName = cbHexag.hexag_name
                cbHexagTile = cbHexag.hexagTile
                cbHexagAngle = cbHexag.angle
                print(f"hex tile {cbHexagTile} hex angle {cbHexagAngle}")
                cityObj = self.findCityObj(self.currentCityButton)
                cityObj.setCitySet(True)
                cityObj.setCompany(stationCompany)
                self.board.updateHexagWithTile(cbHexagTile, cbHexagName ,cbHexagAngle, cityNumber, stationCompany)
                
            else:
                print("nothing to update")
                
            # this is resets the variables for the next player/company
            self.currentCityButton = ""                     # set the station token back to blank as the "turn" is ended
            self.currentTHName = ""                          # set to -1 not 0 so that if hexag 0 is clicked it will register as a new hexag and not be rejected
            self.endTurn = True
            self.stationClicked = False
            self.stationPlaced = False
            self.currentStation = "stn 9"
            print(f"current city button = {self.currentCityButton}")
           
         
    # called if a city QPushbutton is clicked
    def cityButtonClicked(self, company):
        button = self.sender()
        print("------CityButtonClicked--------")
        print(f"{button.objectName()}  active = {button.getActive()} set = {button.getCitySet()}")
        if button.getActive() == True and button.getCitySet() == False:       
            buttonName = button.objectName()
            print("buttonName: " + str(buttonName))
            print("currentCityButton =  " + str(self.currentCityButton))
            print(f"CurrentStation {self.currentStation}")
            
            if self.currentCityButton != "":                                # used to blank out a station icon if another station is clicked before finalizing with company
                print("In city reset")
                cityObj = self.findCityObj(self.currentCityButton)
                numCities = 0
                if cityObj and cityObj.getActive() == False:
                    print("in inner loop")
                    cityObj.setActive(True)             
                    hexagName = buttonName[4:8]
                    hexag = self.board.findHexagByName(hexagName)
                    if hexagName == self.currentTHName:
                        numCities = self.currentNumberOfCities
                    else:
                        tileNumber = hexag.hexagTile
                        hexagTile = self.board.allTilesLookUp(tileNumber)
                        numCities = hexagTile.city_count
                if numCities == 0:
                    cityObj.setIcon(QIcon())
                elif numCities == 1 or numCities == 2:
                    cityObj.setIcon(QIcon(self.getImage("greyDot")))
                else:
                    objName = cityObj.name
                    buttonSlot = objName[8]
                    if buttonSlot % 2 == 0:
                        cityObj.setIcon(QIcon(self.getImage("w")))
                    else:
                        cityObj.setIcon(QIcon(self.getImage("b")))
            if int(self.currentStation[4]) < 9:                          # if a station icon was clicked set the station token to that icon
                hexagName = buttonName[4:8]
                hexag = self.board.findHexagByName(hexagName)               # get the hexag for the loaction of the station
                print(f"hexagName = {hexagName} self.currentTHName = {self.currentTHName} ")
                if hexagName == self.currentTHName:
                    print("top method used")
                    numCities = self.currentNumberOfCities
                else:
                    print("bottom method used")
                    tileNumber = hexag.hexagTile
                    hexagTile = self.board.allTilesLookUp(tileNumber)
                    numCities = hexagTile.city_count
                company = self.currentStation[4]
                print(f"company = {company} number of cities = {numCities}")
                if numCities < 20:
                    bw = 2
                else:
                    slot = int(buttonName[8])
                    if slot % 2 == 0:
                        bw = 0
                    else:
                        bw = 1
                icon = self.getCompanyIcon(company, bw)
                button.setIcon(icon)
                self.currentCityButton = buttonName
                    
    
    def displayCity(self, name, tileHexagClicked, numberOfCities, startUp):                
        hexag = self.board.findHexagByName(name)
        hexagName = hexag.hexag_name
        csLen = len(hexag.companySides)
        self.currentTHName = name
        self.currentNumberOfCities = numberOfCities
        print("<<<<<<Display City>>>>>>>>>")
        print(f"Name = {name} numberOfCities = {numberOfCities}")
        
        locRow = name[:2]
        if locRow[0] == "0":                                        # strip of leading zeros
            hexagRow = int(locRow[1])
        else:
            hexagRow = int(locRow)
        locCol = name[-2:]
        if locCol[0] == "0":                                        # strip of leading zeros
            hexagCol = int(locCol[1])
        else:
            hexagCol = int(locCol)
            
        cityList = []
        for i in range(csLen):
            cityList.append(self.findCityObj("city" + hexagName + str(i)))
            comp = self.findCityObj("city" + hexagName + str(i))  
            
        if cityList == [None, None]:
            return
            
        for i in range(len(cityList)):
            comp = cityList[i].company 
            print(f"slot = {i} company = {comp}")              
            
        if cityList != [None, None]:                                                        # this is needed because village tiles have no upgrade
            if hexagRow < 7:
                colSize = 100
            else:
                colSize = 101
            if numberOfCities == 0:                                                         # going from (1 to 0) or (20 to 0)
                for i in range(csLen):
                    cityList[i].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-35, 40, 40)
                    cityList[i].setActive(False)
                    cityList[i].setIcon(QIcon())
                    self.stationPlaced = False
            elif numberOfCities == 1:                                                       # going from (0 to 1) or (2 to 1)
                for i in range(csLen):   
                    cityList[i].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-35, 40, 40)
                    if hexagName == "1115":
                        cityList[i].setGeometry(int(colSize*(hexagCol/2))-52, (87*hexagRow)-50, 40, 40)
                if startUp == False:
                    if int(cityList[0].company) < 50:                                                # there's a company here
                        cityList[0].setActive(False)
                        icon = self.getCompanyIcon(cityList[0].company, 2)
                        cityList[0].setIcon(icon)
                    else:                                                                       # there's no company here
                        cityList[0].setActive(True)
                        cityList[0].setIcon(QIcon(self.getImage("greyDot")))
                        self.stationPlaced = False
            elif numberOfCities == 2:                                                       # going from (1 to 2)     
                cityList[0].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
                cityList[1].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-15, 40, 40) 
                if startUp == False:
                    for i in range(2):
                        print(f"Comp = {cityList[i].company}")
                        if int(cityList[i].company) < 50:                                            # there's a company here
                            cityList[i].setActive(False)
                            icon = self.getCompanyIcon(cityList[i].company, 2)
                            cityList[i].setIcon(icon)
                        else:                                                                  # there's no company here
                            cityList[i].setActive(True)
                            cityList[i].setIcon(QIcon(self.getImage("greyDot")))
                            self.stationPlaced = False
            elif numberOfCities == 20:                                                      # going from (0 to 20) or (40 to 20)
                cityList[0].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
                cityList[1].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-15, 40, 40)
                if name == "0719":
                    cityList[2].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-55, 40, 40)         # for NY        
                    cityList[3].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-15, 40, 40) 
                if startUp == False:
                    for i in range(csLen):
                        if int(cityList[i].company) < 50:                                            # there's a company here
                            cityList[i].setActive(False)
                            icon = self.getCompanyIcon(cityList[i].company, (i))
                            cityList[i].setIcon(icon)
                        else:                                                                   # there's no company here
                            cityList[i].setActive(True)
                            if i == 0:
                                cityList[i].setIcon(QIcon(self.getImage("w")))
                            elif i == 1:
                                cityList[i].setIcon(QIcon(self.getImage("b")))
                            else:
                                cityList[i].setIcon(QIcon())
                                cityList[i].setActive(False)
                            self.stationPlaced = False
            else:                                                                           # going from (20 to 40)
                if startUp == True:
                    cityList[0].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
                    cityList[1].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-15, 40, 40)
                    cityList[2].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-55, 40, 40)               
                    cityList[3].setGeometry(int(colSize*(hexagCol/2))-38, (87*hexagRow)-15, 40, 40)
                
                else:
                    cityList[0].setGeometry(int(colSize*(hexagCol/2))-55, (87*hexagRow)-55, 40, 40)         # space out the cities        
                    cityList[1].setGeometry(int(colSize*(hexagCol/2))-15, (87*hexagRow)-55, 40, 40)
                    cityList[2].setGeometry(int(colSize*(hexagCol/2))-55, (87*hexagRow)-15, 40, 40)               
                    cityList[3].setGeometry(int(colSize*(hexagCol/2))-15, (87*hexagRow)-15, 40, 40)
                    for i in range(4):
                        if i % 2 == 0:
                            color = 0
                        else:
                            color = 1
                        if int(cityList[i].company) < 50:
                            cityList[i].setActive(False)
                            icon = self.getCompanyIcon(cityList[i].company, color)
                            cityList[i].setIcon(icon)
                        else:
                            cityList[i].setActive(True)
                            if color == 0:
                                cityList[i].setIcon(QIcon(self.getImage("w")))
                            else:
                                cityList[i].setIcon(QIcon(self.getImage("b")))
                            self.stationPlaced = False
                            
                
    def getCompanyIcon(self, company, bw):
        if bw == 0:
            icon = QIcon(self.getImage("s" + str(company) + "w"))  
        elif bw == 1:
            icon = QIcon(self.getImage("s" + str(company) + "b"))   
        else:
            icon = QIcon(self.getImage("s" + str(company)))
        if company == self.currentStation[4]:
            self.stationPlaced = True
        return icon
        
    
    # helper method to return the slot in cityButtons of the currentCity                    
    def findCityButton(self, cityName):
        #print(f"cityButton {cityButton}")
        i = 0
        stationSlot = 0
        for stationTest in self.cityButtons:
            if stationTest.objectName() == cityName:
                stationSlot = i
            i += 1
        return stationSlot
    
    
    # helper method to return the city object from cityButtons based upon city name
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


    def colorTiles(self, tileNumber, name, angle, train): 
        colorList = [(255,255,0,128), (240,227,25,200), (240,227,25,200),(240,227,25,200)]
        color = QColor(*colorList[train])
        tileName = self.tileDictionary[tileNumber]
        pixmap = QPixmap(self.getImage(tileName))
        for slot in self.tileHexagList:
            sName = slot.objectName()
            if sName == name:
                hexagTile = slot
        # Blend the color with the icon pixmap       
        #pixmap = icon.pixmap(icon.availableSizes()[0])                   # Get the first available size
        pixmap_with_color = QPixmap(pixmap.size())
        pixmap_with_color.fill(Qt.transparent)                           # Fill pixmap with transparency
        painter = QPainter(pixmap_with_color)
        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)  # Blend mode
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceAtop)  # Apply color atop the pixmap
        painter.fillRect(pixmap.rect(), color)
        painter.end()
        
        hexagTile.setPixmap(pixmap_with_color)

        
        
        