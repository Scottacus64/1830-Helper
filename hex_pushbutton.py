
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import  QPolygon, QTransform, QIcon
from PyQt5.QtCore import QPoint, Qt
from Board import Board

class HexPushButton(QPushButton):
    
    board_instance = Board()  # Class variable to hold the shared Board object
    board_instance.print_board()
    
    def __init__(self, name, main_window, parent=None):
        super().__init__(parent)
        self.name = name
        self.MainWindow = main_window
        self.setFlat(True)
        self.rotation_angle = 0
        self.setStyleSheet("background-color: transparent; border: none; padding: 0;")
        self.theBoard = HexPushButton.board_instance  # Use the shared Board object
        self.rotationAngle = 0
        self.tileList = []
        self.tileListIndex = 0
        
        # this is a list of all tile names from 1 to 70 in ascending order
        self.tileKey = [
            "t1", "t2", "t3", "t4", "t7", "t8", "t9", 
            "t14", "t15", "t16", "t18", "t19",
            "t20", "t23", "t24", "t25", "t26", "t27", "t28", "t29", 
            "t39", "t40", "t41", 't42', "t43", "t44", "t45", "t46", "t47",
            "t53", "t54,", "t55", "t56", "t57", "t58", "t59",
            "t61", "t62", "t63", "t64", "t65", "t66", "t67", "t68", "t69", "t70"
            ]

    def mousePressEvent(self, event):
        hexagon = QPolygon()
        
        hexDictionary = {
            "0210":0, "0212":1, "0214":2, "0216":3, "0218":4, "0220":5, "0222":6, 
            "0307":7, "0309":8, "0311":9, "0313":10, "0317":11, "0319":12, "0321":13, "0323":14,
            "0402":15, "0404":16, "0406":17, "0408":18, "0410":19, "0412":20, "0414":21, "0416":22, "0418":23, "0420":24,  "0422":25, 
            "0503":26, "0505":27, "0507":28, "0511":29, "0513":30, "0515":31, "0517":32, "0519":33, "0521":34, "0523":35,
            "0604":36, "0608":37, "0610":38, "0612":39, "0614":40, "0616":41, "0618":42, "0620":43, "0622":44, 
            "0703":45, "0705":46, "0707":47, "0709":48, "0711":49, "0713":50, "0715":51, "0717":52, "0719":53,
            "0802":54, "0804":55, "0806":56, "0808":57, "0810":58, "0814":59, "0816":60, "0818":61, 
            "0903":62, "0905":63, "0907":64, "0909":65, "0911":66, "0913":67, "0915":68, "0917":69, 
            "1004":70, "1006":71, "1008":72, "1010":73, "1012":74, "1014":75, 
            "1115":76
            }
        
        hexPoints = [(58,0), (0,29), (0,87), (58,117), (117,87), (117,29)]  # these are the corners of the hexagon
        for i in range(6):
            hexagon.append(QPoint(hexPoints[i][0], hexPoints[i][1]))           
        if hexagon.containsPoint(event.pos(), Qt.OddEvenFill):              # if the mouse is clicked inside a hex
            super().mousePressEvent(event)          
            location = hexDictionary[self.name]                             # check the hex dictionary to get the hex value
            if location != self.MainWindow.lastTile: #and self.MainWindow.lastTile > 0:   # if the hex clicked is new
                self.newLocationClicked((location))
            else:
                 self.sameLocationClicked(location)
            
            # This might be used to color in tiles that are a part of a train route
            #self.MainWindow.colorTiles(tileList[0], location, tileList[1], 0)
            
            
    def newLocationClicked(self, location):
        self.MainWindow.displayTile(0, self.MainWindow.lastTile, 0)                         # set the previous hex to blank
        self.MainWindow.lastTile = location                                                 # set the lastTile to this new location
        company = self.MainWindow.currentCompany
        trainList = self.MainWindow.trainList[company]
        locationFirst = int(self.name[:2])                              # parsing out the tuple for board to use
        locationSecond = int(self.name[2:])
        boardLocation = (locationFirst, locationSecond)
        self.tileList = self.theBoard.checkForPlayableTile(boardLocation, company, trainList)    # ask theBoard for a list of playable tiles to display 
        self.tileListIndex = 0
        self.MainWindow.displayTile(self.tileList[0][0], location, self.tileList[0][1])
        
        
    def sameLocationClicked(self, location):
        self.tileListIndex +=1
        if self.tileListIndex >= len(self.tileList):
            self.tileListIndex = 0
        ind = self.tileListIndex
        self.MainWindow.displayTile(self.tileList[ind][0], location, self.tileList[ind][1])


    def findOverlappingButtons(self, pos):
        overlapping_buttons = []
        for button in self.MainWindow.hexButtons:
            if button.geometry().contains(self.mapToGlobal(pos)):
                overlapping_buttons.append(button)
        return overlapping_buttons



           
            
