import time

# These functions are used for both single and paired reads
def readSolution(fileName):
    return open(fileName).readline().strip()

def getMers(reads):
    length = len(reads[0]) - 1
    mers = []
    for read in reads:
        for i in range(len(read) - length + 1):
            mers.append(read[i : length + i])
    return mers

def findPath(pairedDict):
    for key in pairedDict.keys():
        found = False
        for value in pairedDict.values():
            if (value == key):
                found = True
                break
        if not found:
            start = key
            break

    for value in pairedDict.values():
        found = False
        for key in pairedDict.keys():
            if (value == key):
                found = True
                break
        if not found:
            end = value
            break
    return start, end
################################################################################################
"""
PAIRED READS
"""
def readRegularTextFilePaired(fileName):
    fileContent = open(fileName).readlines()
    firstLineContent = fileContent[0].split(" ")
    lengthOfReads = int(firstLineContent[0])
    gapValue = int(firstLineContent[1])
    readsForward = []
    readsBackward = []
    
    for line in fileContent[1:]:
        lineContent = line.strip().split("|")
        readsForward.append(lineContent[0])
        readsBackward.append(lineContent[1])
    return lengthOfReads, gapValue, readsForward, readsBackward

def createPairedDict(forwardMers, backwardMers):
    pairedDict = {}
    for i in range(0, len(forwardMers), 2):
        pairedDict[(forwardMers[i], backwardMers[i])] = (forwardMers[i + 1], backwardMers[i + 1])
    return pairedDict

def concatenatePaired(start, end, pairedDict, index):
    if index == 'Forward':
        index = 0
    elif index == 'Backward':
        index = 1
        
    seq = start[index]
    for i in range(len(pairedDict)):
        if pairedDict.get(start) == None:
            return seq
        else:
            seq += pairedDict.get(start)[index][-1]
            start = pairedDict.get(start)
    return seq

def assembly(prefix, suffix, length, gap):
    return prefix + suffix[len(suffix) - (length + gap) : ]
    
def pairedReads(fileName, solutionName):
    lengthOfReads, gapValue, readsForward, readsBackward = readRegularTextFilePaired(fileName)
    actualSequence = readSolution(solutionName)
        
    forwardMers = getMers(readsForward)
    #print('Forward Mers: ', forwardMers)

    backwardMers = getMers(readsBackward)
    pairedDict = createPairedDict(forwardMers, backwardMers)
    #print('Graph: ', pairedDict)

    start, end = findPath(pairedDict)
    #print('Start Node: ', start)
    #print('End Node: ', end)

    prefix = concatenatePaired(start, end, pairedDict, 'Forward')
    suffix = concatenatePaired(start, end, pairedDict, 'Backward')
    estimatedSequence = assembly(prefix, suffix, lengthOfReads, gapValue)
    if estimatedSequence == actualSequence:
        print ('Succeeded!! \nThe sequence is ', estimatedSequence)
    
    else:
        print ('Failed!! \nThe actual Sequence is ', actualSequence,
               '\nThe estimated Sequence is ', estimatedSequence)

################################################################################################
"""
SINGLE READS
"""
def readRegularTextFileSingle(fileName):
    fileContent = open(fileName).readlines()
    lengthOfReads = int(fileContent[0])
    readsForward = []
    
    for line in fileContent[1:]:
        readsForward.append(line.rstrip())
    return lengthOfReads, readsForward

def createSingleDict(Mers):
    singleDict = {}
    for i in range(0, len(Mers), 2):
        singleDict[Mers[i]] = Mers [i + 1]
    return singleDict

def concatenateSingle(singleDict, start, end):
    path = start
    while(start != end):
        path += singleDict[start][-1]
        start = singleDict[start]
    return path

def singleReads(fileName, solutionName):
    lengthOfReads, reads = readRegularTextFileSingle(fileName)
    actualSequence = readSolution(solutionName)
    
    mers = getMers(reads)
    #print('Mers: ', mers)

    singleDict = createSingleDict(mers)
    #print('Graph: ', singleDict)

    start, end = findPath(singleDict)
    #print('Start Node: ', start)
    #print('End Node: ', end)

    estimatedSequence = concatenateSingle(singleDict, start, end)
    if estimatedSequence == actualSequence:
        print ('Succeeded!! \nThe sequence is ', estimatedSequence)
    
    else:
        print ('Failed!! \nThe actual Sequence is ', actualSequence,
               '\nThe estimated Sequence is ', estimatedSequence)
################################################################################################           
if __name__ == "__main__":
    print("What do you wish to Assemble? \n1)Single Reads \n2)Paired Reads \n3)Exit")
    userAssembleChoice = int(input())
    while(userAssembleChoice != 3):
        while(userAssembleChoice < 1 or userAssembleChoice > 3):
            print("Ivalid Choice")
            print("What do you wish to Assemble? \n1)Single Reads \n2)Paired Reads \n3)Exit")
            userAssembleChoice = int(input())
        
        if userAssembleChoice == 1:
            print("Running Section Test Case...")
            time.sleep(3)
            singleReads("Our testcases/SingleReadsTestCase1.txt", "Our testcases/SingleReadsTestCase1Solution.txt")
            print(" ")
            
            print("Running Text File Test Case...")
            time.sleep(3)
            singleReads("Testcases/singleReadInputProcessed.txt", "Testcases/SingleReadOutputProcessed.txt")
            print(" ")
            
        elif userAssembleChoice == 2:
            print("Running Section Test Case...")
            pairedReads("Our Testcases/PairedReadsTestCase1.txt", "Our Testcases/PairedReadsTestCase1Solution.txt")
            time.sleep(3)
            print(" ")
            
            print("Running Document Test Case...")
            pairedReads("Our Testcases/PairedReadsTestCase2.txt", "Our Testcases/PairedReadsTestCase2Solution.txt")
            time.sleep(3)
            print(" ")
            
            print("Running Text File Test Case...")
            pairedReads("Testcases/ReadPairsInput.txt", "Testcases/ReadPairsOutput.txt")
            time.sleep(3)
            print(" ")
            
        elif userAssembleChoice == 3:
            break
        
        print("What do you wish to Assemble? \n1)Single Reads \n2)Paired Reads \n3)Exit")
        userAssembleChoice = int(input())