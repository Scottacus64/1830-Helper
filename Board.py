from Hexagon import Hexagon
from TilePile import TilePile


class Board:
    def __init__(self):
        self.unplayedTiles = TilePile().getTiles()
        self.allTiles = TilePile().getTiles()
        self.playedTiles = []
        self.board_hexagons = []
        self.tiles_on_the_board = []
        self.initialze_standard_board()
        self.possibleTiles = []
        self.possibleTilesIndex = 0
        self.lastLocation = (100,100)
        self.largestTrain = 0
        self.tileList = []
        self.tileListIndex = 0
        self.tempHexag = []
        self.companyStations = []
        
        self.hexagDictionary = {
            0: "0210",  1:"0212",  2:"0214",  3:"0216",  4:"0218",  5:"0220",  6:"0222", 
            7: "0307",  8:"0309",  9:"0311", 10:"0313", 11:"0317", 12:"0319", 13:"0321", 14:"0323",
            15:"0402", 16:"0404", 17:"0406", 18:"0408", 19:"0410", 20:"0412", 21:"0414", 22:"0416", 23:"0418", 24:"0420",  25:"0422", 
            26:"0503", 27:"0505", 28:"0507", 29:"0511", 30:"0513", 31:"0515", 32:"0517", 33:"0519", 34:"0521", 35:"0523",
            36:"0604", 37:"0608", 38:"0610", 39:"0612", 40:"0614", 41:"0616", 42:"0618", 43:"0620", 44:"0622", 
            45:"0703", 46:"0705", 47:"0707", 48:"0709", 49:"0711", 50:"0713", 51:"0715", 52:"0717", 53:"0719",
            54:"0802", 55:"0804", 56:"0806", 57:"0808", 58:"0810", 59:"0814", 60:"0816", 61:"0818", 
            62:"0903", 63:"0905", 64:"0907", 65:"0909", 66:"0911", 67:"0913", 68:"0915", 69:"0917", 
            70:"1004", 71:"1006", 72:"1008", 73:"1010", 74:"1012", 75:"1014", 76:"1115"
            }

        

    def initialze_standard_board(self):
        # NOTE: Odd rows only have odd columns, even rows only have even columns
        
        # ----- off_board_hexages -----
        self.off_board_hexages = [(1, 1), (1, 3), (1, 5), (1, 7), (1, 13), (1, 15), (1, 21), (1, 23),
                         (2, 2), (2, 4), (2, 6), (2, 8),
                         (3, 1), (3, 3), (3, 5),
                         (5, 1),
                         (7, 1), (7, 21), (7, 23),
                         (8, 20), (8, 22), (8, 24),
                         (9, 21), (9, 23),
                         (10, 16), (10, 18), (10, 20), (10, 22), (10, 24),
                         (11, 1), (11, 3), (11, 5), (11, 7), (11, 9), (11, 11), (11, 17), (11, 19), (11, 21), (11, 23)]
        
        # ----- on_board_hexages -----
        on_board_hexages = []
        for i in range(1, 12): # Rows A-K
            if i % 2 == 1:
                for j in range(1, 24, 2): # Add all valid hexages in odd rows 
                    if((i, j) not in self.off_board_hexages):
                        on_board_hexages.append((i, j))
            else:
                for j in range(2, 25, 2): # Add all valid hexages in even rows 
                    if((i, j) not in self.off_board_hexages):
                        on_board_hexages.append((i, j))
        
        # ----- grey_hexages -----
        station_ct_list = [[(1, 19),1],
                          [(2, 10), 1], [(2, 16), 1],
                          [(4, 2), 1], [(4,10), 2], [(4, 14), 1],
                          [(5,5), 2], [(5,11), 2], [(5, 19), 1], [(5, 23), 1],
                          [(6, 4), 1], [(6, 6), 1], [(6, 16), 1], [(6, 22), 1],
                          [(7,19), 2],
                          [(8, 4), 1], [(8, 10), 1], [(8, 12), 1], [(8, 16), 1], [(8,18), 2], 
                          [(9, 15), 1], 
                          [(10, 14), 1], 
                          [(11, 15), 1]
                          ]
        
        # ----- one_city_hexages -----
        one_city_hexages = [  [(1, 19), 4],
                              [(2, 10), 0], [(2, 16), 0],
                              [(4, 2), 9], [(4, 14), 11],
                              [(5, 19), 6], [(5, 23), 1],
                              [(6, 4), 0], [(6, 6), 3], [(6, 16), 0], [(6, 22), 0],
                              [(8, 4), 0], [(8, 10), 0], [(8, 12), 8], [(8, 16), 0],
                              [(9, 15), 2],
                              [(10, 14), 0],
                              [(11, 15), 10]
                          ]
        
        # ----- two_city_hexages -----
        two_city_hexages = [((4, 10), 19),
                          ((5, 5), 27), ((5, 11), 29),
                          ((8, 18), 61)]
        
        # ------ four_city_hexag -------
        four_city_hexag = [(7, 19), "NY"]
        
        # ----- one_village_hexages -----
        one_village_hexages = [(2, 20),
                             (3, 15),
                             (4, 4),
                             (5, 7),
                             (6, 10), (6, 24),
                             (9, 19)]
        
        # ----- two_vilage_hexages -----
        two_village_hexages = [(6, 20),
                             (7, 7), (7, 17)]
        
        # ----- rr_start_hexages -----
        rr_start_hexages = [((1, 19), 4),
                          ((5, 19), 6), ((5, 23), 1),
                          ((6, 6), 3),
                          ((7, 19), 7),
                          ((8, 12), 8),
                          ((9, 15), 2)]
        
        # ----- companySides -----
        # (row,column), [[company0, side0, side1 ...][company1, side0, side 1...]]  100 = no station, 71-77 for red off map, 50 for unassigned station, 1-8 for assigned companies
        companySidesList =  [((1,9), [[71,3]]), ((1,11), [[72,3,4]]),  ((1,17),[[100,3,4]]), ((1,19), [[4,3,4]]),
                            ((2,10), [[50,0,0],[50,0,0]]), ((2,16), [[50,0,0],[50,0,0]]), ((2,24), [[73,4,5]]),
                            ((3,15), [[100,1,5]]),
                            ((4,2), [[50,2,3],[100,0,0]]), ((4,10), [[50,0,0], [50,0,0]]), ((4,14), [[50,2,4,5],[100,0,0]]), ((4,24),[[100,4,5]]),
                            ((5,5), [[50,0,0], [50,0,0]]), ((5,9), [[100,6,1]]), ((5,11), [[50,0,0], [50,0,0]]),  ((5,19), [[6],[50]]), ((5,23), [[1,1,3],[50,0,0]]),
                            ((6,2), [[74,1,2,3]]), ((6,4), [[50],[50]]), ((6,6), [[3,3,4]]), ((6,16), [[50,0,0],[50,0,0]]), ((6,22), [[50,0,0],[50,0,0]]), ((6,24),[[100,5,6]]),
                            ((7,19), [[7,1], [50,4], [50,1], [50,4]]),
                            ((8,4),[[50,0,0],[50,0,0]]), ((8,10), [[50,0,0],[50,0,0]]), ((8,12), [[8,2,5], [100,2,5]]), ((8,16),[[50,0,0],[50,0,0]]), ((8,18), [[50,0,0],[50,0,0]]),
                            ((9,1),[[75,2]]), ((9,15), [[2,2,4],[100,0,0]]), ((9,19), [[100,5,6]]),
                            ((10,2), [[76,1,2]]), ((10,14), [[50,0,0],[50,0,0]]),
                            ((11,13), [[77,1,6]]), ((11,15), [[50],[100,0,0]])
                            ]
        # ----- voidSides_hexages -----
        # (row, column), [void sides]
        voidSidesList = [((2,10),[5]), ((2,12),[1]), ((2,14),[1,6]), ((2,16),[6]), ((2,20), [1]), ((2,22), [1,6]),
                     ((3,7), [1,4,5,6]), ((3,9), [6]), ((3,11), [3]), ((3,13), [3,4]), ((3,17), [5,6]), ((3,23), [2,3]),
                     ((4,2), [4,5,6,1]), ((4,4),[1,6]), ((4,6), [1,6]), ((4,12), [1,6]), ((4,14), [1,6]), ((4,16), [6]), 
                     ((5,3), [5]), ((5,5), [3]), ((5,7), [2,3,4]), ((5,11), [5]), ((5,23), [2]),
                     ((6,4), [2]), ((6,8), [1,5,6]), ((6,10), [6]), ((6,20), [3]), ((6,22), [3,4]),
                     ((7,3), [5]), ((7,19), [2,3]),
                     ((8,2),[4,5,6]), ((8,18), [2]),
                     ((9,15),[3]), ((9,17), [3,4]),
                     ((10,4), [3,4]), ((10,6), [3,4]), ((10,8), [3,4]), ((10,10), [3,4]), ((10,12), [4]), ((10,14), [2]),
                     ((11,15), [1,2,3,4,5])
                     ]

        # Create the hexagon objects
        for hexag in on_board_hexages:
            #-----hexag ID-----
            hexag_id = hexag                    # tuple like (3,7)
            
            #-----hexag_name-----
            hexagFirst = hexag[0]
            hexagSecond = hexag[1]
            if hexagFirst < 10:
                hexagFirstStr = str("0" + str(hexag[0]))
            else:
                hexagFirstStr = str(hexag[0])
            if hexagSecond < 10:
                hexagSecondStr = str("0" + str(hexag[1]))
            else:
                hexagSecondStr = str(hexag[1])
            hexagName = str(hexagFirstStr + hexagSecondStr)
            hexag_name = hexagName                # string like 0307
            
            #-----hexagTile-----
            hexagTile = 0
            
            #-----Village Count-----
            if(hexag in one_village_hexages):
                vil_count = 1
            elif(hexag in two_village_hexages):
                vil_count = 2
            else:
                vil_count = 0
            
            #-----City Count-----
            city_count = 0
            for oneCityList in one_city_hexages:
                if oneCityList[0] == hexag: # Case for checking if there is only one city
                    city_count = 1
                    if oneCityList[1] == 2:
                        hexagTile = 80
                    elif oneCityList[1] == 1:
                        hexagTile = 81
                    elif oneCityList[1] == 9:
                        hexagTile = 85
                    elif oneCityList[1] == 10:
                        hexagTile = 86
                    elif oneCityList[1] == 11:
                        hexagTile = 87
            
            for twoCityList in two_city_hexages: # Find if there is matching hexag and get its ind
                if twoCityList[0] == hexag:
                    city_count = 2
                    hexagTile = 83
                        
            if four_city_hexag[0] == hexag:
                city_count = 4
                hexagTile = 82
                        
            #-----Station Count-----
            station_count = 0
            for stationCt in station_ct_list:
                if stationCt[0] == hexag:
                    station_count = stationCt[1]
                    break    
        
            #-----Railroad Start-----
            hexag_rr_ind = None
            for ind, item in enumerate(rr_start_hexages):
                if(item[0] == hexag):
                    hexag_rr_ind = ind
                    break
            if hexag_rr_ind is None:
                rr_start = 100
            else:
                rr_start = rr_start_hexages[hexag_rr_ind][1]
                
            #-----companySides-----
            companySides = None                     # list that contains the [company, side0, side1],[company1, side0, side 1]
            for cs in companySidesList:
                if cs[0] == hexag:
                    companySides = cs[1]
                    break
            if companySides is None:
                companySides = []

            #-----VoidSides-----
            hexagVoidSides = None                     # void sides are sides that are illegal to send rails to like off ap or water
            for item in voidSidesList:
                if item[0] == hexag:
                    hexagVoidSides = item[1]
                    break
            if hexagVoidSides is None:
                voidSides = []
            else:
                voidSides = hexagVoidSides
                
            angle = 0
            
            # Initialize the hexag object
            hexag_to_append = Hexagon(hexag_id, hexag_name, vil_count, city_count, station_count, rr_start, companySides, voidSides, hexagTile, angle, "")
            self.board_hexagons.append(hexag_to_append)
            
        # add city tiles to playedTile list
        cityTiles = [80, 81, 82, 83, 83, 83, 83]
        for tileNumber in cityTiles:
            tile = self.removeTileFromUnplayedTiles(tileNumber) 
            self.playedTiles.append(tile)


    def print_board(self):
        for a_hexag in self.board_hexagons:
            print(a_hexag.hexag_id, "rr =", a_hexag.rr_start, " v =", a_hexag.vil_count, "c =", a_hexag.city_count, "stn = ", a_hexag.station_count, "cs =", a_hexag.companySides, "hv =", a_hexag.voidSides, "t =", a_hexag.hexagTile,  )
            print("---------------")  
        foundTile = self.checkThroughUnplayedTiles(57)
        print("Found Tile " + str(foundTile.tile_id))
            
     
    # This method takes in information from the GUI and returns tiles that can be played 
    def checkForPlayableTile(self, location):
        # this is a list of the hexages rail spurs around the location with the correcponding side of the location in that direction
        # for example the first hexag returned by findAdjacenthexages is above and to the left, if that hexag has a rail on
        # side 3 then that correspnds to side 6 on the location hexag [(3,6), ...]
        listOfPairedSides = [(3,6),(4,1),(2,5),(5,2),(1,4),(6,3)]   # top left, top right, left, right, lower left, lower right
        listOfSides = [3,4,2,5,1,6]
        self.possibleTiles = []
        railInDirection = []
        hexagList = self.findAdjacentHexages(location)
        self.lastLocation = location
        
        # check for rail lines leading into hexag
        index = 0
        print(f"********adjacent Hexagons = {hexagList}")
        for hexag in hexagList:
            hexagObject = self.findHexagTuple(hexag) 
            if hexagObject is not None: 
                print("hexag CS = " + str(hexagObject.companySides))
                sidesList = []
                for csList in hexagObject.companySides:
                    cslLength = len(csList)
                    for i in range (cslLength-1):
                        sidesList.append(csList[i+1])
                for side in sidesList:
                    if side == listOfSides[index]:
                            railInDirection.append(listOfPairedSides[index][1])
            index +=1
        print("Rail in direction = " + str(railInDirection))  
        # check for void sides on the location hexag
        locationhexag = self.findHexagTuple(location)
        voidInDirection = []
        voidInDirection = locationhexag.voidSides
        possibleTiles = []
        upgradeTile = False

        # check to see if a hexag has a tile placed to upgreade
        if locationhexag.hexagTile == 0:                                    # hexag with no tile to upgrade
            if railInDirection:                                             # since this is a hexag with no tiles check to see if rails lead into the hexag
                startTiles = [1, 2, 3, 4, 7, 8, 9, 55, 56, 57, 58, 69]      # base yellow tiles to upgrade to         
                for tileNumber in startTiles:                               # go through each of these tiles and choose tiles that match vil and city cts
                    testTile = self.checkThroughUnplayedTiles(tileNumber) 
                    if testTile is not None:
                        if testTile.city_count == locationhexag.city_count and testTile.village_count == locationhexag.vil_count:
                            possibleTiles.append((tileNumber, 0))
                
        # the hexag already has a tile so the upgrade list is used
        else:                                                                   # hexag with tile associated with it
            hexagTileNumber = locationhexag.hexagTile
            tileToUpgrade = self.playedTileLookUp(hexagTileNumber)
            possibleTiles = tileToUpgrade.upgrade_list
            upgradeTile = True
            
        # this section looks through each tile in possibleTiles and selects and rotates the legal placements
        if possibleTiles:
            validRotation = True
            for tTile in possibleTiles:                                         # look through each possible tile number
                tile = self.checkThroughUnplayedTiles(tTile[0])                 # get the tile object for that number
                if tile:                                                        # if there are unplayed tiles of this type then continue else try next one
                    angle = tTile[1]
                    tileSides = self.findSides(tile, angle)                         # get a list of all sides of the tile that have a rail on them 
                    if upgradeTile == False:                                        # this is a hexag with no previous tile on it
                        for hexagRailDirection in railInDirection:                  # look at each hexag side that faces a rail
                            for eeSide in tileSides:                                # look at each rail side for the tile
                                validRotation = True                                # flag to tell if the rotation being tested is valid
                                offset = hexagRailDirection - eeSide                # find the number of rotation steps needed to line up the rails
                                if offset < 0:                                      # tile entry/exit is left of hexag rail direction
                                    offset += 6  
                                for tSide in tileSides:  
                                    testSide = tSide + offset
                                    if testSide > 6:
                                        testSide -=6
                                    if testSide in locationhexag.voidSides:
                                        validRotation = False
                                if validRotation == True:
                                    if (tile.tile_id, offset) not in self.possibleTiles:
                                        self.possibleTiles.append((tile.tile_id, offset)) 
                                        
                    else:                                                           # this is a hexag with a tile to upgrade
                        validRotation = False
                        colorOk = self.checkTileColor(tile.tile_id)
                        if colorOk == True:
                            validRotation = True
                            angle = angle + locationhexag.angle       # add the rotation of the tile already there to the preset rotation on the new tile
                            if angle > 6:
                                angle -=6
                            print("TileSides = " + str(tileSides) + " angle = " + str(angle) + " voidSides = " + str(locationhexag.voidSides))
                            for eeSide in tileSides:                                # look at each side with a rail on it
                                if eeSide > 0:
                                    testSide = eeSide + angle                           # rotate to the angle
                                    if testSide > 6:
                                        testSide -=6
                                    if testSide in locationhexag.voidSides:               # see if it is in voidSides
                                        validRotation = False
                            offset = angle  
                    if validRotation == True:
                        if (tile.tile_id, offset) not in self.possibleTiles:
                            self.possibleTiles.append((tile.tile_id, offset))   # add the tile number and rotation to the list
                    print(f"possible tiles = {self.possibleTiles}")
            return self.possibleTiles
        
        
    # method to rotate a tile, find all sides touched by rails and output a list of unique sides with rails (no repeats)
    def findSides(self, tile, angle):
        if tile:
            listOfSides = []
            for station in tile.station_list:
                for side in station[1:]:

                    if side > 6:
                        side -=6
                    if side not in listOfSides:
                        listOfSides.append(side)
            return listOfSides
        
    
    # method to find hexages that surround the target hexag
    def findAdjacentHexages(self, location):
        testList = []
        hexagList = []
        locationFirst = location[0]
        locationSecond = location[1]
        # find the hexages around the location hexag
        if locationFirst > 1:               # get tiles above
            if locationSecond > 1:          # get above and left
                testList.append((locationFirst - 1, locationSecond - 1))
            if locationSecond < 24:         # get above and right
                testList.append((locationFirst - 1, locationSecond + 1))
        if locationSecond >1:               # get left
            testList.append((locationFirst, locationSecond - 2))
        if locationSecond < 24:             # get right
            testList.append((locationFirst, locationSecond + 2))
        if locationFirst < 15:              # get tiles below 
            if locationSecond > 1:          # below and left
                testList.append((locationFirst + 1, locationSecond - 1))
            if locationSecond < 24:         # below and right
                testList.append((locationFirst + 1, locationSecond + 1))
        for loc in testList:
            if loc not in self.off_board_hexages:
                hexagList.append(loc)
            else:
                hexagList.append((0,0))
        return hexagList
    
    
    # find the hexag by its id (5,5)
    def findHexagTuple(self, id):
        print("In  Find Hexag by tuple")
        for hexagObj in self.board_hexagons:
            if hexagObj.hexag_id == id:
                print("ID = " + str(id))
                return hexagObj                       #return the hexag upon a match
        return None                                 #If there was no match, return None
    
    
    # find the hexag by its name (0505)
    def findHexagByName(self, name):
        for hexagObj in self.board_hexagons:
            if hexagObj.hexag_name == name:
                return hexagObj                       #return the hexag upon a match
        return None                                 #If there was no match, return None
    
    
    # find the hexag by receiving the number (the dictionary is number:name)
    def findHexagByNumber(self, number):
        print(f"Find Hexag by Number, Number = {number}")
        hexagLocation = self.hexagDictionary[number]
        locationFirst = int(hexagLocation[:2])                    # parsing out the tuple for board to use
        locationSecond = int(hexagLocation[2:])
        boardLocation = (locationFirst, locationSecond)
        return self.findHexagTuple(boardLocation)                 # get the hexag object...
    
    
    # find a hexag by the tile associated with it
    def findByhexagTile(self, hexagTile):
        for hexagObj in self.board_hexagons:
            if hexagObj.hexagTile == hexagTile:
                return hexagObj
        return None
    
    
    def checkThroughUnplayedTiles(self, targetTile):
        ind = 0
        while ind < len(self.unplayedTiles):
            if self.unplayedTiles[ind].tile_id == targetTile:
                return self.unplayedTiles[ind]
            else:
                ind += 1
        return None 
    
    
    def updateHexagWithTile(self, tileNumber, name, angle, cityNumber, stationCompany): # this is run after a hexag is finalized
        hexag = self.findHexagByName(name)
        oldTile = hexag.hexagTile
        if oldTile > 0:
            swapTile = self.addTileBackOnUnplayedList(oldTile)
            if swapTile:
                self.unplayedTiles.append(swapTile)
        
        tile = self.removeTileFromUnplayedTiles(tileNumber)             # remove the tile from the unplayed list and add to played list
        if tile == None:
            return
        hexag.hexagTile = tileNumber                                    # get the tile number assigned to the hexag
        tileStationList = tile.station_list
        print("")
        print("tile Station List = " + str(tileStationList))
        print(f"city number {cityNumber} and stationCompany {stationCompany}")
        print(f"Heag CS = {hexag.companySides}")
        
        rotatedStationList = []
        cityCompany = []
        
        if hexag.companySides:
            index = 0
            for slot in hexag.companySides:
                if slot[0] < 50:
                    cityCompany.append([index, slot[0]])
                else:
                    if index == cityNumber:
                        cityCompany.append([cityNumber, stationCompany])
                    else:
                        cityCompany.append([index, 50])
                index +=1
        else:
            for station in tileStationList:
                cityCompany.append([0,stationCompany])
                    
        print(f"******** EEC = {cityCompany}")
      
        hexag.companySides = []
 
        index = 0
        for stn in tileStationList:
            sideList = []
            rotatedStationList = []
            for i in range(len(stn)):
                if i>0:
                    rSide = stn[i] + angle
                    if rSide > 6:
                        rSide -=6
                    rotatedStationList.append(rSide)
            print(f"rotated station list = {rotatedStationList}") 
            print(f"city company = {cityCompany[index][1]}")            
            sideList.append(cityCompany[index][1])
            for item in rotatedStationList:
                sideList.append(item)  
            hexag.companySides.append(sideList)
            if cityCompany[index][1] < 10:
                if [cityCompany[index][1], name] not in self.companyStations:
                    self.companyStations.append([cityCompany[index][1], name])      # appends the company name and the hexag name to the list for latee recursive methods
            index +=1
            
        if len(hexag.companySides) < 2:
            hexag.companySides.append([100,0,0])

        hexag.angle = angle                                               # set the hexag's angle value
        print(f"tile Color {tile.color}")
        hexag.color = tile.color
        print("******************************")
        print(f"hexag color = {hexag.color}")
        print ("hexagTile = " + str(hexag.hexagTile))
        print ("hexag Cs = " + str(hexag.companySides))
        print (f"company station list = {self.companyStations}")
        print("")
              
        
    def removeTileFromUnplayedTiles(self, tileNumber):
        index = 0
        for tile in self.unplayedTiles:
            if tile.tile_id == tileNumber:
                poppedTile = self.unplayedTiles.pop(index)
                self.playedTiles.append(poppedTile)
                return poppedTile
            index +=1
            
            
    def addTileBackOnUnplayedList(self, oldTile):
        index = 0
        for tile in self.playedTiles:
            if tile.tile_id == oldTile:
                swapTile = self.playedTiles.pop(index)
                return swapTile
            index +=1
         
            
    def playedTileLookUp(self, tileNumber):
        for tile in self.playedTiles:
            if tile.tile_id == tileNumber:
                return tile
            
    
    def unplayedTileLookUp(self, tileNumber):
        for tile in self.unplayedTiles:
            if tile.tile_id == tileNumber:
                return tile


    def allTilesLookUp(self, tileNumber):
        for tile in self.allTiles:
            if tile.tile_id == tileNumber:
                return tile

    def checkTileColor(self, tileNumber):
        green = [14,15,16,18,19,20,23,24,25,26,27,28,29,53,54,59]
        brown = [39,40,41,42,43,44,45,46,47,61,62,63,64,65,66,67,68,70]
        if tileNumber in green and self.largestTrain > 2 or tileNumber in brown and self.largestTrain > 4:
            return True
        else:   
            return False
        
        
    def getHexCompanySides(self, hexag):
        csList = []
        for slot in hexag.companySides:
            csList.append(slot)
        return csList
                
    def setColor(self, hexag, color):
        hexag.color = color
        

            
        























