### Server output ######
ServerOutput = [
            [28, 35,2],
            [27, 36,20,3,4,5]
        ] # [W],[B]
#### Empty board ####
StateMap=[
["", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
] 
### Mapping server output ######
def Boarding(board):
    for indexW in board[0] :
        i=indexW // 8
        j= indexW % 8
        # print(i,j)
        StateMap[i][j]="w"
    for indexB in board[1] :
        i=indexB // 8
        j= indexB % 8
        StateMap[i][j]="b"
        # print(i,j) 

def corecct_moves(player,state):
    PossibleMove=[]
    for i in range(8):
        for j in range(8):
            if(state[i][j]==""):
                nn,l1=support(player,-1,0,i,j,state,0)
                ww,l2=support(player,0,-1,i,j,state,0)
                ee,l3=support(player,0,1,i,j,state,0)
                ss,l4=support(player,1,0,i,j,state,0)
                ne,l5=support(player,-1,-1,i,j,state,0)
                nw,l6=support(player,-1,1,i,j,state,0)
                se,l7=support(player,1,-1,i,j,state,0) 
                sw,l8=support(player,1,1,i,j,state,0)
                if(nn or ww or ee or ss or ne or nw or se or sw):
                    StateMap[i][j]=player.upper()    
                    index = i*8+j
                    PossibleMove.append (index)              
    return StateMap, PossibleMove 

#### identify oponent ####   
def opponent(s):
    if s=="b":
        return "w"
    elif s=="w":
        return "b"
    else:
        return("problem")        

###### Check moves part 1#####
def support(s,di,dj,i,j,state,score):
    other=opponent(s)
    if(other=="problem"):
        return False,0
    if i+di>7 or i+di<0:
        return False,0
    if j+dj>7 or j+dj<0:
        return False,0
    if(state[i+di][j+dj]!=other):
        return False,0
    if i+2*di>7 or i+2*di<0:
        return False,0
    if j+2*dj>7 or j+2*dj<0:
        return False,0
    return check(s,di,dj,i+2*di,j+2*dj,state,score)         
        
    
###### Check moves part 2#####
def check(s,di,dj,i,j,state,score):
    if state[i][j]==s:
        score=score+1 
        return True,score
    if i+di>7 or i+di<0:
        return False,0
    if j+dj>7 or j+dj<0:
        return False,0
    if state[i][j]=="":
        return False,0
    score=score+1    
    l,s=check(s,di,dj,i+di,j+dj,state,score)  
    return l,s     

### Update StateMap####
Boarding(ServerOutput)

new_b, possibleMove=corecct_moves("w",StateMap)

print("Possible Moves list: {} ".format(possibleMove))
print("Possible Moves maping: ")
for i in range(len(new_b)):
    print(new_b[i])
    # print("\n")
