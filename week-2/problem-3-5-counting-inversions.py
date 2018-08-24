import random

def sortAndCountInv(lst):
    if len(lst) == 1:
        return lst, 0
    
    mid = len(lst) // 2
    a, leftInv = sortAndCountInv(lst[:mid])
    b, rightInv = sortAndCountInv(lst[mid:])
    c = [None] * len(lst)

    i = 0
    j = 0
    k = 0
    splitInv = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1
            splitInv += len(a) - i
    
    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1
        splitInv += len(a) - i

    return c, leftInv + rightInv + splitInv

def main():
    lst = [1, 3, 5, 2, 4, 6]
    print(lst)
    sortedLst, inv = sortAndCountInv(lst)
    print(sortedLst)
    print(inv)

if __name__ == '__main__':
    main()