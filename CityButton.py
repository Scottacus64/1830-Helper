#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 10:36:52 2024

@author: scottmiller
"""
from PyQt5.QtWidgets import QPushButton

class CityButton(QPushButton):
    def __init__(self, name, main_window, buttonActive=False, citySet=False, company="0", parent=None):
        super().__init__(name, parent)
        self.name = name
        self.MainWindow = main_window
        self.buttonActive = buttonActive
        self.citySet = citySet
        self.company = company

    def getActive(self):
        return self.buttonActive
    
    def setActive(self, status):
        self.buttonActive = status

    def getCompany(self):
        return self.company

    def setCompany(self, company):
        self.company = company

    def getCitySet(self):
        return self.citySet
        
    def setCitySet(self, status):
        self.citySet = status
        
    def printCityButton(self):
        print(f"Button {self.name} active {self.getActive()} set {self.getCitySet()} company {self.getCompany()}")


       
