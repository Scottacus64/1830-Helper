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
        self.stationMarkers = []
        self.stationMarkerUsed = []
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
        self.currentHexag = -1
        self.currentNumberOfCities = 0
        self.stationClicked = False
        self.stationPlaced = False
        self.startUp = True
        self.currentHPB = None
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
                location = str(sRow + sCol)
                
                if map[row][col] == 1:                   
                    name = sRow + sCol
                    button = HexagPushButton(name, self.board, self)         
                    button.resize(117,116) 
                    button.move(-25+(100*col)+shift, 13+(87 * row))
                    self.hexagButtons.append(button)            
                    self.checkForCity(location, col+1, row+1)     # check to see if the hexag has a city on it
                if map[row][col] == 2:
                    self.checkForCity(location, col+1, row+1)     # check to see if the hexag has a city on it

        pad = 0 
        
        for button in self.cityButtons:
            hexagName = button.objectName()
            print(f"buttonName = {button.objectName()}")
            hexagName = hexagName[4:8]
            hexag = self.board.findHexagName(hexagName)
            numberOfCities = hexag.city_count
            locationName = button.location
            location = self.hexagDictionary[locationName]
            self.displayCity(locationName, location, numberOfCities, True)

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
        self.currentHexag = -1


    # used to show if a hexag has a city on it    
    def checkForCity(self, location, col, row):
        hexag = self.board.findHexagName(location)
        if hexag and hexag.city_count > 0:
            print("city found at: " + str(location))
            #if hexag.rr_start == 100:
            start = hexag.city_count
            if hexag.hexag_name == "0719":
                start = 3
            if start == 2:
                start = 1
            for i in range(start, -1, -1):
                cityName = str("city" + str(location) + str(i))
                cityButton = CityButton(cityName, self, False, False, location, "100", self)
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
                        print(f"RR start on {location} of company {hexag.rr_start}")
                        cityButton.setCitySet(True)
                    if location == "0523" or location == "0719" or location == "0915" or location == "0519":
                        cityButton.setCitySet(True) 
                    if location == "1115" or location == "0402" or location == "0414":
                        cityButton.setActive(True)
                if i == 1 and location == "0719":
                    cityButton.setActive(True)
                self.cityButtons.append(cityButton)       
                        

    # method for getting the image files
    def getImage(self, imageName):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join("resources", imageName)
        image_path = os.path.join(current_dir, relative_path)
        pixmap = QPixmap(image_path)
        return pixmap
    
    
    # method for getting and displaying tiles gotten from theBoard
    def displayTile(self, tileNumber, location, angle, hexPB):       
        locationName = hexPB.name
        numberOfCities = -1
        print("")
        print(f"tileNumber {tileNumber} location {location} locationName {locationName} angle = {angle}")
        if location > -1:
            hexag = self.board.findHexagByNumber(location)
        if tileNumber > 0:                                      # if it is a hexag     
            self.currentTile = [tileNumber, location, angle]    # variable to know if any tiles have been clicked and what the tile info is
            tileName = self.tileDictionary[tileNumber]
            numberOfCities = self.board.allTilesLookUp(tileNumber).city_count
            icon = QIcon(self.getImage(tileName))
        else:                                                   # if it is an old icon that needs to be made blank
            icon = QIcon()
            numberOfCities = 0
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
            hexPB.setIcon(QIcon(final_pixmap))
            hexPB.setIconSize(QSize(115, 115))                           # Set the size of the icon
        else:
            hexPB.setIcon(icon)
            hexPB.setIconSize(QSize(115, 115))                           # Set the size of the icon
        if location > -1 and numberOfCities > -1:
            self.displayCity(locationName, location, numberOfCities, False)
                
        
    # called if a station QPushButton is clicked
    def stationMarkerClicked(self):
        buttonName = self.sender().objectName()                                 # find out which station was clicked
        print("Station: ", buttonName)
        print("Current station " + self.currentStation)
        print(f"Button Name {buttonName}")
        if int(self.currentCompany) == int(buttonName[4]):                      # check to see if the button clicked matches the current company
            for slot in self.stationMarkerUsed:
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
                    self.stationMarkers[stationSlot].setIcon(icon)              # resets a station back to its original icon
                    icon = QIcon()
                    self.cityButtons[stationSlot].setIcon(icon)
                    self.currentStation = "stn 100"
                    self.stationClicked = False  
                    return        
                if self.currentStation == buttonName:
                    print("******In attempt to reset station button")
                    self.stationMarkers[stationSlot].setIcon(icon) 
                    stationSlot = self.findCityButton(self.currentCityButton)
                    cityObj = self.cityButtons[stationSlot]
                    hexagName = cityObj.name[4:8]
                    print(f"HexagName = {hexagName}")
                    hexagObj = self.board.findHexagName(hexagName)
                    hexagTileNumber = hexagObj.hexagTile
                    tilePlaced= 0
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
                    self.currentStation = "stn 100"
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
            
            
    # called is a company QPushButton is clicked
    def companyButtonClicked(self):
    #    pdb.set_trace() 
        print(" >>>>>company button presssed<<<<<<")
        buttonName = self.sender().objectName()
        print("Company button: " + buttonName)
        pixmap =QIcon(self.getImage(buttonName))    
        company = int(buttonName[-1])
        print(f"Current Company = {self.currentCompany}")
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
                self.stationMarkers[stationSlot].setIcon(icon)
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
                    print(f"=====current city button = {self.currentCityButton}")
                    cityObj = self.findCityObj(self.currentCityButton)
                    cityObj.setCitySet(True)
                    cityObj.setCompany(stationCompany)
                print(f"station = {self.currentStation}")
                for slot in self.stationMarkerUsed:
                    if slot[0] == self.currentStation:
                        print(f"station slot = {slot}")
                        slot[1] = 1               
                cityButtonName =  self.currentCityButton[4:8] 
                print(f"currentCityButton = {cityButtonName}")
                if hexag.hexag_name == cityButtonName:
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], cityNumber, stationCompany)
                elif cityButtonName != "":                 
                    self.board.updateHexagWithTile(self.currentTile[0], self.currentTile[1] , self.currentTile[2], 100, 100)
                    cbHexag = self.board.findHexagName(cityButtonName)
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
                cbHexag = self.board.findHexagName(cityButtonName)
                cbHexagName = cbHexag.hexag_name
                cbHexagTile = cbHexag.hexagTile
                cbHexagAngle = cbHexag.angle
                print(f"hex tile {cbHexagTile} hex angle {cbHexagAngle}")
                cbHexagLocation = self.hexagDictionary[cbHexagName]
                print(f"cbHexagLocation {cbHexagLocation}")
                cityObj = self.findCityObj(self.currentCityButton)
                cityObj.setCitySet(True)
                cityObj.setCompany(stationCompany)
                self.board.updateHexagWithTile(cbHexagTile, cbHexagLocation ,cbHexagAngle, cityNumber, stationCompany)
                
            else:
                print("nothing to update")
                
            # this is where the code to let the board know that the tile has been finalized would go
            self.currentCityButton = ""                     # set the station token back to blank as the "turn" is ended
            self.currentHexag = -1                          # set to -1 not 0 so that if hexag 0 is clicked it will register as a new hexag and not be rejected
            self.endTurn = True
            self.stationClicked = False
            self.stationPlaced = False
            self.currentStation = "stn 100"
            print(f"current city button = {self.currentCityButton}")
           
         
    # called if a city QPushbutton is clicked
    def cityButtonClicked(self, company):
        button = self.sender()
        print("------CityButtonClicked--------")
        print(f"{button.objectName()} = {button.getActive()}")
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
                    hexag = self.board.findHexagName(hexagName)
                    hexagLocation = self.hexagDictionary[hexagName]
                    if hexagLocation == self.currentHexag:
                        numCities = self.currentNumberOfCities
                    else:
                        numCities = hexag.city_count
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
            if int(self.currentStation[4:]) < 100:                          # if a station icon was clicked set the station token to that icon
                hexagName = buttonName[4:8]
                hexag = self.board.findHexagName(hexagName)                 # get the hexag for the loaction of the station
                hexagLocation = self.hexagDictionary[hexagName]
                if hexagLocation == self.currentHexag:
                    numCities = self.currentNumberOfCities
                else:
                    numCities = hexag.city_count
                company = self.currentStation[4]
                print(f"company = {company}")
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
                    
    
    def displayCity(self, locationName, location, numberOfCities, startUp):                # location is a number 0 - 76
        hexag = self.board.findHexagByNumber(location)
        hexagName = hexag.hexag_name
        csLen = len(hexag.companySides)
        self.currentHexag = location
        self.currentNumberOfCities = numberOfCities
        print("<<<<<<Display City>>>>>>>>>")
        print(f"Location = {location} numberOfCities = {numberOfCities} locationName = {locationName}")
        
        locRow = locationName[:2]
        if locRow[0] == "0":                                        # strip of leading zeros
            hexagRow = int(locRow[1])
        else:
            hexagRow = int(locRow)
        locCol = locationName[-2:]
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
            if numberOfCities == 0:                                                         # going from (1 to 0) or (20 to 0)
                for i in range(csLen):
                    cityList[i].setGeometry((50*hexagCol)-38, (87*hexagRow)-35, 40, 40)
                    cityList[i].setActive(False)
                    cityList[i].setIcon(QIcon())
                    self.stationPlaced = False
            elif numberOfCities == 1:                                                       # going from (0 to 1) or (2 to 1)
                for i in range(csLen):   
                    cityList[i].setGeometry((50*hexagCol)-38, (87*hexagRow)-35, 40, 40)
                    if hexagName == "1115":
                        cityList[i].setGeometry((50*hexagCol)-52, (87*hexagRow)-50, 40, 40)
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
                cityList[0].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
                cityList[1].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40) 
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
                cityList[0].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
                cityList[1].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40) 
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
                    cityList[0].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)         # space out the cities        
                    cityList[1].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40)
                    cityList[2].setGeometry((50*hexagCol)-38, (87*hexagRow)-55, 40, 40)               
                    cityList[3].setGeometry((50*hexagCol)-38, (87*hexagRow)-15, 40, 40)
                
                else:
                    cityList[0].setGeometry((50*hexagCol)-55, (87*hexagRow)-55, 40, 40)         # space out the cities        
                    cityList[1].setGeometry((50*hexagCol)-15, (87*hexagRow)-55, 40, 40)
                    cityList[2].setGeometry((50*hexagCol)-55, (87*hexagRow)-15, 40, 40)               
                    cityList[3].setGeometry((50*hexagCol)-15, (87*hexagRow)-15, 40, 40)
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
        
        