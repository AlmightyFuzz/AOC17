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
    programData = processTestInput(test1)
    #programData = processPuzzleInput()

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

def balanceTowers(programMap):

    for prog in programMap:
        if prog.stoodOn == None:
            baseProg = prog
            print('Base: ', baseProg.name)

    calculateWeights(baseProg)

    for i in programMap:
        print(i.name, i.totalWeight)

    #traverse(baseProg)

def traverse(prog):

    if prog.holdingUp == []:
        print(prog.name, prog.weight)
    else:
        w = prog.holdingUp[0].weight
        for p in prog.holdingUp:
            if p.weight != w:
                print('Weight mismatch')
        for p in prog.holdingUp:
            traverse(p)

def calculateWeights(program):

    if program.holdingUp == []:
        return program.weight
    else:
        cw = 0
        for prog in program.holdingUp:
            cw += calculateWeights(prog)
                
        program.carriedWeight = cw

        return program.totalWeight
    
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

def processTestInput(inData):
    inData = inData.strip('\n')
    inData = inData.split('\n')
    
    return inData

def processPuzzleInput():
    file = open('day7input.txt','r')

    fileData = [line.strip('\n') for line in file]

    return fileData
    
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
