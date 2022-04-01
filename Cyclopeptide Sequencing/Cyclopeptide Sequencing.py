

#### Start Of Functions ####
''''
    This Function works on taking the theoreticalSpectrum as an input
    and returns the initial list of 1-mers by defining an empty list to
    append the 1-mers to it by taking each mass in the theoretical Spectrum
    and depending on the fact that the maximimum weight of a single aminoacid
    is 186 and that the theoreticalSpectrum is sorted, as long as the mass is
    still below or equal to 186 we check on it if it is equal to any of the keys
    in weights dictionary this means it corresponds to a single aminoacid and
    that this aminoacid is one of our 1-mers so we append it to our list.
    Once we reach a mass value higher than 186 we then are sure no more
    1-mers exist so we return the list.
'''
def Initial_List(theoreticalSpectrum):
    initialAminoAcids=[]
    for mass in theoreticalSpectrum:
        if mass>186:
            return initialAminoAcids
        if mass in weights:
            initialAminoAcids.append(weights[mass])

'''
    This function is take a subpeptide which could be of any length and get its
    totalValue weight by examining each aminoacid in the subpeptide and
    getting its weight from the weights dictionary. And since weights dictionary
    holds the aminoacid as value not key we worked on looping by weights.items()
    to get both keys and values and if the value matches the current
    aminoacid we are examining the key which is the weight is added to the
    totalValue weight and at the end the totalValue weight is returned.
'''
def getWeight(subpeptide):
    totalValue=0
    for aminoacid in subpeptide:
        for key,value in weights.items():
            if value == aminoacid:
                totalValue+=key
    return totalValue

'''
    This function works on taking the peptideSequence and cuts it into pieces
    to get their weight. It gets the first aminoacid then get its weight and
    add it to linearSpectrumValues list, then takes the first aminoacid and the
    second aminoacid and get their total weight together and so on.
    At the end we will be return linearSpectrumValues list that holds the
    weights of every possible subPeptide that can be formed from the
    peptideSequence given as input.
'''
def Linear_Spectrum(peptideSequence):
    linearSpectrumValues = []
    for i in range(len(peptideSequence)+1):
        value = 0
        for j in range(i,len(peptideSequence),1):
            currentSubpeptide = peptideSequence[i:j+1]
            linearSpectrumValues.append(getWeight(currentSubpeptide))
    return linearSpectrumValues

'''
    This is just a helper function to help us fulfill our logic, it works
    on getting a list as an input and converting this list to a
    dictionary where the dictionary keys are the values of the list and
    the dictionary values are the count of how many the keys appeared in the
    list. Then we return this dictionary to use it later.
'''
def getCount(listOfValues):
    dictionaryToReturn = {}
    for value in listOfValues:
        dictionaryToReturn[value]=listOfValues.count(value)
    return dictionaryToReturn

'''
    This is a helper function which works on taking the available list of
    subpeptides and adds on each of them an extra aminoAcid from the
    initialAminoAcids we have. And then return a list with the newly
    extended subPeptides.
'''
def extendSubPeptide(listToBeExtended,initialAminoAcids):
    newExtensions = []
    countOfEachInitialAminoAcid = getCount(initialAminoAcids)
    for subPeptide in listToBeExtended:
        for aminoAcid in initialAminoAcids:
            currentExtension = subPeptide + aminoAcid

            '''
                Since we have the initialAminoAcids which forms the peptide
                we are searching for and by so we also know the count each of
                those initialAminoAcid should appear with we added this if to
                ensure that the new extension we are trying to form will contain
                the same count of each aminoAcid as what it should. For example
                V in initialAminoAcid appears once this means if the current
                extension was VV it shouldn't be added to our new extensions list
                and that is what happens.
            '''
            if currentExtension.count(aminoAcid) > countOfEachInitialAminoAcid[aminoAcid]:
                continue

            '''
                This if is to ensure no extensions are repeated since that if
                we have P and P in the initialAminoAcids List in every extension
                its extension results will appear twice so we prevent that
                as they will lead to the same results in the end so no need for
                duplication.
            '''
            if currentExtension in newExtensions:
                continue
            else:
                newExtensions.append(currentExtension)
            
    return newExtensions   

'''
    This function is to check whether the subPeptideSequence it recieves
    could be the peptide that resulted in the given theoreticalSpectrum or not
    and this is by calling Linear_Spectrum function and giving it the
    subPeptideSequence to get back its linearSpectrumValues where we will loop
    on each value and check whether it appeared in the theoreticalSpectrum or
    not if yes we will continue checking the other values, if not then false is
    returned saying it this subPeptideSequence is not consistent.
'''
def IsConsistent(subPeptideSequence,theoreticalSpectrum):
    linearSpectrumValues = Linear_Spectrum(subPeptideSequence)
    '''
       countOfLinearSpectrumValues now holds the count of each
       value in the theoreticalSpectrum.
    '''
    countOfLinearSpectrumValues = getCount(theoreticalSpectrum)
    for value in linearSpectrumValues:
        '''
            This if is to check the value exists in the theoreticalSpectrum
            and if yes we then check that the count the value appeared with
            in the current subPeptideSequence is the same as the count the
            value appeared with in the theoreticalSpectrum. As for example
            in PVTP 297 value will appear 2 times although in the
            theoretical Spectrum it appears once and by so this makes
            inconsistent. 
        '''
        if value in theoreticalSpectrum and not countOfLinearSpectrumValues[value] == 0:
            countOfLinearSpectrumValues[value] = countOfLinearSpectrumValues[value] - 1
            continue
        else:
            return False
        
    return True


'''
    This function is considered the main function of cyclopeptide sequencing,
    it takes as an input Theoretical Spectrum and 
    its output is All the linear representations of the 
    cyclic sequence of the protein (Peptide Sequence).
'''
def cyclopeptideSequencing(theoreticalSpectrum):
    
    Initial_L = Initial_List(theoreticalSpectrum)
    lengthOfPeptide = len(Initial_L)
    
    print("---------------------------------")
    print("Initial 1-mers: ", Initial_L, "\nLength of Peptide = ", lengthOfPeptide)
    
    
    # TempList: the list that will be extended
    TempList = Initial_L
    currentLengthOfPeptide=1
    ConsistentList = []
    while True:
        
        TempList = extendSubPeptide(TempList,Initial_L)
        if not len(TempList)==0:
            currentLengthOfPeptide=len(TempList[0])

        inConsistenSubPeptides = []
        
        for subPeptide in TempList:
            consistency = IsConsistent(subPeptide,theoreticalSpectrum)
            if consistency is False :
                inConsistenSubPeptides.append(subPeptide)     
        
        for subPeptide in inConsistenSubPeptides:
            TempList.remove(subPeptide)

        
        if len(TempList) == 0:
            print("The generated potential sub-peptides are all inconsistent!")
            break
        
        print("---------------------------------")
        print(currentLengthOfPeptide, "sub-mers: ", TempList)
        print("Length of", currentLengthOfPeptide, "sub-mers = ", len(TempList))
        

        if currentLengthOfPeptide==lengthOfPeptide:
            break
        
    return TempList

#### End Of Functions ####



'''
    This part of code is to read the weights of the aminoacids from a file named "weight"
    of type txt file where each line in the file contains the aminoacid(uppercase):weight
    and store them in a weights dictionary to be used later.
    We were using it while trying to test the code but since the form accepts only one
    .py file we initialized the weights dictionary manually.
'''
'''
weightsFile=open("weight.txt")
weights={}
for weight in weightsFile:
    line=(weight.strip()).split(":")
    weights[int(line[1])]=line[0]
'''

weights={156:'R',114:'N',115:'D',103:'C',129:'E',128:'Q',57:'G',137:'H',113:'L',
         131:'M',147:'F',97:'P',87:'S',101:'T',186:'W',163:'Y',99:'V',71:'A'}

'''
    This part is only to handle taking the theoreticalSpectrum by anyway the
    user wants either by reading a file or by taking it from the user.
    We also added an option of initializing the theoreticalSpectrum manually
    by the numbers in the assignment since we couldn't submit multiple files
    in the form.
'''
theoreticalSpectrum = []
while 1:
    wayOfInput = int(input("Press '1' to work on the spectrum of the Assignment\nPress '2' to read the spectrum from a file\nPress '3' to read the spectrum from the console\n"))
    
    if wayOfInput == 1:
        theoreticalSpectrum=[0,97,97,99,101,103,196,198,198,200,
                             202,295,297,299,299,301,394,396,398,
                             400,400,497]
        break
    
    elif wayOfInput == 2:
        print("--------------------------------------------------")
        print("| Each Spectrum Value must be in a single line!! |")
        print("--------------------------------------------------")
        fileToRead=input("Please enter the file name with .txt at the end of the name 'example: TheoreticalSpectrum.txt' :")
        theoreticalSpectrumFile = open(fileToRead)
        
        # This loop is to convert the file to integers to work with them easily
        for line in theoreticalSpectrumFile:
            line = line.strip()
            theoreticalSpectrum.append(int(line))
        break
        

    elif wayOfInput == 3:
        numberOftheoreticalSpectrum = int(input("Enter how many spectrums you will add: "))
        for i in range(numberOftheoreticalSpectrum):
            theoreticalSpectrum.append(int(input("Enter your spectrum value " +str(i+1)+" : ")))
        break
    else:
        print("Invalid Choice!")
        
        
print("____________________________________________")
print("\nCyclopeptide Sequencing\n")


# This is to ensure the theoriticalSpectrum values are sorted
theoreticalSpectrum.sort()
print("---------------------------------")
print("Theoretical Spectrum [Sorted]:", theoreticalSpectrum)


# The Main Function of Cyclopeptide Sequencing
allLinearRepresentationsOfCyclicSeq = cyclopeptideSequencing(theoreticalSpectrum)


# Printing the final list that contains all linear representations of the antibiotic.
print("____________________________________________\n")
print("Final Representations of the antibiotic are:\n", allLinearRepresentationsOfCyclicSeq)
print("Length of Final Representations of the antibiotic = ", len(allLinearRepresentationsOfCyclicSeq))
print("____________________________________________\n")
