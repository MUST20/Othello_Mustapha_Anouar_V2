# Fonction Minmax
from correct_movements import corecct_moves, BestMove

def SENDmove(server_request):
    playercolors = ['b','w']
    playerindice = server_request['state']['current']
    move = corecct_moves(playercolors[playerindice],server_request['state']['board'])
    if move == "":
        return {
                    "response": "move",
                    "move": "null",
                    "message": "nothing"
                }
    else :
        return {
                    "response": "move",
                    "move": BestMove(move),
                    "message": "good"
                }

