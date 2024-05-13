#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:55:38 2024

@author: scottmiller
"""


from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPainter, QPolygon, QPixmap
from PyQt5.QtCore import QPoint, Qt
import math
from Board import Board

class HexPushButton(QPushButton):
    
    board_instance = Board()                            # Class variable to hold the shared Board object
    board_instance.print_board()
    
    def __init__(self, name, main_window, parent=None):
        super().__init__(parent)
        self.name = name
        self.MainWindow = main_window
        self.setFlat(True)
        self.rotation_angle = 0
        self.setStyleSheet("background-color: transparent; border: 2px solid black;")
        self.theBoard = HexPushButton.board_instance                # Use the shared Board object

    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        hexagon = QPolygon()
        buttonWidth = self.width()
        buttonHeight = self.height()
        sideLength = min(buttonWidth, buttonHeight) // 2
        centerX = buttonWidth // 2
        centerY = buttonHeight // 2
        rotation_angle = math.pi / 6
        
        for i in range(6):
            angle = 2 * math.pi * i / 6 + rotation_angle
            x = centerX + sideLength * math.cos(angle)
            y = centerY + sideLength * math.sin(angle)
            hexagon.append(QPoint(int(x), int(y)))

        painter.drawPolygon(hexagon)
        
    def mousePressEvent(self, event):
        hexagon = QPolygon()
        buttonWidth = self.width()
        buttonHeight = self.height()
        #sideLength = min(buttonWidth, buttonHeight) // 2
        centerX = buttonWidth // 2
        centerY = buttonHeight // 2
        
        hexDictionary = {
            "0101":1 , "0103":2,  "0105":3,  "0107":4, " 0109":5,  "0111":6,  "0113":7,  "0115":8,  "0117":9,  "0119":10, "0121":11, "0123":12,
            "0202":13, "0204":14, "0206":15, "0208":16, "0210":17, "0212":18, "0214":19, "0216":20, "0218":21, "0220":22, "0222":23, "0224":24,
            "0301":25, "0303":26, "0305":27, "0307":28, "0309":29, "0311":30, "0313":31, "0315":32, "0317":33, "0319":34, "0321":35, "0323":36,
            "0402":37, "0404":38, "0406":39, "0408":40, "0410":41, "0412":42, "0414":43, "0416":44, "0418":45, "0420":46, "0422":47, "0424":48,
            "0501":49, "0503":50, "0505":51, "0507":52, "0509":53, "0511":54, "0513":55, "0515":56, "0517":57, "0519":58, "0521":59, "0523":60,
            "0602":61, "0604":62, "0606":63, "0608":64, "0610":65, "0612":66, "0614":67, "0616":68, "0618":69, "0620":70, "0622":71, "0624":72,
            "0701":73, "0703":74, "0705":75, "0707":76, "0709":77, "0711":78, "0713":79, "0715":80, "0717":81, "0719":82, "0721":83, "0723":84,
            "0802":85, "0804":86, "0806":87, "0808":88, "0810":89, "0812":90, "0814":91, "0816":92, "0818":93, "0820":94, "0822":95, "0824":96,
            "0901":97, "0903":98, "0905":99, "0907":100, "0909":101, "0911":102, "0913":103, "0915":104, "0917":105, "0919":106, "0921":107, "0923":108,
            "1002":109, "1004":110, "1006":111, "1008":112, "1010":113, "1012":114, "1014":115, "1016":116, "1018":117, "1020":118, "1022":119, "1024":120,
            "1101":121, "1103":122, "1105":123, "1107":124, "1109":125, "1111":126, "1113":127, "1115":128, "1117":129, "1119":130, "1121":131, "1123":132
            }
        
        for i in range(6):
            x = centerX + buttonWidth * math.cos(2 * math.pi * i / 6)        # uses radians for trig functions (2 Pi * angle/360)
            y = centerY + buttonHeight * math.sin(2 * math.pi * i / 6)
            hexagon.append(QPoint(int(x), int(y)))
        
        if hexagon.containsPoint(event.pos(), Qt.OddEvenFill):              # if the mouse is clicked inside a hex
            super().mousePressEvent(event)
            tileList = []                                                   # list for the tile and orientation
            locationFirst = int(self.name[:2])                              # parsing out the tuple for board to use
            locationSecond = int(self.name[2:])
            boardLocation = (locationFirst, locationSecond)
            location = hexDictionary[self.name]                             # check the hex dictionary to see which label to put the tile on
            if location != self.MainWindow.lastTile and self.MainWindow.lastTile > 0:
                self.MainWindow.displayTile(0, self.MainWindow.lastTile, 0)
            self.MainWindow.lastTile = location  
            tileList = self.theBoard.checkForPlayableTile(boardLocation, 1, [0,0,2,0])  # ask theBoard for a playable tile to display 
            self.MainWindow.displayTile(tileList[0], location, tileList[1])
                

           
            
