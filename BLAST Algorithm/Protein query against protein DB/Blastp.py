#!/usr/bin/env python3

blosum62 = {
	('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0,
	('Q', 'Q'): 5, ('N', 'A'): -2, ('Z', 'Y'): -2, ('W', 'R'): -3,
	('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1,
	('H', 'D'): -1, ('L', 'N'): -3, ('W', 'A'): -3, ('Y', 'M'): -1,
	('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
	('Y', 'A'): -2, ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7,
	('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
	('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2,
	('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('V', 'S'): -2,
	('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2,
	('K', 'K'): 5, ('P', 'D'): -1, ('I', 'H'): -3, ('I', 'D'): -3,
	('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
	('P', 'H'): -2, ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1,
	('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1, ('D', 'R'): -2,
	('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2,
	('Z', 'W'): -3, ('F', 'E'): -3, ('D', 'N'): 1, ('B', 'K'): 0,
	('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0,
	('F', 'M'): 0, ('B', 'C'): -3, ('Z', 'I'): -3, ('Z', 'V'): -2,
	('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
	('N', 'N'): 6, ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3,
	('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0, ('L', 'E'): -3,
	('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0,
	('N', 'R'): 0, ('H', 'C'): -3, ('Y', 'N'): -2, ('G', 'Q'): -2,
	('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2,
	('G', 'A'): 0, ('K', 'R'): 2, ('E', 'D'): 2, ('Y', 'R'): -2,
	('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
	('T', 'A'): 0, ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1,
	('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1, ('K', 'H'): -1,
	('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2,
	('V', 'V'): 4, ('M', 'I'): 1, ('T', 'Q'): -1, ('I', 'G'): -4,
	('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1,
	('Z', 'D'): 1, ('F', 'R'): -3, ('X', 'K'): -1, ('Q', 'D'): 0,
	('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
	('B', 'L'): -4, ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2,
	('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
	('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1,
	('W', 'L'): -2, ('H', 'R'): 0, ('W', 'H'): -2, ('H', 'N'): 1,
	('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4,
	('L', 'D'): -4, ('B', 'I'): -3, ('L', 'H'): -3, ('S', 'N'): 1,
	('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
	('Y', 'G'): -3, ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1,
	('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2, ('E', 'E'): 5,
	('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2,
	('P', 'R'): -2, ('V', 'G'): -3, ('T', 'L'): -1, ('V', 'K'): -2,
	('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1,
	('P', 'F'): -4, ('I', 'N'): -3, ('K', 'I'): -3, ('M', 'D'): -3,
	('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
	('K', 'A'): -1, ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4,
	('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1, ('X', 'F'): -1,
	('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3,
	('F', 'C'): -2, ('Z', 'Q'): 3, ('X', 'Z'): -1, ('F', 'G'): -3,
	('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2,
	('X', 'R'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('Z', 'F'): -3,
	('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
	('L', 'C'): -1, ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4,
	('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0, ('S', 'I'): -2,
	('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2,
	('Y', 'D'): -3, ('E', 'R'): 0, ('X', 'P'): -2, ('G', 'G'): 6,
	('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3,
	('T', 'K'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('T', 'C'): -1,
	('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
	('C', 'R'): -3, ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1,
	('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('M', 'G'): -3,
	('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1,
	('I', 'A'): -1, ('P', 'I'): -3, ('R', 'R'): 5, ('X', 'M'): -1,
	('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1,
	('Z', 'N'): 0, ('X', 'A'): 0, ('B', 'R'): -1, ('B', 'N'): 3,
	('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
	('B', 'F'): -3, ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4
}
#Step 1
def removeLowSequences(protein):
	
	proteinToBlosum = ''
	for i in range (len(protein)):
		proteinToBlosum = proteinToBlosum + str(blosum62[protein[i],protein[i]])
	for i in range (len(protein)+1):
		region = ''
		for j in range (i,len(protein),1):
			region = region + str(blosum62[protein[j],protein[j]])
			if region == 'X':
				break 
			index = proteinToBlosum.find(region, j)
			if index == j+1:
				countOfRepetition=1
				
				for x in range(index,len(protein),1):
					index2=proteinToBlosum.find(region,x)
					if index==index2:
						countOfRepetition+=1
					else :break;
					
				numberOfNToBeAdded=((countOfRepetition+1)*len(region))
				protein=protein[:j-1]+'X'*numberOfNToBeAdded+protein[j+numberOfNToBeAdded-1:]
				break
			
	return protein       

#Step 2
def getSubStrings(protein):
    words=[]
    for i in range (len(protein)+1):
        if (i+3<=len(protein)):
            words.append(protein[i:i+3])
    return words

def getScore(firstProtein,secondProtein):
        score=0
        for i in range (3):
                if (firstProtein[i],secondProtein[i])in blosum62:
                        score+= blosum62[firstProtein[i],secondProtein[i]]
                else:
                        score+= blosum62[secondProtein[i],firstProtein[i]]
        return score
def getScoreOfOne(protein):
        score=0
        for i in range (3):
                score+= blosum62[protein[i],protein[i]]
        return score

#Step 3

def getCombinations(proteinWords):
	
    scoresOfWords={}
    aminoAcidsList = ["A","G","C","T","R","N","D","Q","E","H","I","L","K","M","F","P","S","W","Y","V","B","Z","X"]
    for protein in proteinWords:
            scoresOfWords[protein]=getScore(protein,protein)
            print (protein+" "+str(scoresOfWords[protein]))
            for i in range (len( protein)):
                    for j in range (len (aminoAcidsList)):
                            if protein[i]==aminoAcidsList[j]:
                                    continue
                            else:
                                     newProtein=protein[0:i]+aminoAcidsList[j]+ protein[i+1:]
                                     scoresOfWords[newProtein]=getScore(protein,newProtein)
								
								
    return scoresOfWords

#Step 4    
def ChooseBigger(proteinWords):
    T=14
    NewScoresOfWords = {}
    for protein in proteinWords:
        variable =proteinWords[protein]
        if  variable >= T:
         NewScoresOfWords[protein]=variable
			
    return NewScoresOfWords    


#Step 5
def Hits(NewScoresOfWords):
	searchfile = open("/Users/nourhan/Desktop/Bioinformatics/Lab Example/protein copy.txt", "r")
#	searchfile = open("/Users/nourhan/Desktop/Bioinformatics/A Foreign Example/protein Database.txt", "r")
	wordsHit = {}
	for line in searchfile:
		listOfSeedsHit=[]
		for protein in NewScoresOfWords:
			if protein in line:
				listOfSeedsHit.append(protein)
		if len(listOfSeedsHit) > 0:
				wordsHit[line.rstrip('\n')] = listOfSeedsHit
	searchfile.close()
	return wordsHit

def indexOfWordHitsInDB(DBLine,words):
	indexList = []
	for word in words:
		indexList.append(DBLine.index(word))
	return indexList

def indexOfWordHitsInQuerySeq(Query,words):
	indexList = []
	for word in words:
		if word in Query:
			indexList.append(Query.index(word))
	return indexList
	
	
#Step 6
def extend(Query,wordsHit):
	
	TotalScoreOfEachDBLine = []
	T = 15
	print ("Query Sequence: " + Query + "\n")
	for DBLine in wordsHit:
		
		print ("Database Sequence: " + DBLine)
		
		words = []
		words = wordsHit[DBLine]
		print("Words Hit in this Sequence: " + str(words))
		
		indexListDB = indexOfWordHitsInDB(DBLine,words)
		print("The index of Words Hit in this Sequence: " + str(indexListDB))
		
		indexListQuery = indexOfWordHitsInQuerySeq(Query,words)
		if len(indexListQuery) == 0:
			print("Word is not in Query Sequence !")
			continue
		else: print("The index of Words Hit in Query Sequence: " + str(indexListQuery))
		
		scoreList = []
		TotalScoreInLine = 0
		for i in range(len(words)):

			print("________________________")
			print("Seed " + str(i+1) + " : " + words[i])
			score = NewScoresOfWords[words[i]]
			print ("Score Of Seed: " + str(NewScoresOfWords[words[i]]))
			print ("Its index in DB: " + str(indexListDB[i]))
			print ("Its index in Query: " + str(indexListQuery[i]))
			
			indexInQueryLeft = indexListQuery[i] - 1
			indexInQueryRight = indexListQuery[i] + 3
			indexInDBLeft = indexListDB[i] - 1
			indexInDBRight = indexListDB[i] + 3
			
			print("Extending Left")
			tempLeft = score
			while indexInQueryLeft >= 0 and indexInDBLeft >=0:
				
				if (Query[indexInQueryLeft],DBLine[indexInDBLeft]) in blosum62:
					tempLeft += blosum62[Query[indexInQueryLeft],DBLine[indexInDBLeft]]
				else:
					tempLeft += blosum62[DBLine[indexInDBLeft],Query[indexInQueryLeft]]
				
				if tempLeft < T:
					break
				else:
					score = tempLeft
				
				indexInQueryLeft = indexInQueryLeft - 1
				indexInDBLeft = indexInDBLeft - 1
				
			print("Score after extending Left: " + str(score))
			
			
			print("Extending Right")
			tempRight = score
			while indexInQueryRight != len(Query) and indexInDBRight != len(DBLine):
				
				if (Query[indexInQueryRight],DBLine[indexInDBRight]) in blosum62:
					tempRight += blosum62[Query[indexInQueryRight],DBLine[indexInDBRight]]
				else:
					tempRight += blosum62[DBLine[indexInDBRight],Query[indexInQueryRight]]
					
				if tempRight < T:
					break
				else:
					score = tempRight
					
				indexInQueryRight = indexInQueryRight + 1
				indexInDBRight = indexInDBRight + 1
				
			print("Score after extending Right: " + str(score))
				
#			scoreList.append(score)
#			print(scoreList)
			TotalScoreInLine += score
			print("Total Score of HSP: " + str(score))
			
			
			
		TotalScoreOfEachDBLine.append(TotalScoreInLine)
		print("________________________\n")
		print("Total Score in DB Line: " + str(TotalScoreInLine))
		print("________________________\n")
	return TotalScoreOfEachDBLine


def Display(TotalScoreOfEachDBLine,wordsHit):
	
	index = 0
	for DBLine in wordsHit:
		print("DataBase Sequence : " + DBLine)
		if len(TotalScoreOfEachDBLine) == 0:
			print("No appropriate Hits Here !")
		else: print("Total: " + str(TotalScoreOfEachDBLine[index]))
		index = index + 1


proteinSequence= 'PQGGVNVDVEFG'

#proteinSequence = 'MAAGGSGAESAPPTPSMSSLPLAALNVRVRHRLSLFLNVRTQVAADWTGLAEEMNFEYLEIRRLETHPDPTRSLLDDWQGRPGASVGRLLELLAKLGRDDVLVELGPSIEEDCRKYILKQQQEAAEKPLQVDSVDSSIPWMSGITIRDDPLGQMPEHFDAFICYCPSDIQFVQEMIRQLEQTNYRLKLCVSDRDVLPGTCVWSIASELIEKRCRRMVVVVSDDYLQSKECDFQTKFALSLSPGAHQKRLIPVKYKSMKKEFPSILRFITVCDYTNPCTKSWFWTRLARALSLP'


newProtein = removeLowSequences(proteinSequence)
print ("Step 1: " + newProtein)
#newProtein = 'PQGGVNVDVEFG'
newProtein = newProtein.replace("X","")
print("New Query: " + newProtein)
print("____________________________________________")

wordList=[]
wordList=getSubStrings(newProtein.replace("X",""))
print ("Step 2: "+ str(wordList))

scoresOfWords={}
scoresOfWords=getCombinations(wordList)
print("____________________________________________")

print ("Step 3: "+ str(scoresOfWords))
print ("Step 3: "+ str(len(scoresOfWords)))
print("____________________________________________")

NewScoresOfWords={}
NewScoresOfWords=ChooseBigger(scoresOfWords)
print ("Step 4: "+ str(NewScoresOfWords))
print ("Step 4: "+ str(len(NewScoresOfWords)))
print("____________________________________________")

wordsHit= []
wordsHit = Hits(NewScoresOfWords)
print ("Step 5: "+ str(wordsHit))
print("____________________________________________")

print("Step 6: ")
TotalScoreOfEachDBLine = extend(newProtein,wordsHit)
print("____________________________________________")

print("Step 7: ")
Display(TotalScoreOfEachDBLine,wordsHit)
