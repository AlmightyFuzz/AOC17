import re

test1 = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""

def buildProgramMap():
    #programData = loadTestInput(test1)
    programData = loadPuzzleInput()

    programList = processData(programData)

    #find all the programs that are holding up other programs
    supportingProgs = [prog for prog in programList if prog.holdingUp != []]
    
    #foreach program that is holding up another,
    for sProg in supportingProgs:
        #get the names of those other programs,
        for i,supportedProgName in enumerate(sProg.holdingUp):
            #find the relevant program in the programList,
            for mainProg in programList:
                #then link those programs together
                if supportedProgName == mainProg.name:
                    mainProg.stoodOn = sProg
                    sProg.holdingUp[i] = mainProg

    return programList

#Finds the programs whose weights don't balance
def balanceTowers(programMap):

    for prog in programMap:
        if prog.stoodOn == None:
            baseProg = prog
            print('Base: ', baseProg.name)

    calculateWeights(baseProg)

    unbalancedProgs = []

    for p in programMap:
        if p.holdingUp != []:
            weight = p.holdingUp[0].totalWeight
            
            for i in p.holdingUp:
                if i.totalWeight != weight:
                    unbalancedProgs.append(p)
                    break

    for p in unbalancedProgs:
        for i in p.holdingUp:
            print(p.name+'\t', i.name, ':'+str(i.totalWeight)+':', str(i.weight), str(i.carriedWeight))

        print()

    #You'll have to work out the answer from here on yourself by looking at the output
        
#Runs through the linked programs and calculates all their weights
def calculateWeights(program):

    if program.holdingUp == []:
        return program.weight
    else:
        cw = 0
        for prog in program.holdingUp:
            cw += calculateWeights(prog)
                
        program.carriedWeight = cw

        return program.totalWeight

#Reads in the data and creates the program objects from that
def processData(programData):
    programList = []

    regex = r'(?P<name>[a-z]+)\s\((?P<weight>\d+)\)( -> (?P<progList>.*))?'

    for item in programData:
        match = re.match(regex,item)
        if not match:
            print('No Match found')
            continue

        prog = Program(match.group('name'))
        prog.weight = int(match.group('weight'))
        if match.group('progList'):
            progList = match.group('progList')
            progList = progList.replace(' ', '')
            progList = progList.split(',')
            
            prog.holdingUp = list(progList)

        programList.append(prog)
    
    return programList

def loadTestInput(inData):
    inData = inData.strip('\n')
    inData = inData.split('\n')
    
    return inData

def loadPuzzleInput():
    file = open('day7input.txt','r')

    fileData = [line.strip('\n') for line in file]

    return fileData

#Program Class definition
class Program():
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.carriedWeight = 0
        self.stoodOn = None #The program that this one is stood on
        self.holdingUp = [] #The list of programs that this one is holding up

    @property
    def totalWeight(self):
        return self.weight + self.carriedWeight

    def __str__(self):
        return self.name



if __name__ == '__main__':
    programMap = buildProgramMap()

    balanceTowers(programMap)
