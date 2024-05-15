#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:55:38 2024

@author: scottmiller
"""


from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPainter, QPolygon, QPixmap, QTransform
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
        self.setStyleSheet("background-color: transparent; border: none; padding: 0;")

        #self.setStyleSheet("background-color: transparent; border: 2px solid black;")
        self.theBoard = HexPushButton.board_instance                # Use the shared Board object

    '''
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
    '''
        
    def mousePressEvent(self, event):
        hexagon = QPolygon()
        buttonWidth = self.width()
        buttonHeight = self.height()
        #sideLength = min(buttonWidth, buttonHeight) // 2
        centerX = buttonWidth // 2
        centerY = buttonHeight // 2
        
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
                
    def rotate(self, angle):
        self.rotation_angle = angle
        if self.original_pixmap is not None:
            transform = QTransform()
            transform.rotate(self.rotation_angle)
            rotated_pixmap = self.original_pixmap.transformed(transform, Qt.SmoothTransformation)
            self.setQIcon(rotated_pixmap)
        
    def setPixmap(self, pixmap):
        super().setPixmap(pixmap)
        self.original_pixmap = pixmap


           
            
