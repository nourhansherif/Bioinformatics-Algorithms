

### Nussinov Algorithm ###


def fillMatrix(sequence,matrix,basePairs,directions):
    
    rowFinalCell=0
    colFinalCell=len(sequence)

    for i in range(0,len(sequence)-1,1):
        currentRow=0
        currentCol=i+1

        if currentRow==rowFinalCell and currentCol ==colFinalCell:
                break
            
        while True:
            
            
            diagonalResult= matrix[currentRow+1][currentCol-1]

            if basePairs[sequence[currentRow]] is sequence[currentCol]:
                
                diagonalResult+=1
                

            leftResult =matrix[currentRow][currentCol-1]

            downResult=matrix[currentRow+1][currentCol]

            bifurcationResult,maxK=getMaxForBifurcation(matrix,currentRow,currentCol)

            
            results = (diagonalResult,leftResult,downResult,bifurcationResult)
            maximum = max(results)

            if maximum== downResult:
                directions[currentRow][currentCol]="down"
            elif maximum==diagonalResult:
                directions[currentRow][currentCol]="diagonal"
            elif maximum== leftResult:
                directions[currentRow][currentCol]="left"
            
            elif maximum==bifurcationResult:
                directions[currentRow][currentCol]="bifurcation,"+str(currentRow)+","+str(currentCol)+","+str(maxK)

            matrix[currentRow][currentCol]=maximum
            currentRow=currentRow+1
            currentCol=currentCol+1
            
            if currentRow >len(sequence)-2-i:
                break
            
    return matrix ,directions

    
def getMaxForBifurcation(matrix,currentRow,currentCol):
    maxValue=0
    maxK=0
    for k in range (currentRow+1,currentCol,1):
        value=matrix[currentRow][k]+matrix[k+1][currentCol]
        if value>maxValue:
            maxValue=value
            maxK=k
            
    return maxValue,maxK


def traceBack(directions,currentRow,currentCol,traceBackList):

    if directions[currentRow][currentCol] == "0":
        return traceBackList

    if directions[currentRow][currentCol]=="down":
        
        traceBackList=traceBack(directions,currentRow+1,currentCol,traceBackList)

    elif directions[currentRow][currentCol]=="diagonal":
        
        lower=min(currentRow,currentCol)
        higher=max(currentRow,currentCol)
        traceBackList[lower]='('
        traceBackList[higher]=')'
        
        traceBackList=traceBack(directions,currentRow+1,currentCol-1,traceBackList)
    elif directions[currentRow][currentCol]=="left":
        
            
        traceBackList=traceBack(directions,currentRow,currentCol-1,traceBackList)

    elif "bifurcation" in directions[currentRow][currentCol]:
        
        values=directions[currentRow][currentCol].split(',')
        kRow=int(values[1])
        kCol=int(values[2])
        k=int(values[3])
        traceBackList=traceBack(directions,kRow,k,traceBackList)
        traceBackList=traceBack(directions,k+1,kCol,traceBackList)
            
            
    
    return traceBackList



basePairs={'A':'U','U':'A','C':'G','G':'C'}

sequence=input("Enter RNA Sequence:")

matrix =[ [ 0 for i in range(len(sequence)) ] for j in range(len(sequence)) ]
directions=[ [ '0' for i in range(len(sequence)) ] for j in range(len(sequence)) ]


matrix,directions=fillMatrix (sequence,matrix,basePairs,directions)

traceBackList=[]
for i in range(len(sequence)):
    traceBackList.append('.')

traceBackList=traceBack(directions,0,len(sequence)-1,traceBackList)

print("".join(traceBackList))

for i in range (len(sequence)):
    for j in range (len(sequence)):
        if not j+1==len(sequence):
            print (matrix[i][j],',',end="")
        else:
            print(matrix[i][j])

#Seq 1: UAACGUACUGGAGUA
#Seq 2: GGAAUUAGUUAACC
#Seq 3: GGGAAAUCC
#Seq 4: CGGACCCAGACUUUC
#Seq 5: GGGGGUAUAGCUCAGUUGGUAGAGCGCUGCCUUUGCACGGCAGAUGUCAGGGGUUCGAGUCCCCUUACCUCCA
        
    

            
            
            