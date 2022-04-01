### UPGMA (Unweighted Pair Group Method with Arithmetic Mean) ###
print("\nUsing UPGMA:\n")

## User DNA seq Input & System DNA seq Input System PreDefined distanceMatrix are available, just comment and uncomment.


### User input DNA Seq testing ###

# Stores the distances between the sequences as list of lists
distanceMatrix = []
# Stores the distance between the sequences in the row.
row = []
# Storing an empty list for first cell bet seq A and seq A diagonal
distanceMatrix.append(row)
# Take from user the number of sequences.
numSeq = int(input("Enter Number Of Sequences : "))
# Stores the DNA sequences 
seqMatrix = []

print("Please, Enter Equal Lengths Of Sequences !")

# Take from the user the DNA sequences and append them in the seqMatrix list
for counter in range(1,numSeq + 1):
	seq = input("Enter Sequence : ")
	seqMatrix.append(seq)

# Initializing labels for the sequences.
labels = []
for i in range(ord('A'), ord('A') + len(seqMatrix)):
	labels.append(chr(i))

### End Of user input testing



#### System Input Of DNA Sequences 
#
## Stores the distances between the sequences as list of lists
#distanceMatrix = []
## Stores the distance between the sequences in the row.
#row = []
## Storing an empty list for first cell bet seq A and seq A diagonal
#distanceMatrix.append(row)
#labels = ['A','B','C','D','E','F']
#numSeq = 6
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
print("Labels : " + str(labels))


# Calculating the distance between sequences.
# Looping over the sequences in the seqMatrix
for i in range(1,len(seqMatrix)):
	# Initializing a new row list
	row = []
	# Looping over the rest of the sequences
	for n in range(i):
		dist = 0
		# Stores the Sequences as char list
		seq1 = list(seqMatrix[n])
		seq2 = list(seqMatrix[i])
		# Looping over the nucleotides in the DNA sequences
		for j in range(len(seqMatrix[i])):
			if (seq1 [j] != seq2 [j]):
				dist = dist+1
		row.append(dist)
	distanceMatrix.append(row)

print("Distance Matrix Before: " + str(distanceMatrix))





## Pre-Initialized Distance Table (If want system test uncomment it & Comment user testing)

#labels = ['A','B','C','D','E']
#
#distanceMatrix = [
#	[],                         #A
#	[20],                       #B
#	[60, 50],                   #C
#	[100, 90, 40],              #D
#	[90, 80, 50, 30],           #E
#	]
#print("Labels : " + str(labels))
#print("Distance Matrix Before: " + str(distanceMatrix))



# Looping until reach only 2 clusters
while(len(labels) > 2):
	# Initializing minCell with an infinity (Very Large number)
	minCell = float("inf")
	# Initializing index of minCell with -1 as there is no index by this value
	minRowIndex, minColIndex = -1, -1

	# Search for the lowest distance value in the Matrix
	for i in range(len(distanceMatrix)):
		for j in range(len(distanceMatrix[i])):
			if distanceMatrix[i][j] < minCell:
				minCell = distanceMatrix[i][j]
				minRowIndex, minColIndex = i, j
	
	
	# Joining the 2 sequences entries by calculating distances averages.
	
	# Checks which index is smaller to swap them to get the value from the side that has the value 
	# because the distances are in lower triangle form
	if minColIndex < minRowIndex:
		minRowIndex, minColIndex = minColIndex, minRowIndex

	# Re-construct the row at lower index with the new average distance 
	row = []
	for i in range(0, minRowIndex):
		row.append((distanceMatrix[minRowIndex][i] + distanceMatrix[minColIndex][i]) / 2)
	distanceMatrix[minRowIndex] = row
	
	# Re-construct the column at lower index with the new average distance
	for i in range(minRowIndex + 1, minColIndex):
		distanceMatrix[i][minRowIndex] = (distanceMatrix[i][minRowIndex] + distanceMatrix[minColIndex][i])/2
		
	# Getting the rest of the values from row i
	for i in range(minColIndex + 1, len(distanceMatrix)):
		distanceMatrix[i][minRowIndex] = (distanceMatrix[i][minRowIndex] + distanceMatrix[i][minColIndex])/2
		# Removing the second index column entry
		del distanceMatrix[i][minColIndex]

	# Removing the second index row
	del distanceMatrix[minColIndex]

	# Joining the Labels 
	
	# Checks which index is smaller to swap them to get the value from the side that has the value 
	# because the distances are in lower triangle form
	if minColIndex < minRowIndex:
		minRowIndex, minColIndex = minColIndex, minRowIndex

	# Joining the labels in the first index
	labels[minRowIndex] = "(" + labels[minRowIndex] + "," + labels[minColIndex] + ")"

	# Removing the label in the second index
	del labels[minColIndex]
	

print("\n_______________________________________\n")
print("Cluster 1: " + str(labels[0])) 
print("Cluster 2: " + str(labels[1])) 
print("Average Distance Between Cluster 1 & Cluster 2 : " + str(distanceMatrix[1]))
print("\nClusters : " + str(labels))
print("Distance Matrix After: " + str(distanceMatrix))
