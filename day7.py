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
    #programData = processInputFile()

    programList = processData(programData)

    supportingProgs = []

    #find all the programs that are holding up other programs
    for prog in programList:
        if prog.holdingUp != []:
            supportingProgs.append(prog)
    
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

    for prog in programList:
        if prog.stoodOn == None:
            print('Base: ',prog.name)

def processData(programData):
    programList = []

    regex = r'(?P<name>[a-z]+)\s\((?P<weight>\d+)\)( -> (?P<progList>.*))?'

    for item in programData:
        match = re.match(regex,item)
        if not match:
            print('No Match found')
            continue

        prog = Program(match.group('name'))
        prog.weight = match.group('weight')
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

def processInputFile():
    file = open('day7input.txt','r')

    fileData = []
    for line in file:
        line = line.strip('\n')
        fileData.append(line)

    return fileData
    
class Program():
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.stoodOn = None #Name of program that this one is stood on
        self.holdingUp = [] #Names of the programs that this one is holding up

    def __str__(self):
        return self.name
    
if __name__ == '__main__':
    buildProgramMap()
