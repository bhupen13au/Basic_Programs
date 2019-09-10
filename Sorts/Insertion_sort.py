def insertion_sort(collection):
    for i in range(len(collection)-1):
        j = i
        while j>0 and collection[j-1] > collection[j]:
            collection[j], collection[j-1] = collection[j-1], collection[j]
            j -= 1

col = [60,30,10,20,90,40,50,20,70,80]
insertion_sort(col)
print(col)
