
class Tile:
    def __init__(self, tile_id, upgrade_list, path_pairs, station_list, village_count, city_count):
        self.tile_id = tile_id
        self.upgrade_list = upgrade_list
        self.path_pairs = path_pairs
        self.orientation = 0
        self.station_list = station_list    #(("blank", 0), ("blank", 1)) station ownership, path pair associated with
        self.village_count = village_count
        self.city_count = city_count
    
    
    def with_assoc_hex(cls, tile_id, upgrade_list, path_pairs, station_list, village_count, city_count):
        return cls(tile_id, upgrade_list, path_pairs, station_list, village_count, city_count)
    
    
    def printHex(self):
        print(self.name_id, " is a hex!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    