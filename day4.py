test1 = 'aa bb cc dd ee'
test2 = 'aa bb cc dd aa'
test3 = 'aa bb cc dd aaa'
test4 = 'aa bb cc dd aaa cc'

test5 = 'abcde fghij'
test6 = 'abcde xyz ecdab'
test7 = 'a ab abc abd abf abj'
test8 = 'iiii oiii ooii oooi oooo'
test9 = 'oiii ioii iioi iiio'

# Converts the string into a list of sorted words. This puts duplicate entries
# next to each other, so just compare adjacent entries
def passphraseCheck(phrase):
    words = phrase.strip('\n')
    words = words.split(' ')

    # Sort letters in a word into order in order to find anagrams
    words = list(map(sortWord, words))
    
    words = sorted(words)

    for i, word in enumerate(words):
        if i+1 < len(words):
            if word == words[i+1]:
                return False

    return True

# Sorts all the letters in a given word into alphabetical order
def sortWord(word):
    letters = list(word)
    letters = sorted(letters)
    sortedWord = ''.join(letters)

    return sortedWord


def processFile():
    puzzleInput = open('day4input.txt', 'r')
    validPhrases = 0

    for line in puzzleInput:
        if passphraseCheck(line):
            validPhrases += 1
                
    print("Valid phrases: {0}".format(validPhrases))

if __name__ == '__main__':
    processFile()

    #print(passphraseCheck(test1))
    #print(passphraseCheck(test2))
    #print(passphraseCheck(test3))
    #print(passphraseCheck(test4))

    #print(passphraseCheck2(test6))
