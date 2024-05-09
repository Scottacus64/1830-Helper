from Hexagon import Hexagon


class Board:
    def __init__(self):
        self.board_hexagons = []
        self.tiles_on_the_board = []
        self.initialze_standard_board()


    def initialze_standard_board(self):
        # NOTE: Odd rows only have odd columns, even rows only have even columns
        '''
        This function will build out a standard board of 1830, it'll do so by categorizing each hex
        Categories include:
        -----------------------
            off_board_hexes
            
            on_board_hexes
    
            grey_hexes
            
            red_hexes
            
            yellow_hexes
            
            non_colored_hexes
            
            mountain_hexes
            
            river_hexes
            
            one_city_hexes
            
            two_city_hexes
            
            one_village_hexes
            
            two_villlage_hexes
            
            rr_start_hexes
            
            private_comp_hexes
        '''
        
        # ----- off_board_hexes -----
        off_board_hexes = [(1, 1), (1, 3), (1, 5), (1, 7), (1, 13), (1, 15), (1, 21), (1, 23),
                         (2, 2), (2, 4), (2, 6), (2, 8),
                         (3, 1), (3, 3), (3, 5),
                         (5, 1),
                         (7, 1), (7, 21), (7, 23),
                         (8, 20), (8, 22), (8, 24),
                         (9, 21), (9, 23),
                         (10, 16), (10, 18), (10, 20), (10, 22), (10, 24),
                         (11, 1), (11, 3), (11, 5), (11, 7), (11, 9), (11, 11), (11, 17), (11, 19), (11, 21), (11, 23)]
        
        # ----- on_board_hexes -----
        on_board_hexes = []
        for i in range(1, 12): # Rows A-K
            if i % 2 == 1:
                for j in range(1, 24, 2): # Add all valid hexes in odd rows (ones that aren't in off_board_hexes)
                    if((i, j) not in off_board_hexes):
                        on_board_hexes.append((i, j))
            else:
                for j in range(2, 25, 2): # Add all valid hexes in even rows (ones that aren't in off_board_hexes)
                    if((i, j) not in off_board_hexes):
                        on_board_hexes.append((i, j))
        
        # ----- grey_hexes -----
        grey_hexes = [(1, 17), (1, 19),
                      (3, 15),
                      (4, 2), (4, 14), (4, 24),
                      (5, 9),
                      (6, 6), (6, 24),
                      (8, 12),
                      (9, 19),
                      (11, 15)]
        
        # ----- red_hexes -----
        red_hexes = [(1, 9), (1, 11),
                     (2, 24),
                     (6, 2),
                     (9, 1),
                     (10, 2),
                     (11, 13)]
        
        # ----- yellow_hexes -----
        yellow_hexes = [(4, 10),
                        (5, 5), (5, 11), (5, 23),
                        (7, 19),
                        (9, 15)]

        
        # ----- one_city_hexes -----
        one_city_hexes = [(1, 19),
                          (2, 10), (2, 16),
                          (4, 2), (4, 14),
                          (5, 19), (5, 23),
                          (6, 4), (6, 6), (6, 16), (6, 22),
                          (8, 4), (8, 10), (8, 12), (8, 16),
                          (9, 15),
                          (10, 14),
                          (11, 15)]
        
        # ----- two_city_hexes -----
        two_city_hexes = [((4, 10), "OO"),
                          ((5, 5), "OO"), ((5, 11), "OO"),
                          ((7, 19), "NY"),
                          ((8, 18), "OO")]
        
        # ----- one_village_hexes -----
        one_village_hexes = [(2, 20),
                             (3, 15),
                             (4, 4),
                             (5, 7),
                             (6, 10), (6, 24),
                             (9, 19)]
        
        # ----- two_vilage_hexes -----
        two_village_hexes = [(6, 20),
                             (7, 7), (7, 17)]
        
        # ----- rr_start_hexes -----
        rr_start_hexes = [((1, 19), "Canadian Pacific RR"),
                          ((5, 11), "Erie RR"), ((5, 19), "New York Central RR"), ((5, 23), "Boston & Maine RR"),
                          ((6, 6), "Chesapeake & Ohio RR"),
                          ((7, 19), "New York & New Haven RR"),
                          ((8, 12), "Pennsylvania RR"),
                          ((9, 15), "Baltimore & Ohio RR")]
        
        # -----private_comp_hexes -----
        private_comp_hexes = [((2, 20), "Champlain & St Lawrence"),
                              ((4, 18), "Mohawk & Hudson"),
                              ((6, 16), "Delaware & Hudson"),
                              ((7, 15), "Schuykill Valley"),
                              ((8, 18), "Camden & Amboy"),
                              ((9, 13), "Baltimore & Ohio"), ((9, 15), "Baltimore & Ohio")]
        
        # Create the hexagon objects
        for hex in on_board_hexes:
            #-----Hex ID-----
            hex_id = hex
            
            #-----Village Count-----
            if(hex in one_village_hexes):
                vil_count = 1
            elif(hex in two_village_hexes):
                vil_count = 2
            else:
                vil_count = 0
            
            #-----City Count-----
            hex_city_count_ind = None
            
            if(hex in one_city_hexes): # Case for checking if there is only one city
                city_count = 1
            else: # Case hit for two cities or no cities
                for ind, item in enumerate(two_city_hexes): # Find if there is matching hex and get its ind
                    if(item[0] == hex):
                        hex_city_count_ind = ind
                        break
                if hex_city_count_ind is None: # If there was no match, then city_count is 0
                    city_count = 0
                else:
                    city_count = two_city_hexes[hex_city_count_ind][1] # If there are two cities, then return OO or NY
            
            #-----Color-----
            if(hex in grey_hexes):
                color = "grey"
            elif(hex in red_hexes):
                color = "red"
            elif(hex in yellow_hexes):
                color = "yellow"
            else:
                color = "blank"
        
            #-----Private Company-----
            hex_pc_ind = None
            for ind, item in enumerate(private_comp_hexes): # Find if there is matching hex and get its ind
                if(item[0] == hex):
                    hex_pc_ind = ind
                    break
            if hex_pc_ind is None: # If there was no match, "", otherwise set PC to its string PC value
                pc = ""
            else:
                pc = private_comp_hexes[hex_pc_ind][1]
        
            #-----Railroad Start-----
            hex_rr_ind = None
            for ind, item in enumerate(rr_start_hexes):
                if(item[0] == hex):
                    hex_rr_ind = ind
                    break
            if hex_rr_ind is None:
                rr_start = ""
            else:
                rr_start = rr_start_hexes[hex_rr_ind][1]
        
            # Initialize the hex object
            hex_to_append = Hexagon(hex_id, vil_count, city_count, color, pc, rr_start)
            self.board_hexagons.append(hex_to_append)
    
    # Create tiles that have rail on them initially
    # Given an id, return its corresponding hex
    def find_hex_by_id(self, id_to_search_for):
        for a_hex in self.board_hexagons:
            if a_hex.hex_id == id_to_search_for:
                return a_hex    #return the hex upon a match
        return None     #If there was no match, return None
    
    def place_initial_tiles(self):
        
    
    
    def print_board(self):
        for a_hex in self.board_hexagons:
            print(a_hex.hex_id, a_hex.vil_count, a_hex.city_count, a_hex.color, a_hex.pc, a_hex.rr_start)
            print("---------------")

























