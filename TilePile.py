from Tile import Tile

class TilePile():
    def __init__(self):
        self.pile = []
        self.populate_pile()
    
    def populate_pile(self):
        #tile_id, upgrade_list, path_pairs, color, png
        
        #----- yellow -----
        self.pile.append(Tile(1, (), ((2, 6),(3, 5)), "yellow", ()))  #1
        self.pile.append(Tile(2, (), ((1, 2),(3, 6)), "yellow", ()))  #2
        for i in range(0, 2):
            self.pile.append(Tile(3, (), ((4, 5)), "yellow", ())) #3
            self.pile.append(Tile(4, (), ((3, 6)), "yellow", ())) #4
        for i in range(0, 4):
            self.pile.append(Tile(7, (18, 26, 27, 28, 29), ((3, 4)), "yellow", ()))   #7
                             
        for i in range(0, 8):
            self.pile.append(Tile(8, (16, 19, 23, 24, 25, 28, 29), ((3, 5)), "yellow", ()))   #8
        for i in range(0, 7):
            self.pile.append(Tile(9, (18, 19, 20, 23, 24, 26, 27), ((3, 6)), "yellow", ()))   #9
        self.pile.append(Tile(55, (), ((2, 5),(3, 6)), "yellow", ())) #55
        self.pile.append(Tile(56, (), ((1, 3),(2, 6)), "yellow", ())) #56
        for i in range(0, 4):
            self.pile.append(Tile(57, (14, 15), ((3, 6)), "yellow", (("blank", 0))))  #57
        for i in range(0, 2):
            self.pile.append(Tile(58, (), ((3, 5)), "yellow", ()))    #58
        self.pile.append(Tile(69, (), ((1, 5),(3, 6)), "yellow", ())) #69
        
        #----- green -----
        for i in range(0, 3):
            self.pile.append(Tile(14, (63), ((2, 3),(2, 5),(2, 6),(3, 5),(3, 6),(5, 6)), "green", (("blank", 0, 1, 2, 3, 4, 5), ("blank", 0, 1, 2, 3, 4, 5))))    #14
        for i in range(0, 2):
            self.pile.append(Tile(15, (63), ((1, 2),(1, 3),(1, 6),(2, 3),(2, 6),(3, 6)), "green", (("blank", 0, 1, 2, 3, 4, 5), ("blank", 0, 1, 2, 3, 4, 5))))    #15
        self.pile.append(Tile(16, (43, 70), ((1, 3),(2, 6)), "green", ()))    #16
        self.pile.append(Tile(18, (43), ((1, 2),(3, 6)), "green", ()))    #18
        self.pile.append(Tile(19, (45, 46), ((1, 5),(3, 6)), "green", ()))    #19
        self.pile.append(Tile(20, (44, 47), ((2, 5),(3, 6)), "green", ()))    #20
        for i in range(0, 3):
            self.pile.append(Tile(23, (41, 43, 45, 47), ((1, 3),(3, 6)), "green", ()))    #23
            self.pile.append(Tile(24, (42, 43, 46, 47), ((3, 5),(3, 6)), "green", ()))    #24
        self.pile.append(Tile(25, (40, 45, 46), ((1, 3),(3, 5)), "green", ()))    #25
        self.pile.append(Tile(26, (42, 44, 45), ((2, 3),(3, 6)), "green", ()))    #26
        self.pile.append(Tile(27, (41, 44, 46), ((3, 4),(3, 6)), "green", ()))    #27
        self.pile.append(Tile(28, (39, 43, 46, 70), ((1, 3),(2, 3)), "green", ()))    #28
        self.pile.append(Tile(29, (39, 43, 45, 70), ((3, 4),(3, 5)), "green", ()))    #29
        for i in range(0, 2):
            self.pile.append(Tile(53, (61), ((1, 3),(1, 5),(3, 5)), "green", (("blank", 0, 1, 2))))    #53
        self.pile.append(Tile(54, (62), ((1, 2),(5, 6)), "green", (("blank", 0), ("blank", 1))))    #54
        for i in range(0, 2):
            self.pile.append(Tile(59, (64, 65, 66, 67, 68), ((2),(4)), "green", (("blank", 0), ("blank", 1))))  #59, WEIRD CASE for "OO"      
        
        #----- brown -----
        self.pile.append(Tile(39, (), ((2, 2),(2, 4),(3, 4)), "brown", ()))   #39
        self.pile.append(Tile(40, (), ((1, 3),(1, 5),(3, 5)), "brown", ()))   #40
        for i in range(0, 2):
            self.pile.append(Tile(41, (), ((1, 3),(1, 6),(3, 6)), "brown", ()))   #41
            self.pile.append(Tile(42, (), ((3, 5),(3, 6),(5, 6)), "brown", ()))   #42
            self.pile.append(Tile(43, (), ((1, 2),(1, 3),(2, 6),(3, 6)), "brown", ()))    #43
        self.pile.append(Tile(44, (), ((2, 3),(2, 5),(3, 6),(5, 6)), "brown", ()))    #44
        for i in range(0, 2):
            self.pile.append(Tile(45, (), ((1, 2),(1, 3),(2, 5),(3, 5)), "brown", ()))    #45
            self.pile.append(Tile(46, (), ((1, 3),(1, 4),(3, 5),(4, 5)), "brown", ()))    #46
        self.pile.append(Tile(47, (), ((2, 5),(2, 6),(3, 6),(3, 5)), "brown", ()))    #47
        for i in range(0, 2):
            self.pile.append(Tile(61, (), ((1, 3),(1, 5),(1, 6),(3, 4),(3, 6),(5, 6)), "brown", (("blank", 0, 1 , 2, 3, 4, 5))))  #61
        self.pile.append(Tile(62, (), ((1, 2),(5, 6)), "brown", (("blank", 0), ("blank", 0), ("blank", 1), ("blank", 1))))    #62
        for i in range(0, 3):
            self.pile.append(Tile(63, (), ((1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(2, 3),(2, 4),(2, 5),(2, 6),(3, 4),(3, 5),(3, 6),(4, 5),(4, 6),(5, 6)), "brown", (("blank", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), ("blank", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))))     #63
        self.pile.append(Tile(64, (), ((1, 2),(4, 6)), "brown", (("blank", 0), ("blank", 1))))  #64
        self.pile.append(Tile(65, (), ((2, 3),(4, 6)), "brown", (("blank", 0), ("blank", 1))))  #65
        self.pile.append(Tile(66, (), ((1, 6),(2, 5)), "brown", (("blank", 0), ("blank", 1))))  #66
        self.pile.append(Tile(67, (), ((2, 5),(4, 6)), "brown", (("blank", 0), ("blank", 1))))  #67
        self.pile.append(Tile(68, (), ((1, 4),(3, 6)), "brown", (("blank", 0), ("blank", 1))))  #68
        self.pile.append(Tile(70, (), ((1, 3),(1, 6),(2, 3),(2, 6)), "brown", ()))    #70

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        