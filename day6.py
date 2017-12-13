test1 = [0,2,7,0]
puzzleInput = [4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]

def infinLoopSpotter(memoryBanks):
    cycles = 0
    previousConfigs = []
    previousConfigs.append(list(memoryBanks)) #list(listA) creates a shallow copy

    firstRepeatedConfig = []
    loopSize = 0

    while True:

        #find largest value in list
        largest = max(memoryBanks)
        largeIdx = memoryBanks.index(largest)
        memoryBanks[largeIdx] = 0

        #Distribute the blocks amongst the banks
        idx = largeIdx
        for i in range(largest):
            idx += 1
            if idx >= len(memoryBanks):
                idx = 0

            memoryBanks[idx] += 1        

        if firstRepeatedConfig == []:
            #if we haven't found a repeating configuration
            cycles += 1
            
            #Check if current configuration of memory blocks has been seen before
            if memoryBanks in previousConfigs:
                firstRepeatedConfig = list(memoryBanks)
                #break
            else:
                previousConfigs.append(list(memoryBanks))
        else:
            #If we have found a repeated config, keep looking until we find it again
            #to find the size of the repeating loops
            loopSize += 1
            
            if memoryBanks == firstRepeatedConfig:
                break

    
    return cycles,loopSize

if __name__ == '__main__':
    #print(infinLoopSpotter(test1))
    print(infinLoopSpotter(puzzleInput))
