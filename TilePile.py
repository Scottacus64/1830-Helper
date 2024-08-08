from Tile import Tile

class TilePile():
    def __init__(self):
        self.pile = []
        self.populate_pile()
    
    def populate_pile(self):
        #tile_id, upgrade_list, path_pairs, station list (owner followed by rails connected to the station), village_count, city_count, color
        # 100 = no station, 90 = village, 50 = unassigned city
        #----- yellow -----
        self.pile.append(Tile(1, (), [[2, 6],[3, 5]], [[90,2,6],[90,3,5]], 2, 0, "yellow"))  #1
        self.pile.append(Tile(2, (), [[1, 2],[3, 6]], [[90,1,2],[90,3,6]], 2, 0, "yellow"))  #2
        for i in range(0, 2):
            self.pile.append(Tile(3, (), [[4, 5]], [[100,4,5]], 1, 0, "yellow")) #3
            self.pile.append(Tile(4, (), [[3, 6]], [[100,3,6]],  1, 0, "yellow")) #4
        for i in range(0, 4):
            self.pile.append(Tile(7, [(18,2), (26,1), (27,0), (28,1), (29,0)], [[3, 4]], [[100,3,4]], 0, 0, "yellow"))  #7
                             
        for i in range(0, 8):
            self.pile.append(Tile(8, [(16,2), (16,3), (19,4), (23,2), (24,0), (25,0), (25,2), (28,2), (29,0)], [[3, 5]], [[100,3,5]], 0, 0, "yellow") )  #8
        for i in range(0, 7):
            self.pile.append(Tile(9, [(18,0), (18,3), (19,0), (19,3), (20,0), (20,1), (20,3), (20,4), (23,0), (23,3), (24,0), (24,3), (26,0), (26,3), (27,0), (27,3)], [[3, 6]], [[100,3,6]], 0, 0, "yellow"))   #9
        self.pile.append(Tile(55, (), [[2, 5],[3, 6]], [[90,2,5],[90,3,6]], 2, 0, "yellow")) #55
        self.pile.append(Tile(56, (), [[1, 3],[2, 6]], [[90,1,3],[90,2,6]], 2, 0, "yellow")) #56
        for i in range(0, 4):
            self.pile.append(Tile(57, [(14,0), (14,1), (14,3), (14,4), (15,0), (15,3)], [[3, 6]], [[50, 3, 6]], 0, 1, "yellow"))  #57
        for i in range(0, 2):
            self.pile.append(Tile(58, (), [[3, 5]], [[90,3,5]], 1, 0, "yellow"))    #58
        self.pile.append(Tile(69, (), [[1, 5],[3, 6]], [[90,1,5],[90,3,6]], 2, 0, "yellow")) #69
        
        #----- green -----
        for i in range(0, 3):
            self.pile.append(Tile(14, [(63,0)], [[2, 3],[2, 5],[2, 6],[3, 5],[3, 6],[5, 6]], [[50, 2, 3, 5, 6], [50, 2, 3, 5, 6]], 0, 2, "green"))    #14
        for i in range(0, 2):
            self.pile.append(Tile(15, [(63,0)], [[1, 2],[1, 3],[1, 6],[2, 3],[2, 6],[3, 6]], [[50, 1, 2, 3, 6], [50, 1, 2, 3, 6]], 0, 2, "green"))    #15
        self.pile.append(Tile(16, [(43,0), (43,1), (70,0), (70,1)], [[1, 3],[2, 6]], [[100,1,3],[100,2,6]], 0, 0, "green"))    #16
        self.pile.append(Tile(18, [(43,0)], [[1, 2],[3, 6]], [[100,1,2],[100,3,6]], 0, 0, "green"))    #18
        self.pile.append(Tile(19, [(45,4), (46,2)], [[1, 5],[3, 6]], [[100,1,5],[100,3,6]], 0, 0, "green"))    #19
        self.pile.append(Tile(20, [(44,0), (44,3), (47,0), (47,3)], [[2, 5],[3, 6]], [[100,2,5],[100,3,6]], 0, 0, "green"))    #20
        for i in range(0, 3):
            self.pile.append(Tile(23, [(41,0), (43,0), (45,4), (47,2)], [[1, 3],[3, 6]], [[100,1,3],[100,3,6]], 0, 0, "green"))    #23
            self.pile.append(Tile(24, [(42,0), (43,3), (46,2), (47,0)], [[3, 5],[3, 6]], [[100,3,5],[100,3,6]], 0, 0, "green"))    #24
        self.pile.append(Tile(25, [(40,0), (45,0), (46,0)], [[1, 3],[3, 5]], [[100,1,3],[100,3,5]], 0, 0, "green"))    #25
        self.pile.append(Tile(26, [(42,3), (44,0), (45,1)], [[2, 3],[3, 6]], [[100,2,3],[100,3,6]], 0, 0, "green"))    #26
        self.pile.append(Tile(27, [(41,3), (44,1), (46,5)], [[3, 4],[3, 6]], [[100,3,4],[100,3,6]], 0, 0, "green") )   #27
        self.pile.append(Tile(28, [(39,5), (43,1), (46,4), (70,0)], [[1, 3],[2, 3]], [[100,1,3],[100,2,3]], 0, 0, "green"))    #28
        self.pile.append(Tile(29, [(39,1), (43,2), (45,2), (70,3)], [[3, 4],[3, 5]], [[100,3,4],[100,3,5]], 0, 0, "green"))    #29
        for i in range(0, 2):
            self.pile.append(Tile(53, [(61,0), (61,1), (61,2), (61,3), (61,4), (61,5)], [[1, 3],[1, 5],[3, 5]], [[50, 1, 3, 5]], 0, 1, "green"))    #53 Bost and Balt
        self.pile.append(Tile(54, [(62,0)], [[1, 2],[5, 6]], [[7, 1, 2, 5, 6], [50, 1, 2, 5, 6], [50], [50]], 0, 20, "green"))    #54 NY
        for i in range(0, 2):
            self.pile.append(Tile(59, [(64,2), (65,2), (66,3), (67,0), (68,1), (68,4)], [[2,0],[4,0]], [[50, 4], [50, 2]], 0, 20, "green"))  #59 "OO"      

        #----- brown -----
        self.pile.append(Tile(39, (), [[2, 2],[2, 4],[3, 4]], [[100,2,3,4]], 0, 0, "brown"))   #39
        self.pile.append(Tile(40, (), [[1, 3],[1, 5],[3, 5]], [[100,1,3,5]], 0, 0, "brown"))   #40
        for i in range(0, 2):
            self.pile.append(Tile(41, (), [[1, 3],[1, 6],[3, 6]], [[100,1,3,6]], 0, 0, "brown"))   #41
            self.pile.append(Tile(42, (), [[3, 5],[3, 6],[5, 6]], [[100,3,5,6]], 0, 0, "brown"))   #42
            self.pile.append(Tile(43, (), [[1, 2],[1, 3],[2, 6],[3, 6]], [[100,1,2,3,6]], 0, 0, "brown"))    #43
        self.pile.append(Tile(44, (), [[2, 3],[2, 5],[3, 6],[5, 6]], [[100,2,3,5,6]], 0, 0, "brown"))    #44
        for i in range(0, 2):
            self.pile.append(Tile(45, (), [[1, 2],[1, 3],[2, 5],[3, 5]], [[100,1,2,3,5]], 0, 0, "brown"))    #45
            self.pile.append(Tile(46, (), [[1, 3],[1, 4],[3, 5],[4, 5]], [[100,1,3,4,5]], 0, 0, "brown"))    #46
        self.pile.append(Tile(47, (), [[2, 5],[2, 6],[3, 6],[3, 5]], [[100,2,3,5,6]], 0, 0, "brown"))    #47
        for i in range(0, 2):
            self.pile.append(Tile(61, (), [[1, 3],[1, 5],[1, 6],[3, 5],[3, 6],[5, 6]], [[50, 1, 3, 5, 6]], 0, 1, "brown"))  #61
        self.pile.append(Tile(62, (), [[1, 2],[5, 6]], [[7,1,2], [50,1,2], [50,5,6], [50,5,6]], 0, 40, "brown"))    #62
        for i in range(0, 3):
            self.pile.append(Tile(63, (), [[1, 2],[1, 3],[1, 4],[1, 5],[1, 6],[2, 3],[2, 4],[2, 5],[2, 6],[3, 4],[3, 5],[3, 6],[4, 5],[4, 6],[5, 6]], [[50, 1, 2, 3, 4, 5, 6], [50, 1, 2, 3, 4, 5, 6]], 0, 2, "brown") )    #63
        self.pile.append(Tile(64, (), [[1, 2],[4, 6]], [[50, 1, 2], [50, 4, 6]], 0, 20, "brown"))  #64
        self.pile.append(Tile(65, (), [[2, 3],[4, 6]], [[50, 2, 3], [50, 4, 6]], 0, 20, "brown"))  #65
        self.pile.append(Tile(66, (), [[1, 6],[2, 5]], [[50, 1, 6], [50, 2, 5]], 0, 20, "brown"))  #66
        self.pile.append(Tile(67, (), [[2, 5],[4, 6]], [[50, 4, 6], [50, 2, 5]], 0, 20, "brown"))  #67
        self.pile.append(Tile(68, (), [[1, 4],[3, 6]], [[50, 3, 6], [50, 1, 4]], 0, 20, "brown"))  #68
        self.pile.append(Tile(70, (), [[1, 3],[1, 6],[2, 3],[2, 6]], [[100,1,2,3,6]], 0, 0, "brown") )   #70
        
        #----- special tiles for cities and OO -----
        self.pile.append(Tile(80, [(53,1)], [[1,3]], [[1, 1, 3]], 0, 0, ""))     # Baltimore
        self.pile.append(Tile(81, [(53,0)], [[2,4]], [[2, 2, 4]], 0, 0, "") )    # Boston
        self.pile.append(Tile(82, [(54,5)], [[1,0], [4,0]], [[7, 1], [50, 4]], 0, 0, ""))   # New York
        for i in range(4):
            self.pile.append(Tile(83, [(59,0), (59,1), (59,2), (59,3), (59,4), (59,5)], [[]], [[50],[50]], 0, 0, ""))   # blank "00"
            
        #----- special tiles for empty cities with rails -----
        self.pile.append(Tile(85, (), [(2,3)], [[50,2,3]], 0, 1, ""))
        self.pile.append(Tile(86, (), [6,0], [[50,6]], 0, 1, ""))
        
        
    def getTiles(self):
        return self.pile
    
    def getCompany(self, tileNumber):
        for tile in self.pile:
            if tile.getId == tileNumber:
                return tile.getCompany
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        