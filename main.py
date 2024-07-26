"""
Created on Sun May  5 07:55:38 2024
@author: scottmiller

The game consists of a Board that is populated with Hexagons.   The Hexagons have:
hexag_id (5,5), hexag_name (0505), vil_count, city_count, station_count, rr_start, entryExitStation, voidSides, hexagTile, angle, color

There are also Tiles that are formed into a TilePile.  These Tiles have:
tile_id (15), upgrade_list, path_pairs, station_list, village_count, city_count, color

These is also a MainWindow UI that is populated with many different types of QPushButtons, these include HexagPushButton, company, city, train and station push buttons
"""

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())