# 1 2 3 4 7 10 6 5
# O(logn)

def findCorrelate(a, l, r):
    print(l, r)
    if l == r:
        if a[l] == l:
            return l
        return None
    else:
        mid = (r + l) // 2
        if a[mid] >= mid:
            return findCorrelate(a, l, mid)
        else:
            return findCorrelate(a, mid + 1, r)

def main():
    a = [-1, 1, 2, 5, 8, 10]
    print(findCorrelate(a, 0, len(a) - 1))

if __name__ == '__main__':
    main()
