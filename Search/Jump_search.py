from math import *

def jump_search(collection,find):
    m = floor(sqrt(len(collection)))

    for i in range(0,len(collection)-1,m):
        if collection[i] == find:
            return 'Found at {}'.format(i)

        elif collection[i] > find:
            for j in range(1,m):
                if collection[i-j] == find:
                    return 'Found at {}'.format(i-j)

    return 'Not found'


col = [1,2,2,33,36,44,47,49,55,59,77,78,79,80,88,89,99,100]

a = jump_search(col,77)
print(a)
