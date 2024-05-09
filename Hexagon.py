from Tile import Tile

class Hexagon:
    def __init__(self, hex_id, vil_count, city_count, color, pc, rr_start):
        self.hex_id = hex_id
        self.vil_count = vil_count
        self.city_count = city_count
        self.color = color
        self.pc = pc
        self.rr_start = rr_start
        
    def printHex(self):
        print(self.name_id, " is a hex!")
        
        
        