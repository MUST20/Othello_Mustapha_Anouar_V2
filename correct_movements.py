board = [
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", " ", " ", ""],
    ["", "", "", "w", "w", "", "", ""],
    ["", "", "b", "w", "w", "", "", ""],
    ["", "", "", "", "b", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
]
leagal_moves=[]

def corecct_moves(s,position):
    a=[
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ]  
    for i in range(8):
        for j in range(8):
            if(position[i][j]==""):
                nn,s1=support(s,-1,0,i,j,position,0)
                ww,s2=support(s,0,-1,i,j,position,0)
                ee,s3=support(s,0,1,i,j,position,0)
                ss,s4=support(s,1,0,i,j,position,0)
                ne,s5=support(s,-1,-1,i,j,position,0)
                nw,s6=support(s,-1,1,i,j,position,0)
                se,s7=support(s,1,-1,i,j,position,0) 
                sw,s8=support(s,1,1,i,j,position,0)
                if(nn or ww or ee or ss or ne or nw or se or sw):
                    a[i][j]=s   
                    print(s1+s2+s3+s4+s5+s6+s7+s8) 
    return a            

def other(s):
    if s=="b":
        return "w"
    elif s=="w":
        return "b"
    else:
        return("problem")        


def support(s,di,dj,i,j,position,score):
    autre=other(s)
    if(autre=="problem"):
        return False,0
    if i+di>7 or i+di<0:
        return False,0
    if j+dj>7 or j+dj<0:
        return False,0
    if(position[i+di][j+dj]!=autre):
        return False,0
    if i+2*di>7 or i+2*di<0:
        return False,0
    if j+2*dj>7 or j+2*dj<0:
        return False,0
    return check(s,di,dj,i+2*di,j+2*dj,position,score)         
        
    

def check(s,di,dj,i,j,position,score):
    if position[i][j]==s:
        score=score+1 
        return True,score
    if i+di>7 or i+di<0:
        return False,0
    if j+dj>7 or j+dj<0:
        return False,0
    if position[i][j]=="":
        return False,0
    score=score+1    
    l,s=check(s,di,dj,i+di,j+dj,position,score)  
    return l,s     




new_b=corecct_moves("b",board)

for i in range(len(new_b)):
    print(new_b[i])
    print("\n")

