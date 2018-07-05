import math

def multiply(x, y):
    n = max(len(str(x)), len(str(y)))
    if n > 1:
        n2 = n // 2
        
        half = 10 ** n2

        a = x // half
        b = x % half
        c = y // half
        d = y % half

        m1 = multiply(a, c)
        m2 = multiply(b, d)
        m3 = multiply(a + b, c + d)
        s = m3 - m2 - m1
        return (m1 * 10 ** (2 * n2))  + (s * 10 ** n2) + m2
    else:
        return x * y

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(multiply(num1, num2))

if __name__ == '__main__':
    main()