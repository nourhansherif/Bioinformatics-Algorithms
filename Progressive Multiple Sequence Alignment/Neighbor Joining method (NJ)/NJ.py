### NJ (Neighbor Joining method) ###
print("\nUsing Neighbor Joining method:\n")

## User DNA seq Input & System DNA seq Input System PreDefined distanceMatrix are available, just comment and uncomment.


### User input DNA Seq testing ###


# Take from user the number of sequences.
numSeq = int(input("Enter Number Of Sequences : "))
# Stores the DNA sequences 
seqMatrix = []

print("Please, Enter Equal Lengths Of Sequences !")

# Take from the user the DNA sequences and append them in the seqMatrix list
for counter in range(1,numSeq + 1):
	seq = input("Enter Sequence : ")
	seqMatrix.append(seq)

# Initializing the distances Matrix between the sequences as 2D array
distanceMatrix = [ [ 0 for j in range(numSeq) ] for i in range(numSeq) ]

# Initializing Taxa labels for the sequences.
taxaList = []
for i in range(ord('A'), ord('A') + len(seqMatrix)):
	taxaList.append(chr(i))
### End Of user input testing



#### System Input Of DNA Sequences 
#numSeq = 6
## Stores the distances between the sequences as list of lists
#distanceMatrix = [ [ 0 for j in range(numSeq) ] for i in range(numSeq) ]
#taxaList = ['A','B','C','D','E','F']
#seqMatrix = []
#seqMatrix.append("ATCGTGGTACTG")
#seqMatrix.append("CCGGAGAACTAG")
#seqMatrix.append("AACGTGCTACTG")
#seqMatrix.append("ATGGTGAAAGTG")
#seqMatrix.append("CCGGAAAACTTG")
#seqMatrix.append("TGGCCCTGTATC")
#### End of System DNA Input


print("\n_______________________________________\n")
print("Sequence Matrix : " + str(seqMatrix))
print("Labels : " + str(taxaList))

# Calculating the distance between sequences.
# Looping over the sequences in the seqMatrix
for i in range(1,len(seqMatrix)):
	# Looping over the rest of the sequences
	for n in range(i):
		dist = 0
		# Stores the Sequences as char list
		seq1 = list(seqMatrix[n])
		seq2 = list(seqMatrix[i])
		# Looping over the nucleotides in the DNA sequences
		for j in range(len(seqMatrix[i])):
			if (seq1 [j] != seq2 [j]):
				dist = dist + 1
		distanceMatrix[i][n] = dist

print("Distance Matrix Before: " + str(distanceMatrix))



## Pre-Initialized Distance Table (If want system test uncomment it & Comment user testing)
#taxaList = ['A', 'B', 'C', 'D', 'E', 'F']
#distanceMatrix = [ [ 0.0 for j in range(6) ] for i in range(6) ]
#distanceMatrix[1][0] = 5
#distanceMatrix[2][0] = 4
#distanceMatrix[2][1] = 7
#distanceMatrix[3][0] = 7
#distanceMatrix[3][1] = 10
#distanceMatrix[3][2] = 7
#distanceMatrix[4][0] = 6
#distanceMatrix[4][1] = 9
#distanceMatrix[4][2] = 6
#distanceMatrix[4][3] = 5
#distanceMatrix[5][0] = 8
#distanceMatrix[5][1] = 11
#distanceMatrix[5][2] = 8
#distanceMatrix[5][3] = 9
#distanceMatrix[5][4] = 8
#print("Taxas : " + str(taxaList))
#print("Distance Matrix Before: " + str(distanceMatrix))
### End Of system input 



# Calculates the distance between two Taxa
def calcDist(distMat, i, j):
	if i < j:
		i, j = j, i
	return distMat[i][j]
	
# Calculates the sumation of distances for a taxa.
def calcDistSum(distMat, i):
	sum = 0
	for k in range(len(distMat)):
		sum += distMat[i][k]
	for k in range(len(distMat)):
		sum += distMat[k][i]
	return sum
	
# Looping until reach only 2 clusters
while(len(distanceMatrix) != 2):
	
	# Calculating the whole Q matrix.
	q = [ [ 0 for j in range(len(distanceMatrix) )] for i in range(len(distanceMatrix)) ]
	for i in range(1, len(distanceMatrix)):
		for j in range(i):
			q[i][j] = (len(distanceMatrix))* calcDist(distanceMatrix, i, j) - calcDistSum(distanceMatrix, i) - calcDistSum(distanceMatrix, j)

	
	# Finding the minimum Q value to be combined
	taxaA = 0
	taxaB = 0
	minQ = 0
	for i in range(len(q)):
		for j in range(len(q)):
			if min(minQ, q[i][j]) == q[i][j]:
				minQ = q[i][j]
				taxaA = i
				taxaB = j

	# Initializing a new distance matrix
	newMat = [ [ 0.0 for j in range(len(distanceMatrix) - 1) ] for i in range(len(distanceMatrix) - 1) ]

	# Combining oldtaxa in taxalist to create new taxalist
	oldTaxaList = taxaList[:]
	oldTaxaList.remove(taxaList[taxaA])
	oldTaxaList.remove(taxaList[taxaB])
	newTaxaList = [[taxaList[taxaA], taxaList[taxaB]]] + oldTaxaList

	# Calculating the new distance matrix for the new combined taxa values
	for i in range(1, len(newMat)):
		oldI = taxaList.index(newTaxaList[i])
		# Calculating the distance from each of the oldTaxa to the new combined Taxa.
		distOldNewTaxaB = (calcDist(distanceMatrix, taxaB, taxaA)/2) + ((1./(2*(len(distanceMatrix)-2))) * (calcDistSum(distanceMatrix,taxaB) - calcDistSum(distanceMatrix, taxaA)))
		distOldNewTaxaA = (calcDist(distanceMatrix, taxaA, taxaB)/2) + ((1./(2*(len(distanceMatrix)-2))) * (calcDistSum(distanceMatrix,taxaA) - calcDistSum(distanceMatrix, taxaB)))

		newMat[i][0] = ((calcDist(distanceMatrix,taxaB,oldI) - distOldNewTaxaB) / 2) + ((calcDist(distanceMatrix,taxaA,oldI) - distOldNewTaxaA)/2)
		
		
	# Copy the rest of the old distance matrix to the new matrix.
	for i in range(2, len(newMat)):
		for j in range(1, len(newMat)-1):
			oldI = taxaList.index(newTaxaList[i])
			oldJ = taxaList.index(newTaxaList[j])
			newMat[i][j] = distanceMatrix[oldI][oldJ]
	
	# Making the old matrix equal the new matrix to start calculating again.
	distanceMatrix = newMat
	taxaList = newTaxaList


taxaList = str(taxaList).replace(' ', '').replace('[','(').replace(']',')').replace('\'','')
print("\n_______________________________________\n")
print("Average Distance Between all Branches calculated & Last Taxa : " + str(distanceMatrix[1][0]))
print("Joining Of Branches : " + str(taxaList))
print("Distance Matrix After: " + str(distanceMatrix))


			
	