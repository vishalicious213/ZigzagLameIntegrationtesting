def checkBlanagrams(word1, word2):
# big plan: check if all letters are the same except for one
    if len(word1) < 1 or len(word2) < 1:
        return False
        
    list1 = list(word1)
    list2 = list(word2)
    
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                print('match', i, list1[i], j, list2[j])
                del list2[j]
                print('in loop', len(list2), list2)
                break
            else:
                break
                print('miss', i, list1[i], j, list2[j])

    print('outside', len(list2), list2)
    if len(list2) == 1:
        return True
    return False