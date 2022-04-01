#!/usr/bin/python



### Global Alignment ###
print("___________________________________")
print("\nUsing Global Alignmet:\n")

# User input the sequences and Match, Mismatch, Gap values
seq1 = input("Enter 1st Sequence: ").upper()
seq2 = input("Enter 2nd Sequence: ").upper()
match = int(input("Enter Match value: "))
misMatch = int(input("Enter MisMatch value: "))
gap = int(input("Enter Gap value: "))

# Initializing a 2D matrix with 0
matrix = [ [ 0 for j in range(len(seq2) + 1) ] for i in range(len(seq1) + 1) ]

# Will carry the final score Of the Alignment
score = 0

# Initializing the First row with respect to the gap : F(i,0) = i . gap , 0 <= i <= Length Of Sequence 2
for i in range(0,len(seq1)+1):
	matrix[i][0] = i * gap
# Initializing the First column with respect to the gap : F(0,j) = j . gap , 0 <= j <= Length Of Sequence 1
for j in range(0,len(seq2)+1):
	matrix[0][j] = j * gap
	
# Initializing other cells in the matrix : F(i,j) = max (F(i,j-1) + gap , F(i-1,j) + gap, F(i-1,j-1) + matchOrmismatch (according to the sequence letter at that index))
for i in range(1,len(seq1)+1):
	for j in range(1,len(seq2)+1):
		# F(i,j-1) + gap
		horizontal = matrix[i][j-1] + gap
		# F(i-1,j) + gap
		vertical = matrix[i-1][j] + gap
		# F(i-1,j-1) + s(S1[i], S2[j])
		if seq2[j-1] == seq1[i-1]:
			diagonal = matrix[i-1][j-1] + match
		else: 
			diagonal = matrix[i-1][j-1] + misMatch
		# Getting max of the three scores
		matrix[i][j] = max(horizontal,vertical,diagonal)
		
# Printing the Matrix
print("\nThe Matrix:")
for i in range(0, len(seq1)+1):
	for j in range(0, len(seq2)+1):
		print(matrix[i][j], end = " ")
	print("\n")


# TraceBack

# Creating 2 variables to carry the alignments strings
alignment1 = ""
alignment2 = ""

# Begin TraceBack from last bottom right cell in matrix 
colNo = len(seq2)
rowNo = len(seq1)

# Looping on the matrix until reach left edge or top left of the matrix
while rowNo > 0 and colNo > 0:
	# Creating variables with the score of the current cell & its neighbouring cells (upper, left, diagonal).
	currentCell = matrix[rowNo][colNo]
	valueFromVerticalCell = matrix[rowNo][colNo - 1] + gap
	valueFromHorizontalCell = matrix[rowNo - 1][colNo] + gap
	if seq2[colNo - 1] == seq1[rowNo - 1]:
		valueFromDiagonalCell = matrix[rowNo - 1][colNo - 1] + match
	else: 
		valueFromDiagonalCell = matrix[rowNo - 1][colNo - 1] + misMatch
	
	# Determining which cell the current cell score was calculated from then updating rowNo & colNo
	if currentCell == valueFromHorizontalCell:
		alignment2 += '-'
		alignment1 += seq1[rowNo-1]
		rowNo -= 1
	elif currentCell == valueFromVerticalCell:
		alignment2 += seq2[colNo-1]
		alignment1 += '-'
		colNo -= 1
	elif currentCell == valueFromDiagonalCell:
		alignment2 += seq2[colNo-1]
		alignment1 += seq1[rowNo-1]
		rowNo -= 1
		colNo -= 1
	
# Finish the Tracing Up To The Top Left Cell In Matrix
while rowNo > 0:
	alignment2 += '-'
	alignment1 += seq1[rowNo-1]
	rowNo -= 1
while colNo > 0:
	alignment2 += seq2[colNo-1]
	alignment1 += '-'
	colNo -= 1

# Reversing the order of characters in alignment sequence as the tracing was from bottom right to Top left.
alignment1 = alignment1[::-1]
alignment2 = alignment2[::-1]

# Calculating the final score from the Alignment.
for i in range(0,len(alignment1)):
	if(alignment1[i] == alignment2[i]):
		score += match
	elif(alignment1[i] == "-" or alignment2[i] == "-"):
		score += gap
	else: 
		score += misMatch

# Printing the Alignment Sequences & The Score
print("Alignment 1: " + alignment1)
print("Alignment 2: " + alignment2)
print("Score: " + str(score))
if(score == matrix[len(seq1)][len(seq2)]):
	print("Score Calculated Successfully !\nThe Calculated Score From Alignment & The Score At The Last Cell In Matrix Are The Same.")
print("___________________________________")