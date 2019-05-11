compTake1 = 0
compTake2 =0
forList= []
numPiles = 0
piles = []
bins = [0]*numPiles
nimSums = 0
nimNums= [0]*numPiles
pileSums = [0]* numPiles
pileNums = [0]* numPiles
pile = 0
taken = 0
dif =0
def nimWin():
    """ starts the game"""
    gameStart()
    printer()
    while True:
        playerTurn()
        if winCheck() == False:
            print "You Win!"
            break
        compTurn()
        if winCheck() == False:
            print "I win again!"
            break
    print "Game Over!"
def gameStart():
    """Starts by asking the user how many piles they want and how many in each pile"""
    global piles
    global numPiles
    numPiles = int(raw_input("How many piles do you want to play with? "))
    piles = [0] * numPiles
    forListConst()
    tempPiles = numPiles
    while tempPiles > 0:
        piles[(tempPiles-1)] = int(raw_input("How many in pile " + str(tempPiles) +"? "))
        tempPiles-= 1
    return piles

def preTurn():
    """Updates all values before each turn"""
    global piles
    global bins
    global nimSums
    global pileSums
    global numPiles
    binMaker()
    nimSums= nimComp(bins)
    pileSums =  map(pileSumComp, bins)
    pileNumComp()
def playerTurn():
    """The players turn"""
    global numPiles
    global piles
    global taken
    global pile
    preTurn()
    pile= int(raw_input("Which pile are you taking from? "))
    while pile > numPiles:
        print "That pile does not exist"
        pile = int(raw_input("Which pile are you taking from? "))
    while pile < 0:
        print "Please enter a positive number."
        pile = int(raw_input("Which pile are you taking from? "))
    while piles[pile-1] == 0:
        print "You can't take coins from an empty pile"
        pile = int(raw_input("Which pile are you taking from? "))
    taken = int(raw_input("How many are you taking from that pile? "))
    while taken < 0:
        print "You can't take a negative amount of coins"
        taken = int(raw_input("How many are you taking from that pile? "))
    while taken > piles[pile-1]:
        print "You can't take more coins than are in the pile"
        taken = int(raw_input("How many are you taking from that pile? "))
    if piles[pile-1] > 0:        
        piles[pile-1] = int(piles[pile-1]) - taken
        pileNums[pile-1] = piles[pile-1] - taken
    else:
        return piles
    printer()
def numToBinary(N):
    """Takes a decimal number and converts it to binary"""
    if N == 0:
        return '0'
    else:
        return numToBinary(N/2) + str(N%2)
def padder(O):
    """Pads the binary numbers to 5 digits so they are the same length"""
    while len(O) < 5:
        O= '0' + O
    return O        
def compTurn():
    """The computer makes the optimal move"""
    preTurn()
    compare()
    printer()
def binMaker():
    """ converts the piles list into binary numbers"""
    global bins
    global piles
    tempBins = map(numToBinary, piles)
    bins = map(padder, tempBins)
def nim_sum(x,y):
    """Finds the exclusive or sum of the numbers"""
    nimSum = int(x) ^ int(y)
    return padder(str(nimSum))    
def nimComp(P):
    """Uses nim_sum helper function to compute nim sum of the game"""
    return reduce(nim_sum,P)
def pileSumComp(T):
    """ takes a number and gives the exclusive or against the nimSum"""
    global nimSums
    pileSum = int(nimSums) ^ int(T)
    return padder(str(pileSum))
def binaryToNum(S):
    """ converts a base-2 number to base-10"""
    if S =='':
        return 0
    elif len(S) == 1:
        return int(S)
    else:
        return 2*(binaryToNum(S[:-1])) + int(S[-1])
def pileNumComp():
    """Computes the decimal pile sums"""
    global pileNums
    global nimNums
    nimNums = map(binaryToNum, bins)
    pileNums = map(binaryToNum, pileSums)
def forListConst():
    """Makes a list that can be used for for loops"""
    global numPiles
    global forList
    forList = [0]* numPiles
    numTemp = numPiles
    count = 0
    while numTemp >0:
        forList[count] = count
        count+= 1
        numTemp-= 1
    return forList
def compare():
    """ Performs the best move, and if it can't it subtracts one from a pile """
    global pileNums
    global piles
    global nimNums
    for i in forList:
        if pileNums[i] < piles[i]:                                       
            dif = piles[i] - pileNums[i]
            piles[i] = piles[i] - (dif)                                     
            print('I remove ' + str(dif) + ' from pile ' + str(i+1))
            break
    if piles == pileNums:   
        for i in forList:                                     
            if piles[i] > 0:
                piles[i] = piles[i] -1
                print('I remove ' + str(1) + ' from pile ' + str(i+1))
                break
    else:
        return pileNums
def winCheck():
    """Checks to see if someone won"""
    global piles
    if piles == ([0]*numPiles):
        return False
    else:
        return True
def printer():
    """Prints the scoreboard"""
    global piles
    for i in forList:
        print "Pile " + str(i+1) + ": " + str(piles[i]) + " coins"
if __name__ == "__main__" :
    """ Runs the game automatically """
    nimWin()
