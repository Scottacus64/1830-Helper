#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 08:06:13 2024

@author: scottmiller
"""

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QTransform
#import os
from PyQt5.QtCore import Qt

class RotatableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        

    def setPixmap(self, pixmap):
        super().setPixmap(pixmap)
        self.original_pixmap = pixmap

    def resetRotation(self):
        self.rotation_angle = 0
        self.setPixmap(self.original_pixmap)
    

    def rotate(self, angle):
        self.rotation_angle = angle
        if self.original_pixmap is not None:
            transform = QTransform()
            transform.rotate(self.rotation_angle)
            rotated_pixmap = self.original_pixmap.transformed(transform, Qt.SmoothTransformation)
            self.setPixmap(rotated_pixmap)
    
    
       
