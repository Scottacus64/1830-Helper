from Tile import Tile

class TilePile():
    def __init__(self):
        self.pile = []
        self.populate_pile()
    
    def populate_pile(self):
        #tile_id, upgrade_list, path_pairs, station list (owner followed by tuple associated with the station), village_count, city_count
        
        #----- yellow -----
        self.pile.append(Tile(1, (), ((2, 6),(3, 5)), (), 2, 0))  #1
        self.pile.append(Tile(2, (), ((1, 2),(3, 6)), (), 2, 0))  #2
        for i in range(0, 2):
            self.pile.append(Tile(3, (), [(4, 5)], (), 1, 0)) #3
            self.pile.append(Tile(4, (), [(3, 6)], (),  1, 0)) #4
        for i in range(0, 4):
            self.pile.append(Tile(7, [18, 26, 27, 28, 29], [(3, 4)], (), 0, 0))   #7
                             
        for i in range(0, 8):
            self.pile.append(Tile(8, [16, 19, 23, 24, 25, 28, 29], [(3, 5)], (), 0, 0))   #8
        for i in range(0, 7):
            self.pile.append(Tile(9, [18, 19, 20, 23, 24, 26, 27], [(3, 6)], (), 0, 0))   #9
        self.pile.append(Tile(55, (), ((2, 5),(3, 6)), (), 2, 0)) #55
        self.pile.append(Tile(56, (), ((1, 3),(2, 6)), (), 2, 0)) #56
        for i in range(0, 4):
            self.pile.append(Tile(57, [14, 15], [(3, 6)], [("blank", 0)], 0, 1))  #57
        for i in range(0, 2):
            self.pile.append(Tile(58, (), [(3, 5)], (), 1, 0))    #58
        self.pile.append(Tile(69, (), ((1, 5),(3, 6)), (), 2, 0)) #69
        
        #----- green -----
        for i in range(0, 3):
            self.pile.append(Tile(14, [63], ((2, 3),(2, 5),(2, 6),(3, 5),(3, 6),(5, 6)), (("blank", 0, 1, 2, 3, 4, 5), ("blank", 0, 1, 2, 3, 4, 5)), 0, 2))    #14
        for i in range(0, 2):
            self.pile.append(Tile(15, [63], ((1, 2),(1, 3),(1, 6),(2, 3),(2, 6),(3, 6)), (("blank", 0, 1, 2, 3, 4, 5), ("blank", 0, 1, 2, 3, 4, 5)), 0, 2))    #15
        self.pile.append(Tile(16, [43, 70], ((1, 3),(2, 6)), (), 0, 0))    #16
        self.pile.append(Tile(18, [43], ((1, 2),(3, 6)), (), 0, 0))    #18
        self.pile.append(Tile(19, [45, 46], ((1, 5),(3, 6)), (), 0, 0))    #19
        self.pile.append(Tile(20, [44, 47], ((2, 5),(3, 6)), (), 0, 0))    #20
        for i in range(0, 3):
            self.pile.append(Tile(23, [41, 43, 45, 47], ((1, 3),(3, 6)), (), 0, 0))    #23
            self.pile.append(Tile(24, [42, 43, 46, 47], ((3, 5),(3, 6)), (), 0, 0))    #24
        self.pile.append(Tile(25, [40, 45, 46], ((1, 3),(3, 5)), (), 0, 0))    #25
        self.pile.append(Tile(26, [42, 44, 45], ((2, 3),(3, 6)), (), 0, 0))    #26
        self.pile.append(Tile(27, [41, 44, 46], ((3, 4),(3, 6)), (), 0, 0))    #27
        self.pile.append(Tile(28, [39, 43, 46, 70], ((1, 3),(2, 3)), (), 0, 0))    #28
        self.pile.append(Tile(29, [39, 43, 45, 70], ((3, 4),(3, 5)), (), 0, 0))    #29
        for i in range(0, 2):
            self.pile.append(Tile(53, [61], ((1, 3),(1, 5),(3, 5)), (("blank", 0, 1, 2)), 0, 1))    #53
        self.pile.append(Tile(54, [62], ((1, 2),(5, 6)), (("blank", 0), ("blank", 1)), 0, 2))    #54
        for i in range(0, 2):
            self.pile.append(Tile(59, [64, 65, 66, 67, 68], [(2),(4)], (("blank", 0), ("blank", 1)), 0, 2))  #59, WEIRD CASE for "OO"      
        
        #----- brown -----
        self.pile.append(Tile(39, (), ((2, 2),(2, 4),(3, 4)), (), 0, 0))   #39
        self.pile.append(Tile(40, (), ((1, 3),(1, 5),(3, 5)), (), 0, 0))   #40
        for i in range(0, 2):
            self.pile.append(Tile(41, (), ((1, 3),(1, 6),(3, 6)), (), 0, 0))   #41
            self.pile.append(Tile(42, (), ((3, 5),(3, 6),(5, 6)), (), 0, 0))   #42
            self.pile.append(Tile(43, (), ((1, 2),(1, 3),(2, 6),(3, 6)), (), 0, 0))    #43
        self.pile.append(Tile(44, (), ((2, 3),(2, 5),(3, 6),(5, 6)), (), 0, 0))    #44
        for i in range(0, 2):
            self.pile.append(Tile(45, (), ((1, 2),(1, 3),(2, 5),(3, 5)), (), 0, 0))    #45
            self.pile.append(Tile(46, (), ((1, 3),(1, 4),(3, 5),(4, 5)), (), 0, 0))    #46
        self.pile.append(Tile(47, (), ((2, 5),(2, 6),(3, 6),(3, 5)), (), 0, 0))    #47
        for i in range(0, 2):
            self.pile.append(Tile(61, (), ((1, 3),(1, 5),(1, 6),(3, 4),(3, 6),(5, 6)), (("blank", 0, 1 , 2, 3, 4, 5)), 0, 1))  #61
        self.pile.append(Tile(62, (), ((1, 2),(5, 6)), (("blank", 0), ("blank", 0), ("blank", 1), ("blank", 1)), 0, 4))    #62
        for i in range(0, 3):
            self.pile.append(Tile(63, (), ((1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(2, 3),(2, 4),(2, 5),(2, 6),(3, 4),(3, 5),(3, 6),(4, 5),(4, 6),(5, 6)),(("blank", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), ("blank", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)), 0, 2))     #63
        self.pile.append(Tile(64, (), ((1, 2),(4, 6)), (("blank", 0), ("blank", 1)), 0, 2))  #64
        self.pile.append(Tile(65, (), ((2, 3),(4, 6)), (("blank", 0), ("blank", 1)), 0, 2))  #65
        self.pile.append(Tile(66, (), ((1, 6),(2, 5)), (("blank", 0), ("blank", 1)), 0, 2))  #66
        self.pile.append(Tile(67, (), ((2, 5),(4, 6)), (("blank", 0), ("blank", 1)), 0, 2))  #67
        self.pile.append(Tile(68, (), ((1, 4),(3, 6)), (("blank", 0), ("blank", 1)), 0, 2))  #68
        self.pile.append(Tile(70, (), ((1, 3),(1, 6),(2, 3),(2, 6)), (), 0, 0))    #70

    def getTiles(self):
        return self.pile
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        