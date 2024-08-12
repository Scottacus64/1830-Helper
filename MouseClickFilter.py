#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 07:55:20 2024

@author: scottmiller
"""
from PyQt5.QtCore import QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QMouseEvent

class MouseClickFilter(QObject):
    mouseClicked = pyqtSignal()  # Define the signal here

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.local_x = None  
        self.local_y = None 
        self.counter = 0
        self.oldX = 0
        self.oldY = 0

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and isinstance(event, QMouseEvent):
            local_pos = self.window.mapFromGlobal(event.globalPos())
            self.local_x = local_pos.x() 
            self.local_y = local_pos.y() 
            self.mouseClicked.emit()
            '''
            if self.counter == 1:
                m = (self.local_y - self.oldY)/(self.local_x - self.oldX)
                b = self.local_y - (self.local_x * m)
                print(f"m = {m} and b = {b}")
            self.oldX = self.local_x
            self.oldY = self.local_y     
            self.counter +=1
            if self.counter > 1:
                self.counter = 0
            return True
            '''
        return super().eventFilter(obj, event)

    # Method to retrieve the x coordinate
    def getLocalX(self):
        return self.local_x

    # Method to retrieve the y coordinate
    def getLocalY(self):
        return self.local_y
