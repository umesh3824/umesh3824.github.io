import copy
finalState=[[1,2,3],[4,5,6],[7,8,-1]]
initailState=[[1,2,3],[-1,4,6],[7,5,8]]

def countMisplcaed(CurrentState,final):
    count=0
    for i in range(3):
        for j in range(3):
            if(CurrentState[i][j]!=-1 and CurrentState[i][j]!=final[i][j]):
                count+=1
    return count


def findPosOfMinusOne(mat):
    for i in range(3):
        for j in range(3):
            if(mat[i][j]==-1):
                return [i,j]
               
                
def moveRight(mat,pos): 
    if(pos[1]==2):
        return None
    m=copy.deepcopy(mat)
    m[pos[0]][pos[1]],m[pos[0]][pos[1]+1]=m[pos[0]][pos[1]+1],m[pos[0]][pos[1]]
    return m
    
def moveLeft(mat,pos):
    if(pos[1]==0):
        return None
    m=copy.deepcopy(mat)
    m[pos[0]][pos[1]],m[pos[0]][pos[1]-1]=m[pos[0]][pos[1]-1],m[pos[0]][pos[1]]
    return m
    
def moveUp(mat,pos):
    if(pos[0]==0):
        return None
    m=copy.deepcopy(mat)
    m[pos[0]][pos[1]],m[pos[0]-1][pos[1]]=m[pos[0]-1][pos[1]],m[pos[0]][pos[1]]
    return m
    
    
def moveDown(mat,pos):
    if(pos[0]==2):
        return None
    m=copy.deepcopy(mat)
    m[pos[0]][pos[1]],m[pos[0]+1][pos[1]]=m[pos[0]+1][pos[1]],m[pos[0]][pos[1]]
    return m


def printMatrix(mat):
    for i in range(3):
        print(mat[i])
        
        
def printInitialAndFinalState(i,f):
    print("\n--------------------")
    print("Start State : ")
    printMatrix(i)
    print("\n--------------------")
    print("Goal State : ")
    printMatrix(f)
    print("\n--------------------")
    
    
def printAllStates(st):
    print("--------------------\n")
    for i in range(len(states)):
        print("State : ",i+1)
        printMatrix(states[i])
        print()
    print("--------------------")



def eightPuzzle(initialState,finalState):
    printInitialAndFinalState(initialState,finalState)
    gn=1
    explored=[]
    currentState=copy.deepcopy(initialState)
    while(currentState!=finalState):
        left=moveLeft(currentState,findPosOfMinusOne(currentState))
        right=moveRight(currentState,findPosOfMinusOne(currentState))
        up=moveUp(currentState,findPosOfMinusOne(currentState))
        down=moveDown(currentState,findPosOfMinusOne(currentState))
        fnl=99999
        fnr=99999
        fnu=99999
        fnd=99999
        
        if(left!=None):
            hnl=countMisplcaed(left,finalState)
            fnl=hnl+gn
            
        if(right!=None):
            hnr=countMisplcaed(right,finalState)
            fnr=hnr+gn
           
        if(up!=None):
            hnu=countMisplcaed(up,finalState)
            fnu=hnu+gn
           
        if(down!=None):
            hnd=countMisplcaed(down,finalState)
            fnd=hnd+gn
            
        
        minimum=min(fnl,fnr,fnu,fnd)
        
        if(minimum==fnl and (left not in explored)):
            currentState=copy.deepcopy(left)
            explored.append(left)
        elif(minimum==fnr and (right not in explored)):
            currentState=copy.deepcopy(right)
            explored.append(right)
        elif(minimum==fnu and (up not in explored) ):
            currentState=copy.deepcopy(up)
            explored.append(up)
        elif(minimum==fnd and (down not in explored)):
            currentState=copy.deepcopy(down)
            explored.append(down)
        gn+=1
      
    return explored
    
states=eightPuzzle(initailState,finalState)  
printAllStates(states)

