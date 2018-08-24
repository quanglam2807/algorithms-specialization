import random

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    a = mergeSort(lst[:mid])
    b = mergeSort(lst[mid:])
    c = [None] * len(lst)

    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1
    
    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1

    return c 

def main():
    lst = random.sample(range(0, 1000), 100)
    print(lst)
    sortedLst = mergeSort(lst)
    print(sortedLst)

if __name__ == '__main__':
    main()