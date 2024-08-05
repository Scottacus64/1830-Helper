#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:55:38 2024
@author: scottmiller
"""


import os
import pdb
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QTransform, QIcon, QPalette, QColor, QPainter
from HexagPushButton import HexagPushButton
from Board import Board
from CityButton import CityButton
from PyQt5.QtCore import Qt, QSize


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.hexagButtons = []                   # set up these global variables before the initUI
        self.stationButtons = []
        self.stationButtonUsed = []
        self.trainButtons = []
        self.companyButtons = []
        self.trainList = []
        self.cityButtons = []
        self.currentTile = [0,0,0]
        self.currentStation = "stn 100"
        self.currentCompany = 9
        self.oneCityIndex = 0
        self.twoCityIndex = 0
        self.endTurn = True
        self.currentCityButton = ""
        self.currentHexag = 0
        self.stationClicked = False
        self.stationPlaced = False
        self.startUp = True
        self.initUI()
 
        
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
        
        self.hexagDictionary = {
            "0210": 0, "0212": 1, "0214": 2, "0216": 3, "0218": 4, "0220": 5, "0222": 6, 
            "0307": 7, "0309": 8, "0311": 9, "0313": 10, "0317": 11, "0319": 12, "0321": 13, "0323": 14,
            "0402": 15, "0404": 16, "0406": 17, "0408": 18, "0410": 19, "0412": 20, "0414": 21, "0416": 22, "0418": 23, "0420": 24, "0422": 25, 
            "0503": 26, "0505": 27, "0507": 28, "0511": 29, "0513": 30, "0515": 31, "0517": 32, "0519": 33, "0521": 34, "0523": 35,
            "0604": 36, "0608": 37, "0610": 38, "0612": 39, "0614": 40, "0616": 41, "0618": 42, "0620": 43, "0622": 44, 
            "0703": 45, "0705": 46, "0707": 47, "0709": 48, "0711": 49, "0713": 50, "0715": 51, "0717": 52, "0719": 53,
            "0802": 54, "0804": 55, "0806": 56, "0808": 57, "0810": 58, "0814": 59, "0816": 60, "0818": 61, 
            "0903": 62, "0905": 63, "0907": 64, "0909": 65, "0911": 66, "0913": 67, "0915": 68, "0917": 69, 
            "1004": 70, "1006": 71, "1008": 72, "1010": 73, "1012": 74, "1014": 75, 
            "1115": 76
        } 
        
        # this is the number of stations per company
        self.stationList = [2,3,3,4,3,4,2,4]
        
        # make the QPushbuttons for the hexages
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
                    button = HexagPushButton(name, self, self.board, self)         
                    button.resize(117,116) 
                    button.move(-25+(100*col)+shift, 13+(87 * row))
                    self.hexagButtons.append(button) 
                    location = str(sRow + sCol)
                    self.checkForCity(location, col+1, row+1)     # check to see if the hexag has a city on it

        pad = 0 
        
        for button in self.cityButtons:
            hexagName = button.objectName()
            print(f"buttonName = {button.objectName()}")
            hexagName = hexagName[4:8]
            #print(f"hexagName {hexagName}")
            hexag = self.board.findhexagName(hexagName)
            numberOfCities = hexag.city_count
            #print(f"hexag obj = {hexag}")
            button.clicked.connect(self.cityButtonClicked)
            if numberOfCities == 1:
                self.drawCity(hexag, numberOfCities, 0, True)
            else:
                self.drawCity(hexag, numberOfCities, 0, False)
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
                    sButton.clicked.connect(self.stationButtonClicked)
                    sButton.setText("")
                    sButton.setStyleSheet("border: none;")
                    icon = QIcon(self.getImage(str("s" + str((row//2)+1))))
                    sButton.setIconSize(QSize(60,60))
                    sButton.setIcon(icon)
                    self.stationButtons.append(sButton)
                    self.stationButtonUsed.append([sName, 0])
                    
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
        specialCity = [["city01190",4],["city06060",3],["city08120",8]]
        for city in specialCity:
            cityButton = CityButton(city[0], self, False, True, city[1])
            self.cityButtons.append(cityButton)
        self.show()
        self.startUp = False
        for city in self.cityButtons:
            city.printCityButton()


    # used to show if a hexag has a city on it    
    def checkForCity(self, location, col, row):
        hexag = self.board.findhexagName(location)
        if hexag and hexag.city_count > 0:
            print("city found at: " + str(location))
            #if hexag.rr_start == 100:
            start = hexag.city_count
            if start == 2:
                start = 1
            elif start == 4:
                start = 3
            for i in range(start, -1, -1):
                cityName = str("city" + str(location) + str(i))
                cityButton = CityButton(cityName, self, False, False, "0", self)
                cityButton.setObjectName(cityName)
                cityButton.clicked.connect(self.cityButtonClicked)  
                cityButton.setText("")
                cityButton.setStyleSheet("QPushButton { color: transparent; border: 2px solid red; }")
                icon = QIcon()
                cityButton.setIconSize(QSize (38,38))
                cityButton.setIcon(icon)
                self.cityButtons.append(cityButton)
                if i == 0:
                    if hexag.rr_start < 100:
                        cityButton.setCompany(hexag.rr_start)
                        print(f"RR start on {location} of company {hexag.rr_start}")
                    if location == "0523" or location == "0719" or location == "0915" or location == "0519":
                        cityButton.setCitySet(True) 

                        
            
    
    # method for getting the image files
    def getImage(self, imageName):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join("resources", imageName)
        image_path = os.path.join(current_dir, relative_path)
        pixmap = QPixmap(image_path)
        return pixmap
    
    
    # method for getting and displaying tiles gotten from theBoard
    def displayTile(self, tileNumber, location, angle):
        hexagPB = self.hexagButtons[location]
        if tileNumber > 0:                                      # if it is a hexag
            hexag = self.board.findHexagByNumber(location)
            self.currentTile = [tileNumber, location, angle]    # variable to know if any tiles have been clicked and what the tile info is
            tileName = self.tileDictionary[tileNumber]
            icon = QIcon(self.getImage(tileName))
        else:                                                   # if it is an old icon that needs to be made blank
            icon = QIcon()
        if angle > 0:
            transform = QTransform()
            transform.rotate(angle * 60)
            original_pixmap = icon.pixmap(QSize(115, 115))
            rotated_pixmap = original_pixmap.transformed(transform, Qt.SmoothTransformation)
            final_pixmap = QPixmap(QSize(115, 115))                             # new QPixmap with the desired size
            final_pixmap.fill(Qt.transparent)                                   # transparent color
            xOffset = (final_pixmap.width() - rotated_pixmap.width()) / 2       # draw the rotated pixmap to center it in the final pixmap
            yOffset = (final_pixmap.height() - rotated_pixmap.height()) / 2
            painter = QPainter(final_pixmap)                                    # Draw the rotated pixmap onto the final pixmap
            painter.drawPixmap(int(xOffset), int(yOffset), rotated_pixmap)
            painter.end() 
            hexagPB.setIcon(QIcon(final_pixmap))
            hexagPB.setIconSize(QSize(115, 115))                           # Set the size of the icon
        else:
            hexagPB.setIcon(icon)
            hexagPB.setIconSize(QSize(115, 115))                           # Set the size of the icon
        if location > -1:
            self.displayStations(tileNumber, location)

            
    def displayStations(self, tileNumber, location):   # location is a number 0 - 76, city names are like city081021
        hexag = self.board.findHexagByNumber(location)
        cityCount = hexag.city_count
        tile = self.board.allTilesLookUp(tileNumber)
        if tile:
            hexCityCount = tile.city_count
            if hexCityCount > 0:
                print(f"city count {hexCityCount} CS = {hexag.companySides}")
                for city in range(hexCityCount):
                    index = 0
                    for hexagCS in hexag.companySides:
                        if index == city and hexagCS[0] < 50:
                            buttonName = str("city" + hexag.hexag_name + str(city))
                            print(f"display stations {buttonName}")
                            self.setCityButton(buttonName, hexagCS[0], cityCount)          
                            break
                        index += 1
                
        
    # called if a station QPushButton is clicked
    def stationButtonClicked(self):
        buttonName = self.sender().objectName()                                 # find out which station was clicked
        print("Station: ", buttonName)
        print("Current station " + self.currentStation)
        print(f"Button Name {buttonName}")
        if int(self.currentCompany) == int(buttonName[4]):                      # check to see if the button clicked matches the current company
            for slot in self.stationButtonUsed:
                if slot[0] == buttonName and slot[1] == 1:
                    return
            self.stationClicked = True
            stationSlot = 100
            if int(self.currentStation[4:]) < 100:                              # this lets stations in the same company reset if another station is clicked
                stationSlot = self.findStation()
                print("Station slot = " + str(stationSlot))
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                if self.currentCityButton == "": 
                    self.stationButtons[stationSlot].setIcon(icon)              # resets a station back to its original icon
                    icon = QIcon()
                    self.cityButtons[stationSlot].setIcon(icon)
                    self.currentStation = "stn 100"
                    self.stationClicked = False  
                    return        
                if self.currentStation == buttonName:
                    print("******In attempt to reset station button")
                    self.stationButtons[stationSlot].setIcon(icon) 
                    icon = QIcon(self.getImage("greyDot"))
                    stationSlot = self.findCityButton(self.currentCityButton)
                    self.cityButtons[stationSlot].setIcon(icon)
                    self.currentStation = "stn 100"
                    self.stationClicked = False
                    return      
            self.currentStation = buttonName
            stationSlot = self.findStation()
            self.stationButtons[stationSlot].setIcon(QIcon())
        
        
    # helper method to find a station from the stationButtons list   
    def findStation(self):
        print(f" findstation {self.currentStation}")
        i = 0
        for stationTest in self.stationButtons:
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
            
            
    # called is a company QPushButton is clicked
    def companyButtonClicked(self):
    #    pdb.set_trace() 
        print(" >>>>>>>>>>>company button presssed<<<<<<<<<<<<<<")
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
            
            if self.stationClicked == True and self.stationPlaced == False:  # if a station was clicked and not placed then replace it
                stationSlot = self.findStation()
                company = self.currentStation[4]
                icon = QIcon(self.getImage(str("s" + company)))
                self.stationButtons[stationSlot].setIcon(icon)
                self.currentStation = "stn 100"
                
            # this is where the board hex gets updated to the new tile and city station    
            if self.currentTile != [0,0,0]:                                     #if there is a new tile                           
                location = self.currentTile[1]
                hexag = self.board.findHexagByNumber(location)
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                print(f"Current tile = {self.currentTile}")
                print(f"hexag = {hexag}")
                print(f"hexagName {hexag.hexag_name}")
                print("tile = " + str(self.currentTile[0]))
                print (f"location = {location}")
                print("angle = " + str(self.currentTile[2]))
                stationCompany = int(self.currentStation[4])
                
                if self.currentCityButton:
                    cityNumber = int(self.currentCityButton[8])
                    cityObj = self.findCityObj(self.currentCityButton)
                    cityObj.setCitySet(True)

                print(f"station = {self.currentStation}")
                for slot in self.stationButtonUsed:
                    if slot[0] == self.currentStation:
                        print(f"station slot = {slot}")
                        slot[1] = 1
                
                cityButtonName =  self.currentCityButton[4:8] 
                print(f"currentCityButton {cityButtonName}")
                if hexag.hexag_name == cityButtonName:
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], cityNumber, stationCompany)
                elif cityButtonName != "":                 
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], 100, 100)
                    cbHexag = self.board.findhexagName(cityButtonName)
                    cbHexagName = cbHexag.hexag_name
                    cbHexagTile = cbHexag.hexagTile
                    cbHexagAngle = cbHexag.angle
                    print(f"hex tile {cbHexagTile} hex angle {cbHexagAngle}")
                    cbHexagLocation = self.hexagDictionary[cbHexagName]
                    print(f"cbHexagLocation {cbHexagLocation}")
                    self.board.updateHexagWithTile(cbHexagTile, cbHexagLocation ,cbHexagAngle, cityNumber, stationCompany)
                else:
                    currentTileNumber = self.currentTile[0]
                    tile = self.board.allTilesLookUp(currentTileNumber)
                    tileCompany = tile.station_list[0][0]
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], 100, tileCompany)
                self.currentTile = [0,0,0]
            elif self.currentCityButton != "":
                stationCompany = int(self.currentStation[4])
                cityNumber = int(self.currentCityButton[8])
                cityButtonName =  self.currentCityButton[4:8]
                cbHexag = self.board.findhexagName(cityButtonName)
                cbHexagName = cbHexag.hexag_name
                cbHexagTile = cbHexag.hexagTile
                cbHexagAngle = cbHexag.angle
                print(f"hex tile {cbHexagTile} hex angle {cbHexagAngle}")
                cbHexagLocation = self.hexagDictionary[cbHexagName]
                print(f"cbHexagLocation {cbHexagLocation}")
                self.board.updateHexagWithTile(cbHexagTile, cbHexagLocation ,cbHexagAngle, cityNumber, stationCompany)
            else:
                print("nothing to update")
                
            # this is where the code to let the board know that the tile has been finalized would go
            self.currentCityButton = ""                     # set the station token back to blank as the "turn" is ended
            self.currentHexag = -1                          # set to -1 not 0 so that if hexag 0 is clicked it will register as a new hexag and not be rejected
            self.endTurn = True
            self.currentStation = "stn 100"
            print(f"current city button = {self.currentCityButton}")
            
         
    # called if a city QPushbutton is clicked
    def cityButtonClicked(self, company):
        button = self.sender()
        if button.getActive() == True and button.getCitySet() == False:       
            buttonName = button.objectName()
            print("buttonName: " + str(buttonName))
            print("currentCityButton =  " + str(self.currentCityButton))
            print(f"CurrentStation {self.currentStation}")
            
            if self.currentCityButton != "":                                # used to blank out a station icon if another station is clicked before finalizing with company
                cityObj = self.findCityObj(self.currentCityButton)
                if cityObj and cityObj.getActive() == False:
                    hexagName = buttonName[4:8]
                    self.resetCityButton(self.board.findhexagName(hexagName))
            if int(self.currentStation[4:]) < 100:                          # if a station icon was clicked set the station token to that icon
                hexagName = buttonName[4:8]
                hexag = self.board.findhexagName(hexagName)                 # get the hexag for the loaction of the station
                cityCount = hexag.city_count
                print(f"hexagTile {hexag.hexagTile}")
                stationSet = 0
                buttonNumber = buttonName[8]
                if hexag.hexagTile:                                         # if there's a tile here
                    print(f"hexag CS {hexag.companySides}")
                    if hexag.companySides:
                        for hList in hexag.companySides:                # check to see if the hexag's station has been set yet
                            print(f"hList {hList}")
                            if buttonNumber == hList[0]:   
                                stationSet = 1
                        if stationSet == 0:        
                            self.setCityButton(buttonName, self.currentStation[4], cityCount)
                    else:
                        self.setCityButton(buttonName, self.currentStation[4], cityCount)
                else:
                    self.setCityButton(buttonName, self.currentStation[4], cityCount)
                    
    
    # method for setting the station icon of a city                   
    def setCityButton(self, buttonName, company, cityCount):                                
        if self.currentStation != "stn 100":
            print(f"currentStation {self.currentStation}")
            stationSlot = self.findCityButton(buttonName)
            print(f"Button Name {buttonName}")
            if cityCount < 2:
                icon = QIcon(self.getImage(str("s" + str(company))))
            else:
                if buttonName[8] == "0" or buttonName[8] == "2":
                    icon = QIcon(self.getImage(str("s" + str(company) + "w")))
                else:
                    icon = QIcon(self.getImage(str("s" + str(company) + "b")))
            self.cityButtons[stationSlot].setIcon(icon)
            self.currentCityButton = buttonName                         
            self.stationPlaced = True
           
    
    # method to set a city button back to grey or clear depending on if two or one cities
    def resetCityButton(self, hexag):
        numberOfCities = hexag.city_count
        print(f"@@@@@ in reset cityButton, Color = {hexag.color}  num of cities = {numberOfCities}  city count = {hexag.city_count}")
    
        if numberOfCities == 0:
            return
        #note that colors are only updated when the tile is finalized by hitting the company button
        if numberOfCities == 1: 
            if hexag.color == "yellow":
                self.drawCity(hexag, 1, 0, True)                # G1C to blank or G2C to blank
                self.board.setColor(hexag, "")
            elif hexag.color == "green":
                self.drawCity(hexag, 1, 1, True)                # G1C to Y1C (also Balt and Boston)
                self.board.setColor(hexag, "yellow")
            else:
                return                                          # do nothing on B1C to G1C
        
        if numberOfCities == 2 and hexag.color == "green":      # do nothing on B2C to G2C
            self.drawCity(hexag, 1, 0, True)                    # Y1C to blank or G2C to blank
            self.board.setColor(hexag, "yellow")
            
        if numberOfCities == 4:
            if hexag.color == "green":      
                self.drawCity(hexag, 4, 0, True)                # NY2 to blank
                self.board.setColor(hexag, "")
            else:
                self.drawCity(hexag, 4, 1, True)                # NY4 to NY2
                self.board.setColor(hexag, "green")
            

        print("Exit resetCityButton")
        self.currentCityButton = ""
            
    
    def drawCity(self, hexag, numberOfCities, tilePresent, reset):
        print("{{{{{{{{{{{{{Draw city}}}}}}}}}}}}}")   
        print(f"number of cities = {numberOfCities}")           
        csList = self.board.getHexCompanySides(hexag)              # list of hex Company/Sides [3,2,4,6] company 3 with sides 2,4,6
        print(f"CompanySides = {csList}")
        specialCities = ["0523", "0719", "0915", "0519"]
        specialFlag = False
        
        location = hexag.hexag_name                                 # parse out the row and col for the location
        if location in specialCities:                               # find NY, Balt and Boston
            specialFlag = True        
        locRow = location[:2]
        if locRow[0] == "0":                                        # strip of leading zeros
            hexagRow = int(locRow[1])
        else:
            hexagRow = int(locRow)
        locCol = location[-2:]
        if locCol[0] == "0":                                        # strip of leading zeros
            hexagCol = int(locCol[1])
        else:
            hexagCol = int(locCol)
        
        cityList = []                                               # build the city list here rather than send it in     
        if numberOfCities > 0:
            if numberOfCities == 1:
                listSize = 2
            else:
                listSize = numberOfCities
            for i in range(listSize):
                buttonName = str("city" + hexag.hexag_name + str(i))
                #print(f"ButtonName {buttonName}")
                cityObj = self.findCityObj(buttonName)
                cityList.append(cityObj)
                
        print(f"^^^^^cityList {cityList} num of cities {numberOfCities} tile present {tilePresent} location {location} reset = {reset}")
        for i in range (2):
            print(f"csList {i} company is {csList[i][0]}")
            
                                    
        if numberOfCities == 1 and tilePresent == 0 and reset == False:                 # blank to Y1C
            cityList[0].setActive(True)
            if specialFlag == True:
                company = csList[0][0]
                icon0 = QIcon(self.getImage(str("s" + str(company))))
                cityList[0].setActive(False)
                cityList[0].setIcon(icon0)
            else:
                cityList[0].setIcon(QIcon(self.getImage("greyDot")))
        
        if numberOfCities == 1 and tilePresent == 0 and reset == True:                  # Y1C to blank or G2C to blank
            for i in range (2):
                cityList[i].setGeometry((50*hexagCol)-38, (87*hexagRow)-35, 40, 40)
                cityList[i].setIcon(QIcon())
                cityList[i].setActive(False)
                
        if numberOfCities == 1 and tilePresent == 1 and reset == False:                 # Y1C to G1C or G1C to B1C
            cityList[0].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
            cityList[1].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40) 
            for i in range(2):
                print(f"getCitySet = {cityList[i].getCitySet()}")
                if cityList[i].getCitySet() == False:                                     # if the city hasn't been set make the city active and set the icon to grey
                    cityList[i].setActive(True)
                    cityList[i].setIcon(QIcon(self.getImage("greyDot")))
                else:                                                                   # otherwise set the icon to the company and make the city inactive
                    company = csList[i][0]
                    icon = QIcon(self.getImage("s" + str(company)))
                    cityList[i].setIcon(icon)
                    cityList[i].setActive(False)
        
        if numberOfCities == 1 and tilePresent == 1 and reset == True:                  # G1C to Y1C
            icon = QIcon(self.getImage("greyDot"))
            for i in range (2):
                cityList[i].setGeometry((50*hexagCol)-38, (87*hexagRow)-35, 40, 40)     # change from spaced to overlapping cities
            if cityList[0].getCitySet() == False:                                       # if the city hasn't been set (not Balt, Bost or another company)                                                    
                cityList[0].setIcon(icon)                                               # grey icon and active city
                cityList[0].setActive(True)
            else:
                company = csList[0][0]
                icon0 = QIcon(self.getImage(str("s" + str(company))))
                cityList[0].setActive(False)
                if specialFlag == False:                                                # if not Balt or Bost
                    cityList[0].setIcon(icon0)                                          # set icon to company
                else:
                    cityList[0].setIcon(QIcon())                                        # if Balt or Bost then blank out icon to let board icon show
                cityList[1].setIcon(QIcon())                                            # either way blank out city 1's icon
                                  
        if numberOfCities == 2 and tilePresent == 0 and reset == False:                 # blank to G2C or G2C to B2C
            cityList[0].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
            cityList[1].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40) 
            for i in range(2):
                if i == 0:
                    dot = "w"
                else:
                    dot = "b"
                if cityList[i].getCitySet() == False:                                     # if the city hasn't been set make the city active and set the icon to b/w
                    
                    if self.startUp == True:
                        cityList[i].setIcon(QIcon())
                        cityList[i].setActive(False)
                    else:
                        cityList[i].setIcon(QIcon(self.getImage(dot)))
                        cityList[i].setActive(True)
                else:                                                                   # otherwise set the icon to the company and make the city inactive
                    company = csList[i][0]
                    icon = QIcon(self.getImage("s" + str(company) + dot))
                    cityList[i].setIcon(icon)
                    cityList[i].setActive(False)
     
        if numberOfCities == 4 and tilePresent == 0 and reset == False:                 # blank to NY2   
            cityList[0].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
            cityList[1].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40) 
            for i in range(2):
                if cityList[i].getCitySet() == False:                                     # if the city hasn't been set make the city active and set the icon to b/w
                    cityList[i].setActive(True)
                    if i == 0:
                        dot = "whiteDot"
                    else:
                        dot = "blackDot"
                    cityList[i].setIcon(QIcon(self.getImage(dot)))
                else:                                                                   # otherwise set the icon to the company and make the city inactive
                    company = csList[i][0]
                    icon = QIcon(self.getImage("s" + str(company)))
                    cityList[i].setIcon(icon)
                    cityList[i].setActive(False)
                    
        if numberOfCities == 4 and tilePresent == 1 and reset == False:                 # NY2 to NY4
            cityList[0].setGeometry((50*hexagCol)-58, (87*hexagRow)-55, 40, 40)         # space out the cities        
            cityList[1].setGeometry((50*hexagCol)-18, (87*hexagRow)-15, 40, 40)
            cityList[2].setGeometry((50*hexagCol)-58, (87*hexagRow)-55, 40, 40)
            cityList[3].setGeometry((50*hexagCol)-18, (87*hexagRow)-15, 40, 40)
            for i in range(4):
                if i % 2 == 0:
                    dot = "b"
                else:
                    dot = "w"
                if cityList[i].getCitySet() == False:                                     # if the city hasn't been set make the city active and set the icon to b/w
                    cityList[i].setActive(True)

                    cityList[i].setIcon(QIcon(self.getImage(dot)))
                else:                                                                   # otherwise set the icon to the company and make the city inactive
                    company = csList[i][0]
                    icon = QIcon(self.getImage("s" + str(company)))
                    cityList[i].setIcon(icon)
                    cityList[i].setActive(False)
                
        if numberOfCities == 4 and tilePresent == 0 and reset == True:                  # NY2 to blank
            cityList[0].setIcon(QIcon())
            if cityList[1].getCitySet() == False:
                cityList[1].setIcon(QIcon())
                cityList[1].setActive(True)
            else:
                company = csList[1][0]
                icon = QIcon(self.getImage("s" + str(company) + "b"))
                cityList[1].setIcon(icon)
                cityList[1].setActive(False)
                
        if numberOfCities == 4 and tilePresent == 1 and reset == True:                  # NY4 to Ny2
            cityList[0].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
            cityList[1].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40)
            cityList[2].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)               
            cityList[3].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40)
            cityList[0].setIcon(QIcon())
            if cityList[1].getCitySet() == False:
                cityList[1].setIcon(QIcon(self.getImage("b")))
                cityList[1].setActive(True)
            else:
                company = csList[1][0]
                icon = QIcon(self.getImage("s" + str(company) + "b"))
                cityList[1].setIcon(icon)
                cityList[1].setActive(False)
            
        self.currentCityButton = ""
        
        
    
    # helper method to return the slot in cityButtons of the currentCity                    
    def findCityButton(self, cityButton):
        #print(f"cityButton {cityButton}")
        i = 0
        stationSlot = 0
        for stationTest in self.cityButtons:
            if stationTest.objectName() == cityButton:
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


    def colorTiles(self, tileNumber, location, angle, train): 
        colorList = [(255,255,0,128), (240,227,25,200), (240,227,25,200),(240,227,25,200)]
        color = QColor(*colorList[train])
        tileName = self.tileDictionary[tileNumber]
        icon = QIcon(self.getImage(tileName))
        hexagPB = self.hexagButtons[location]
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
        
        hexagPB.setIcon(QIcon(pixmap_with_color)) 
        hexagPB.setIconSize(QSize(115, 115))                         # Set the size of the icon
        
        