
class Tile:
    def __init__(self, tile_id, upgrade_list, path_pairs, color, station_list, assoc_hex = None):
        self.tile_id = tile_id
        self.upgrade_list = upgrade_list
        self.path_pairs = path_pairs
        self.orientation = 0
        self.color = color
        self.station_list = station_list    #(("blank", 0), ("blank", 1)) station ownership, path pair associated with
        self.assoc_hex = assoc_hex
    
    def with_assoc_hex(cls, tile_id, upgrade_list, path_pairs, color, station_list, assoc_hex):
        return cls(tile_id, upgrade_list, path_pairs, color, station_list, assoc_hex)
        
    def printHex(self):
        print(self.name_id, " is a hex!")
    
    
    '''
    Functions needed
    -----------------
    place tile function():
        Parameters:
            hex_id (row, col)
            hex_color (grey, red, blank, yellow, green, brown)
        Functionality:
            Check if current company is able to place the hex_id passed in
            Check the color to see if it is a new tile being placed or an upgrade of an existing tile
            If upgrade:
                1) check to see if the current tile's upgrade_list is empty
                    a) if it is empty, there are no valid upgrades
                    b) if there is at least one value, then an upgrade may be possible
                2) see what trains are available to see if an upgrade is allowed to the next color
            If new tile:
                1) If it's NYC's turn, and their rr_start is blank, allow for tile placement
            
    
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    