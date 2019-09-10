def selection_sort(collection):
    for i in range(len(collection)-1):
        least = i
        for j in range(i+1,len(collection)):
            if collection[j] < collection[least]:
                least = j
        collection[i], collection[least] = collection[least], collection[i]
    return collection

col = [22,99,88,33,77,55,44,11,66]

a = selection_sort(col)
print(a)
