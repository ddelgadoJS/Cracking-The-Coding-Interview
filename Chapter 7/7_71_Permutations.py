def recursivePermutation(inputString, permutationsList):
    if len(inputString) <= 1:
        return [inputString]

    else:
        tempPermutationsList = []
        permutationsList = recursivePermutation(inputString[:-1], permutationsList)
        for permutation in permutationsList:
        	for index in range(len(permutation) + 1):
        		tempPermutationsList.append(permutation[:index] + inputString[-1] + permutation[index:])
        
        permutationsList = tempPermutationsList[:]

        return permutationsList

inputString = "abc"
print(recursivePermutation(inputString, []))