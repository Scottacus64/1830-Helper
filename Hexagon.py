

class Hexagon:
    def __init__(self, hex_id, hex_name, vil_count, city_count, station_count, rr_start, entryExitStation, voidSides, hexTile, angle):
        self.hex_id = hex_id
        self.hex_name = hex_name
        self.vil_count = vil_count
        self.city_count = city_count
        self.station_count = station_count
        self.rr_start = rr_start
        self.entryExitStation = entryExitStation
        self.voidSides = voidSides
        self.hexTile = hexTile
        self.angle = angle
        
    def printHex(self):
        print(self.name_id, " is a hex!")
        

        
        
        