
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import  QPolygon, QTransform, QIcon
from PyQt5.QtCore import QPoint, Qt
from Board import Board

class HexagPushButton(QPushButton):
    
    def __init__(self, name, main_window, board, parent=None):
        super().__init__(parent)
        self.name = name
        self.MainWindow = main_window
        self.setFlat(True)
        self.rotation_angle = 0
        self.setStyleSheet("background-color: transparent; border: none; padding: 0;")
        self.theBoard = board  # Use the shared Board object
        self.rotationAngle = 0
       
        
        # this is a list of all tile names from 1 to 70 in ascending order
        self.tileKey = [
            "t1", "t2", "t3", "t4", "t7", "t8", "t9", 
            "t14", "t15", "t16", "t18", "t19",
            "t20", "t23", "t24", "t25", "t26", "t27", "t28", "t29", 
            "t39", "t40", "t41", 't42', "t43", "t44", "t45", "t46", "t47",
            "t53", "t54,", "t55", "t56", "t57", "t58", "t59",
            "t61", "t62", "t63", "t64", "t65", "t66", "t67", "t68", "t69", "t70"
            ]
        
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

    def mousePressEvent(self, event):
        hexagon = QPolygon([
            QPoint(58, 0),
            QPoint(7, 29),
            QPoint(7, 87),
            QPoint(58, 117),
            QPoint(110, 87),
            QPoint(110, 29)
        ])  # corners of the hexagon
        
        overlapping_buttons = self.findOverlappingButtons(event.pos())
        print("..........")
        for cButton in overlapping_buttons:
            print(cButton.name)

        if hexagon.containsPoint(event.pos(), Qt.OddEvenFill):
            location = self.hexagDictionary[self.name]                           # location is an int between 0 and 76
            newLoc = ""
            print(location)
            if location != self.MainWindow.currentHexag or self.MainWindow.endTurn:
                self.newLocationClicked(location)
                self.MainWindow.endTurn = False
            else:
                self.sameLocationClicked(location)
        elif len(overlapping_buttons) > 0:                                  # code designed to check if lower portion with overlapping buttons in clicked
            if len(overlapping_buttons) == 2:   
                newLoc = self.cellAbove(overlapping_buttons[1].name,0)
                print("correctlocation " + newLoc)
            else:
                if event.pos().x() < 60:
                    newLoc = self.cellAbove(overlapping_buttons[0].name,0)
                    print("correct location " + newLoc)
                else:
                    newLoc = self.cellAbove(overlapping_buttons[0].name,1)
                    print("correct location " + newLoc)
            if newLoc in self.hexagDictionary:
                location = self.hexagDictionary[newLoc]
            else:
                location = 100
            if location < 100:
                if location != self.MainWindow.currentHexag or self.MainWindow.endTurn:
                    self.newLocationClicked(location)
                    self.MainWindow.endTurn = False
                else:
                    self.sameLocationClicked(location)
        else:
            print("not a hexag")
            super().mousePressEvent(event)
            
            # This might be used to color in tiles that are a part of a train route
            # self.MainWindow.colorTiles(tileList[0], location, tileList[1], 0)
     
        
    def findOverlappingButtons(self, pos):
        overlapping_buttons = []
        for button in self.MainWindow.hexagButtons:
            if button.geometry().contains(self.mapToGlobal(pos)):
                overlapping_buttons.append(button)
        return overlapping_buttons         
             
    
    def cellAbove(self, name, direction):
        firstTwo = name[:2]
        lastTwo = name[-2:]
        newFirst = int(firstTwo) - 1
        if direction == 0:
            newLast = int(lastTwo) - 1
        else:
            newLast = int(lastTwo) + 1
        if newFirst < 10:
            newFirst = str("0" + str(newFirst))
        if newLast < 10:
            newLast = str("0" + str(newLast))
        newLoc = str(str(newFirst) + str(newLast)) 
        return newLoc
       
            
    def newLocationClicked(self, location):                 # location is an int between 0 and 76
        print(f"******** New Location {location}")
        # check if the player clicked on a second tile this turn, if so we need to either blank out the previous tile or reset it to its original tile
        if self.MainWindow.currentHexag > -1:                                       # this case there was a previous tile, -1 because there is a '0' hexag
            currentHexagNumber = self.MainWindow.currentHexag                       # restore the last hexag's tile
            hexagLocation = self.theBoard.hexagDictionary[currentHexagNumber]
            locationFirst = int(hexagLocation[:2])                                  # parsing out the tuple for board to use
            locationSecond = int(hexagLocation[2:])
            boardLocation = (locationFirst, locationSecond)
            currentHexag = self.theBoard.findhexagTuple(boardLocation)
            print(f"new location reset {currentHexag.hexag_name}")
            #self.MainWindow.resetCityButton(currentHexag)
            if currentHexag:
                self.MainWindow.displayTile(currentHexag.hexagTile, currentHexagNumber, currentHexag.angle) # tile number, location,angle
            else:
                self.MainWindow.displayTile(0, currentHexagNumber, 0)               # set the previous hexag to blank  
        #else:                                                                       # this case there was no previous tile so just blank it out
        #    self.MainWindow.displayTile(0, self.MainWindow.currentHexag, 0)         # set the previous hexag to blank 
        self.MainWindow.currentHexag = location                                     # set the currentHexag to this new location
        company = self.MainWindow.currentCompany
        trainList = self.MainWindow.trainList[company]
        name = self.theBoard.hexagDictionary[location]
        locationFirst = int(name[:2])                                               # parsing out the tuple for board to use
        locationSecond = int(name[2:])
        boardLocation = (locationFirst, locationSecond)
        hexag = self.theBoard.findhexagTuple(boardLocation)
        self.theBoard.tileList = self.theBoard.checkForPlayableTile(boardLocation, company, trainList)    # ask theBoard for a list of playable tiles to display 
        self.theBoard.tileListIndex = 0
        if self.theBoard.tileList:
            tileNumber = self.theBoard.tileList[0][0]
            angle = self.theBoard.tileList[0][1]
            self.MainWindow.displayTile(tileNumber, location, angle)
            '''
            tile = self.theBoard.unplayedTileLookUp(self.theBoard.tileList[0][0])
            cityCount = hexag.city_count
            print(f"City count = {cityCount}")
            # cityCount of 0 means blank to rail with no cities, can have vilages though
            if cityCount == 1:                                      # single city or Boston or Baltimore
                if hexag.color == "":
                    self.MainWindow.drawCity(hexag, 1, 0, False, False)    # blank to Y1C
                    self.theBoard.setColor(hexag, "yellow")
                elif hexag.color == "yellow":
                    self.MainWindow.drawCity(hexag, 1, 1, False, False)    # Y1C to G1C and G1C to B1C
                    self.theBoard.setColor(hexag, "green")
                else:
                    self.theBoard.setColor(hexag, "brown")
            if cityCount == 2:                                      # 00 hexag doesn't matter if blank or green
                self.MainWindow.drawCity(hexag, 2, 0, False, False)        # blank to G2C and G2C to B2C
                if hexag.color == "":
                    self.theBoard.setColor(hexag, "green")
                else:
                    self.theBoard.setColor(hexag, "brown")
            if cityCount == 4:
                print(f"Hexag color = {hexag.color}")
                if hexag.color == "":
                    self.MainWindow.drawCity(hexag, 4, 1, False, False)    # blank to NY2  
                    self.theBoard.setColor(hexag, "green")
                else:
                    self.MainWindow.drawCity(hexag, 4, 2, False, False)    # NY2 to NY4
                    self.theBoard.setColor(hexag, "brown")
            '''

        
    def sameLocationClicked(self, location):
        print("******** Same Location")
        if self.theBoard.tileList:
            self.theBoard.tileListIndex +=1
            if self.theBoard.tileListIndex >= len(self.theBoard.tileList):
                self.theBoard.tileListIndex = 0
            ind = self.theBoard.tileListIndex
            self.MainWindow.displayTile(self.theBoard.tileList[ind][0], location, self.theBoard.tileList[ind][1])
            






           
            