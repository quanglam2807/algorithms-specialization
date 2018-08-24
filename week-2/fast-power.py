def fastPower(a, b):
    if b == 1:
        return a
    else:
        c = a * a
        ans = fastPower(c, b // 2)
    if b % 2 == 0:
        return ans
    else:
        return ans * a

def main():
    a = 5
    b = 10
    print(fastPower(5, 10))

if __name__ == '__main__':
    main()
