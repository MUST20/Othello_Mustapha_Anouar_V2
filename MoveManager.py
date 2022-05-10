class BadMove(Exception):
	pass

directions = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0),
    ( 1,  1),
    (-1,  1),
    ( 1, -1),
    (-1, -1)
]

def add(p1, p2):
    l1, c1 = p1
    l2, c2 = p2
    return l1 + l2, c1 + c2

def coord(index):
    return index // 8, index % 8
    
def isInside(coord):
    l, c = coord
    return 0 <= l < 8 and 0 <= c < 8

def walk(start, direction):
    current = start
    while isInside(current):
        current = add(current, direction)
        yield current

def index(coord):
    l, c = coord
    return l*8+c

def willBeTaken(state, move):
    playerIndex = state['current']
    otherIndex = (playerIndex+1)%2

    if not (0 <= move < 64):
        raise BadMove('Your must be between 0 inclusive and 64 exclusive')

    if move in state['board'][0] + state['board'][1]:
        raise BadMove('This case is not free')

    board = []
    for i in range(2):
        board.append(set((coord(index) for index in state['board'][i])))

    move = coord(move)

    cases = set()
    for direction in directions:
        mayBe = set()
        for case in walk(move, direction):
            if case in board[otherIndex]:
                mayBe.add(case)
            elif case in board[playerIndex]:
                cases |= mayBe
                break
            else:
                break

    if len(cases) == 0:
        raise BadMove('Your move must take opponent\'s pieces')
    
    # return [index(case) for case in cases]
    return len(cases)



def possibleMoves(state):
    PossibleMoves = []
    PawnsDestroyed= []
    for move in range(64):
        try:
            PawnsDestroyed.append(willBeTaken(state, move))
            PossibleMoves.append(move)
        except BadMove:
            pass
    return PossibleMoves,PawnsDestroyed

def maximumIndices(liste):
    maxi = liste[0]
    longueur=len(liste)
    for i in range(longueur):
        if liste[i] >= maxi:
            maxi = liste[i]
    return maxi


def BestMove(PossibleMoves,PawnsDestroyed):
    if PossibleMoves!=[]:
        a = maximumIndices(PawnsDestroyed)
        b = PawnsDestroyed.index(a)
        c = PossibleMoves[b]
        print("taken move :" )
        print(c)
        return c
    else : 
        null = None
        return null
