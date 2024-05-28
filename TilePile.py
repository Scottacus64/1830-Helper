from Tile import Tile

class TilePile():
    def __init__(self):
        self.pile = []
        self.populate_pile()
    
    def populate_pile(self):
        #tile_id, upgrade_list, path_pairs, station list (owner followed by tuple associated with the station), village_count, city_count
        
        #----- yellow -----
        self.pile.append(Tile(1, (), [(2, 6),(3, 5)], (), 2, 0))  #1
        self.pile.append(Tile(2, (), [(1, 2),(3, 6)], (), 2, 0))  #2
        for i in range(0, 2):
            self.pile.append(Tile(3, (), [(4, 5)], (), 1, 0)) #3
            self.pile.append(Tile(4, (), [(3, 6)], (),  1, 0)) #4
        for i in range(0, 4):
            self.pile.append(Tile(7, [(18,2), (26,1), (27,0), (28,1), (29,0)], [(3, 4)], (), 0, 0))   #7
                             
        for i in range(0, 8):
            self.pile.append(Tile(8, [(16,2), (16,3), (19,4), (23,2), (24,0), (25,0), (25,2), (28,2), (29,0)], [(3, 5)], (), 0, 0))   #8
        for i in range(0, 7):
            self.pile.append(Tile(9, [(18,0), (18,3), (19,0), (19,3), (20,0), (20,1), (20,3), (20,4), (23,0), (23,3), (24,0), (24,3), (26,0), (26,3), (27,0), (27,3)], [(3, 6)], (), 0, 0))   #9
        self.pile.append(Tile(55, (), [(2, 5),(3, 6)], (), 2, 0)) #55
        self.pile.append(Tile(56, (), [(1, 3),(2, 6)], (), 2, 0)) #56
        for i in range(0, 4):
            self.pile.append(Tile(57, [(14,0), (14,1), (14,3), (14,4), (15,0), (15,3)], [(3, 6)], [("blank", 0)], 0, 1))  #57
        for i in range(0, 2):
            self.pile.append(Tile(58, (), [(3, 5)], (), 1, 0))    #58
        self.pile.append(Tile(69, (), [(1, 5),(3, 6)], (), 2, 0)) #69
        
        #----- green -----
        for i in range(0, 3):
            self.pile.append(Tile(14, [(63,0)], [(2, 3),(2, 5),(2, 6),(3, 5),(3, 6),(5, 6)], (("blank", 0, 1, 2, 3, 4, 5), ("blank", 0, 1, 2, 3, 4, 5)), 0, 2))    #14
        for i in range(0, 2):
            self.pile.append(Tile(15, [(63,0)], [(1, 2),(1, 3),(1, 6),(2, 3),(2, 6),(3, 6)], (("blank", 0, 1, 2, 3, 4, 5), ("blank", 0, 1, 2, 3, 4, 5)), 0, 2))    #15
        self.pile.append(Tile(16, [(43,0), (43,1), (70,0), (70,1)], [(1, 3),(2, 6)], (), 0, 0))    #16
        self.pile.append(Tile(18, [(43,0)], [(1, 2),(3, 6)], (), 0, 0))    #18
        self.pile.append(Tile(19, [(45,4), (46,2)], [(1, 5),(3, 6)], (), 0, 0))    #19
        self.pile.append(Tile(20, [(44,0), (44,3), (47,0), (47,3)], [(2, 5),(3, 6)], (), 0, 0))    #20
        for i in range(0, 3):
            self.pile.append(Tile(23, [(41,0), (43,0), (45,4), (47,2)], [(1, 3),(3, 6)], (), 0, 0))    #23
            self.pile.append(Tile(24, [(42,0), (43,3), (46,2), (47,0)], [(3, 5),(3, 6)], (), 0, 0))    #24
        self.pile.append(Tile(25, [(40,0), (45,0), (46,0)], [(1, 3),(3, 5)], (), 0, 0))    #25
        self.pile.append(Tile(26, [(42,3), (44,0), (45,1)], [(2, 3),(3, 6)], (), 0, 0))    #26
        self.pile.append(Tile(27, [(41,3), (44,1), (46,5)], [(3, 4),(3, 6)], (), 0, 0))    #27
        self.pile.append(Tile(28, [(39,5), (43,1), (46,4), (70,0)], [(1, 3),(2, 3)], (), 0, 0))    #28
        self.pile.append(Tile(29, [(39,1), (43,2), (45,2), (70,3)], [(3, 4),(3, 5)], (), 0, 0))    #29
        for i in range(0, 2):
            self.pile.append(Tile(53, [(61,0), (61,1), (61,2), (61,3), (61,4), (61,5)], [(1, 3),(1, 5),(3, 5)], (("blank", 0, 1, 2, 3, 4, 5)), 0, 1))    #53
        self.pile.append(Tile(54, [(62,0)], [(1, 2),(5, 6)], (("blank", 0), ("blank", 1)), 0, 2))    #54
        for i in range(0, 2):
            self.pile.append(Tile(59, [(64,0), (64,1), (64,2), (64,3), (64,4), (64,5),
                                       (65,0), (65,1), (65,2), (65,3), (65,4), (65,5),
                                       (66,0), (66,1), (66,2), (66,3), (66,4), (66,5),
                                       (67,0), (67,1), (67,2), (67,3), (67,4), (67,5),
                                       (68,0), (68,1), (68,2), (68,3), (68,4), (68,5)], [(2,0),(4,0)], (("blank", 0), ("blank", 1)), 0, 2))  #59 "OO"      
        
        #----- brown -----
        self.pile.append(Tile(39, (), [(2, 2),(2, 4),(3, 4)], (), 0, 0))   #39
        self.pile.append(Tile(40, (), [(1, 3),(1, 5),(3, 5)], (), 0, 0))   #40
        for i in range(0, 2):
            self.pile.append(Tile(41, (), [(1, 3),(1, 6),(3, 6)], (), 0, 0))   #41
            self.pile.append(Tile(42, (), [(3, 5),(3, 6),(5, 6)], (), 0, 0))   #42
            self.pile.append(Tile(43, (), [(1, 2),(1, 3),(2, 6),(3, 6)], (), 0, 0))    #43
        self.pile.append(Tile(44, (), [(2, 3),(2, 5),(3, 6),(5, 6)], (), 0, 0))    #44
        for i in range(0, 2):
            self.pile.append(Tile(45, (), [(1, 2),(1, 3),(2, 5),(3, 5)], (), 0, 0))    #45
            self.pile.append(Tile(46, (), [(1, 3),(1, 4),(3, 5),(4, 5)], (), 0, 0))    #46
        self.pile.append(Tile(47, (), [(2, 5),(2, 6),(3, 6),(3, 5)], (), 0, 0))    #47
        for i in range(0, 2):
            self.pile.append(Tile(61, (), [(1, 3),(1, 5),(1, 6),(3, 5),(3, 6),(5, 6)], (("blank", 0, 1 , 2, 3, 4, 5)), 0, 1))  #61
        self.pile.append(Tile(62, (), [(1, 2),(5, 6)], (("blank", 0), ("blank", 0), ("blank", 1), ("blank", 1)), 0, 4))    #62
        for i in range(0, 3):
            self.pile.append(Tile(63, (), [(1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(2, 3),(2, 4),(2, 5),(2, 6),(3, 4),(3, 5),(3, 6),(4, 5),(4, 6),(5, 6)],(("blank", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), ("blank", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)), 0, 2))     #63
        self.pile.append(Tile(64, (), [(1, 2),(4, 6)], (("blank", 0), ("blank", 1)), 0, 2))  #64
        self.pile.append(Tile(65, (), [(2, 3),(4, 6)], (("blank", 0), ("blank", 1)), 0, 2))  #65
        self.pile.append(Tile(66, (), [(1, 6),(2, 5)], (("blank", 0), ("blank", 1)), 0, 2))  #66
        self.pile.append(Tile(67, (), [(2, 5),(4, 6)], (("blank", 0), ("blank", 1)), 0, 2))  #67
        self.pile.append(Tile(68, (), [(1, 4),(3, 6)], (("blank", 0), ("blank", 1)), 0, 2))  #68
        self.pile.append(Tile(70, (), [(1, 3),(1, 6),(2, 3),(2, 6)], (), 0, 0))    #70
        
        #----- special tiles for cities and OO -----
        self.pile.append(Tile(80, [(53,1)], [(1,3)], [("B&O", 0)], 0, 1))     # Baltimore
        self.pile.append(Tile(81, [(53,0)], [(1,3)], [("B&M", 0)], 0, 1))     # Boston
        self.pile.append(Tile(82, [(54,5)], [(1,0), (4,0)], [("NNH", 0), ("blank", 1)], 0, 2))   # New York
        for i in range(4):
            self.pile.append(Tile(83, [(59,0), (59,1), (59,2), (59,3), (59,4), (59,5)], (), (), 0, 2))   # blank "00"
        
        
    def getTiles(self):
        return self.pile
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        