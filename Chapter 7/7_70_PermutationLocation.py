def findPermutations(s, b):
    hashTable = {}
    for char in s:
        if char in hashTable.keys():
            hashTable[char] = hashTable[char] + 1
        else:
            hashTable[char] = 1

    slicedString = ""
    printFlag = True
    for index in range(len(b) - 3):
        slicedString = b[index:index + 4]
        for character in hashTable.keys():
            if slicedString.count(character) != hashTable[character]:
                printFlag = False
                break

        if printFlag == True:
            print("Index: " + str(index))
            print("Sliced string: " + slicedString)
        else: printFlag = True

s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"
print(findPermutations(s, b))