#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:45:58 2024

@author: scottmiller
"""
from PyQt5.QtCore import QObject, QEvent, QMouseEvent

class GlobalMouseClickFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and isinstance(event, QMouseEvent):
            x = event.globalX()
            y = event.globalY()
            print(f"Global Mouse clicked at: ({x}, {y})")
        return super().eventFilter(obj, event)
