# 1 2 3 4 7 10 6 5
# O(logn)

def findMax(a, l, r):
    if l == r:
        return a[r]
    else:
        mid = (r + l) // 2
        if a[mid] < a[mid + 1]:
            return findMax(a, mid + 1, r)
        else:
            return findMax(a, l, mid)

def main():
    a = [1, 2, 3, 4, 7, 10, 6, 5]
    print(findMax(a, 0, len(a) - 1))

if __name__ == '__main__':
    main()
