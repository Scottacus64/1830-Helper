
class Tile:
    def __init__(self, tile_id, upgrade_list, station_list, village_count, city_count, color):
        self.tile_id = tile_id
        self.upgrade_list = upgrade_list
        self.orientation = 0
        self.station_list = station_list    #(("blank", 0), ("blank", 1)) station ownership, path pair associated with
        self.village_count = village_count
        self.city_count = city_count
        self.color = color
    
    def getCityCount(self):
        return self.city_count

    def printTile(self):
        print(f"if {self.tile_id} color {self.color}")
    
    def printhexag(self):
        print(self.name_id, " is a hexag!")
        
    def getId(self):
        return self.tile_id
        
    def getCompany(self):
        return self.station_list[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    