from Hexagon import Hexagon
from TilePile import TilePile


class Board:
    def __init__(self):
        self.unplayedTiles = TilePile().getTiles()
        self.playedTiles = []
        self.board_hexagons = []
        self.tiles_on_the_board = []
        self.initialze_standard_board()
        self.possibleTiles = []
        self.possibleTilesIndex = 0
        self.lastLocation = (100,100)
        
        self.hexDictionary = {
            0:"0210", 1:"0212", 2:"0214", 3:"0216", 4:"0218", 5:"0220", 6:"0222", 
            7:"0307", 8:"0309", 9:"0311", 10:"0313", 11:"0317", 12:"0319", 13:"0321", 14:"0323",
            15:"0402", 16:"0404", 17:"0406", 18:"0408", 19:"0410", 20:"0412", 21:"0414", 22:"0416", 23:"0418", 24:"0420",  25:"0422", 
            26:"0503", 27:"0505", 28:"0507", 29:"0511", 30:"0513", 31:"0515", 32:"0517", 33:"0519", 34:"05214", 35:"0523",
            36:"0604", 37:"0608", 38:"0610", 39:"0612", 40:"0614", 41:"0616", 42:"0618", 43:"0620", 44:"0622", 
            45:"0703", 46:"0705", 47:"0707", 48:"0709", 49:"0711", 50:"0713", 51:"0715", 52:"0717", 53:"0719",
            54:"0802", 55:"0804", 56:"0806", 57:"0808", 58:"0810", 59:"0814", 60:"0816", 61:"0818", 
            62:"0903", 63:"0905", 64:"0907", 65:"0909", 66:"0911", 67:"0913", 68:"0915", 69:"0917", 
            70:"1004", 71:"1006", 72:"1008", 73:"1010", 74:"1012", 75:"1014", 76:"1115"
            }

        

    def initialze_standard_board(self):
        # NOTE: Odd rows only have odd columns, even rows only have even columns
        '''
        This function will build out a standard board of 1830, it'll do so by categorizing each hex
        Categories include:
        -----------------------
            off_board_hexes
            
            on_board_hexes
    
            grey_hexes

            one_city_hexes
            
            two_city_hexes
            
            one_village_hexes
            
            two_villlage_hexes
            
            rr_start_hexes
            
            entryExitStation
            
            voidSides
            
            hexTile
            
            angle
        '''
        
        # ----- off_board_hexes -----
        self.off_board_hexes = [(1, 1), (1, 3), (1, 5), (1, 7), (1, 13), (1, 15), (1, 21), (1, 23),
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
                    if((i, j) not in self.off_board_hexes):
                        on_board_hexes.append((i, j))
            else:
                for j in range(2, 25, 2): # Add all valid hexes in even rows (ones that aren't in off_board_hexes)
                    if((i, j) not in self.off_board_hexes):
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
        
        # ----- one_city_hexes -----
        one_city_hexes = [[(1, 19),"0"],
                          [(2, 10), "0"], [(2, 16), "0"],
                          [(4, 2), "0"], [(4, 14), "0"],
                          [(5, 19), "0"], [(5, 23), "Boston"],
                          [(6, 4), "0"], [(6, 6), "0"], [(6, 16), "0"], [(6, 22), "0"],
                          [(8, 4), "0"], [(8, 10), "0"], [(8, 12), "0"], [(8, 16), "0"],
                          [(9, 15), "Baltimore"],
                          [(10, 14), "0"],
                          [(11, 15), "0"]
                          ]
        
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
        rr_start_hexes = [((1, 19), "CP"),
                          ((5, 11), "E"), ((5, 19), "NYC"), ((5, 23), "B&M"),
                          ((6, 6), "CCO"),
                          ((7, 19), "NYNH"),
                          ((8, 12), "PRR"),
                          ((9, 15), "B&O")]
        
        # ----- entryExitStation -----
        # (row, column), [[entry, exit, station]] exit == 0 for no exit, station == 0 for blank station, station == 10 no station
        entryExitStationList = [((1,9), [[3,0,10]]), ((1,11), [[3,0,10],[4,0,10]]),  ((1,17),[[3,4,10]]), ((1,19), [[3,4,0]]),
                            ((2,24), [[4,0,10], [5,0,10]]),
                            ((3,15), [[1,5,10]]),
                            ((4,2), [[2,3,0]]), ((4,14), [[2,5,0], [2,4,0], [4,5,0]]), ((4,24),[[4,5,10]]),
                            ((5,9), [[6,1,10]]), ((5,19), [[0,0,0]]), ((5,23), [[1,3,0]]),
                            ((6,2),[[1,0,10], [2,0,10], [3,0,10]]), ((6,6), [[3,4,0]]), ((6,24),[[5,6,10]]),
                            ((7,19), [[1,0,0], [4,0,0]]),
                            ((8,12), [[2,5,0], [2,5,10]]),
                            ((9,1),[[2,0,10]]), ((9,15), [[2,4,0]]), ((9,19), [[5,6,10]]),
                            ((10,2), [[1,0,10], [2,0,10]]), 
                            ((11,13), [[1,0,10], [6,0,10]]), ((11,15), [[6,0,0]])
                            ]
        # ----- voidSides_hexes -----
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
        for hex in on_board_hexes:
            #-----Hex ID-----
            hex_id = hex                # value tuple like (3,7)
            
            #-----HexTile-----
            hexTile = 0
            
            #-----Village Count-----
            if(hex in one_village_hexes):
                vil_count = 1
            elif(hex in two_village_hexes):
                vil_count = 2
            else:
                vil_count = 0
            
            #-----City Count-----
            city_count = 0
            for cityList in one_city_hexes:
                if cityList[0] == hex: # Case for checking if there is only one city
                    city_count = 1
                    if cityList[1] == "Boston":
                        hexTile = 81
                    if cityList[1] == "Baltimore":
                        hexTile = 80
            
            for twoCityList in two_city_hexes: # Find if there is matching hex and get its ind
                if twoCityList[0] == hex:
                    city_count = 2
                    if twoCityList[1]  == "NY":
                        hexTile = 82
                    else:
                        hexTile = 83
            
            #-----Color-----
            if(hex in grey_hexes):
                color = "grey"
            else:
                color = "blank"
        
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
                
            #-----EntryExitStation-----
            entryExit = None                        # list that contains the entry and exit sides of a hex and station associated with thsoe sides
            for item in entryExitStationList:       # station = 0 for station without a company assigned to it station = 10 for no station
                if item[0] == hex:
                    entryExit = item[1]
                    break
            if entryExit is None:
                entryExitStation = []
            else:
                entryExitStation = entryExit
            
            #-----VoidSides-----
            hexVoidSides = None                     # void sides are sides that are illegal to send rails to like off ap or water
            for item in voidSidesList:
                if item[0] == hex:
                    hexVoidSides = item[1]
                    break
            if hexVoidSides is None:
                voidSides = []
            else:
                voidSides = hexVoidSides
                
            angle = 0
            

        
            # Initialize the hex object
            hex_to_append = Hexagon(hex_id, vil_count, city_count, color, rr_start, entryExitStation, voidSides, hexTile, angle)
            self.board_hexagons.append(hex_to_append)
            
        # add city tiles to playedTile list
        cityTiles = [80, 81, 82, 83, 83, 83, 83]
        for tileNumber in cityTiles:
            tile = self.removeTileFromUnplayedTiles(tileNumber) 
            self.playedTiles.append(tile)

    def print_board(self):
        for a_hex in self.board_hexagons:
            print(a_hex.hex_id, "v =", a_hex.vil_count, "c =", a_hex.city_count, "col = ", a_hex.color, "ees =", a_hex.entryExitStation, "hv =", a_hex.voidSides, "t =", a_hex.hexTile,  a_hex.rr_start)
            print("---------------")  
        foundTile = self.checkThroughUnplayedTiles(57)
        print("Found Tile " + str(foundTile.tile_id))
            
     
    # This method take in information from the GUI and returns tiles that can be played 
    def checkForPlayableTile(self, location, company, trainList, newStation):
        # this is a list of the hexes rail spurs around the location with the correcponding side of the location in that direction
        # for example the first hex returned by findAdjacentHexes is above and to the left, if that hex has a rail on
        # side 3 then that correspnds to side 6 on the location hex [(3,6), ...]
        listOfPairedSides = [(3,6),(4,1),(2,5),(5,2),(1,4),(6,3)]   # top left, top right, left, right, lower left, lower right
        self.possibleTiles = []
        railInDirection = []
        hexList = self.findAdjacentHexes(location)
        self.lastLocation = location
        
        # check for rail lines leading into hex
        index = 0
        for hex in hexList:
            hexObject = self.findHex(hex) 
            if hexObject is not None: 
                for loc in hexObject.entryExitStation:
                    # [[3,0,10],[4,0,10]]
                    entrySide = loc[0]
                    exitSide = loc[1]
                    if entrySide == listOfPairedSides[index][0] or exitSide == listOfPairedSides[index][0]:
                        if listOfPairedSides[index][1] not in railInDirection:
                            railInDirection.append(listOfPairedSides[index][1])
            index +=1
            
        # check for void sides on the location hex
        locationHex = self.findHex(location)
        print("Location Hex at memory location: " + str(locationHex))
        voidInDirection = []
        voidInDirection = locationHex.voidSides
        print("Hex Current Tile = " + str(locationHex.hexTile))
        print ("Void sides = " + str(voidInDirection))
        print("CityCount = " + str(locationHex.city_count))
        possibleTiles = []
        upgradeTile = False

        # check to see if a hex has a tile placed to upgreade
        if locationHex.hexTile == 0:                                        # hex with no tile to upgrade
            if railInDirection:                                             # since this is a hex with no tiles check to see if rails lead into the hex
                startTiles = [1, 2, 3, 4, 7, 8, 9, 55, 56, 57, 58, 69]      # base yellow tiles to upgrade to         
                for tileNumber in startTiles:                               # go through each of these tiles and choose tiles that match vil and city cts
                    testTile = self.checkThroughUnplayedTiles(tileNumber) 
                    if testTile is not None:
                        if testTile.city_count == locationHex.city_count and testTile.village_count == locationHex.vil_count:
                            possibleTiles.append((tileNumber, 0))
                print("Possible tiles = " + str(possibleTiles))
                
        # the hex already has a tile so the upgrade list is used
        else:                                                                   # hex with tile associated with it
            hexTileNumber = locationHex.hexTile
            tileToUpgrade = self.playedTileLookUp(hexTileNumber)
            possibleTiles = tileToUpgrade.upgrade_list
            print("possible Tiles = " + str(possibleTiles))
            upgradeTile = True
            
        # this section looks through each tile in possibleTiles and selects and rotates the legal placements
        if possibleTiles:
            validRotation = True
            for tTile in possibleTiles:                                         # look through each possible tile number
                tile = self.checkThroughUnplayedTiles(tTile[0])                 # get the tile object for that number
                angle = tTile[1]
                tileSides = self.findSides(tile, angle)                         # get a list of all sides of the tile that have a rail on them
                print("**** tileSides = " + str(tileSides))  
                if upgradeTile == False:                                        # this is a hex with no previous tile on it
                    for hexRailDirection in railInDirection:                    # look at each hex side that faces a rail
                        for eeSide in tileSides:                                # look at each rail side for the tile
                            validRotation = True                                # flag to tell if the rotation being tested is valid
                            offset = hexRailDirection - eeSide                  # find the number of rotation steps needed to line up the rails
                            if offset < 0:                                      # tile entry/exit is left of hex rail direction
                                offset += 6  
                            for tSide in tileSides:  
                                testSide = tSide + offset
                                if testSide > 6:
                                    testSide -=6
                                if testSide in locationHex.voidSides:
                                    validRotation = False
                            if validRotation == True:
                                if (tile.tile_id, offset) not in self.possibleTiles:
                                    self.possibleTiles.append((tile.tile_id, offset)) 
                                    
                else:                                                           # this is a hex with a tile to upgrade
                    validRotation = True
                    angle = angle + locationHex.angle       # add the rotation of the tile already there to the preset rotation on the new tile
                    if angle > 6:
                        angle -=6
                    print("TileSides = " + str(tileSides) + " angle = " + str(angle) + " voidSides = " + str(locationHex.voidSides))
                    for eeSide in tileSides:                                # look at each side with a rail on it
                        if eeSide > 0:
                            testSide = eeSide + angle                           # rotate to the angle
                            if testSide > 6:
                                testSide -=6
                            if testSide in locationHex.voidSides:               # see if it is in voidSides
                                validRotation = False
                    offset = angle  
                if validRotation == True:
                    if (tile.tile_id, offset) not in self.possibleTiles:
                        self.possibleTiles.append((tile.tile_id, offset))   # add the tile number and rotation to the list
            print("****" + str(self.possibleTiles))
            return self.possibleTiles
        
        
    # method to rotate a tile, find all sides touched by rails and output a list of unique sides with rails (no repeats)
    def findSides(self, tile, angle):
        listOfSides = []
        for pair in tile.path_pairs:
            for i in range(2):
                pairSide = pair[i]
                if pairSide > 6:
                    pairSide -=6
                if pairSide not in listOfSides:
                    listOfSides.append(pairSide)
        return listOfSides
        
    
    # method to find hexes that surround the target hex
    def findAdjacentHexes(self, location):
        testList = []
        hexList = []
        locationFirst = location[0]
        locationSecond = location[1]
        # find the hexes around the location hex
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
            if loc not in self.off_board_hexes:
                hexList.append(loc)
            else:
                hexList.append((0,0))
        return hexList
        
    
    def findHex(self, id):
        print("id = " + str(id))
        for hexObj in self.board_hexagons:
            if hexObj.hex_id == id:
                return hexObj    #return the hex upon a match
        return None     #If there was no match, return None
        
    
    def checkThroughUnplayedTiles(self, targetTile):
        ind = 0
        while ind < len(self.unplayedTiles):
            if self.unplayedTiles[ind].tile_id == targetTile:
                return self.unplayedTiles[ind]
            else:
                ind += 1
        return None
            
    
    def updateHexWithTile(self, tileNumber, location, angle):
        hexLocation = self.hexDictionary[location]
        locationFirst = int(hexLocation[:2])                            # parsing out the tuple for board to use
        locationSecond = int(hexLocation[2:])
        boardLocation = (locationFirst, locationSecond)
        hex = self.findHex(boardLocation)                               # get the hex object...
        
        oldTile = hex.hexTile
        if oldTile > 0:
            swapTile = self.addTileBackOnUnplayedList(oldTile)
            if swapTile:
                self.unplayedTiles.append(swapTile)
        
        tile = self.removeTileFromUnplayedTiles(tileNumber)             # remove the tile from the unplayed list and add to played list
        hex.hexTile = tileNumber                                        # get the tile number assigned to the hex
        tileStations = tile.station_list
        tileEntryExit = tile.path_pairs
        rotatedEntryExit = []
        index = 0
        if angle > 0:                                                   # if the angle is greater than zero then rotate the tile...
            for pair in tileEntryExit:                                  # entry and exit by the rotation angle
                tEntry = int(pair[0])
                tExit = int(pair[1])
                tEntry += angle
                if tEntry > 6:                                          # if the angles are greater than 6 get them back into the...
                    tEntry -= 6                                         # range of zero to six
                tExit += angle
                if tExit > 6:
                    tExit -= 6
                if tileStations == ():                                  # need to add entry/exit/station to the hex so add the...
                    rotatedEntryExit.append([tEntry, tExit, 10])        # station to the entry/exit pair 0=no company 10=no station
                else:
                    for station in tileStations:
                        if int(station[1]) == index:
                            rotatedEntryExit.append([tEntry, tExit, 0])                 
                index +=1
        else:
            rotatedEntryExit = tileEntryExit                     

        hex.entryExitStation = rotatedEntryExit                         # set the hex's ees value
        hex.angle = angle                                               # set the hex's angle value
        print ("HexTile = " + str(hex.hexTile))
        print ("Hex EE = " + str(hex.entryExitStation))
        print("played = " + str(len(self.playedTiles)))
        print("unplayed = " + str(len(self.unplayedTiles)))
              
        
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
























