def ikjMatrixProduct(x, y):
    n = len(x)
    z = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                z[i][j] += x[i][k] * y[k][j]
    return z

def substract(x, y):
    n = len(x)
    z = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            z[i][j] = x[i][j] - y[i][j]
    return z

def add(x, y):
    n = len(x)
    z = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            z[i][j] = x[i][j] + y[i][j]
    return z

def strassen(x, y):
    if len(x) <= 1: 
        return ikjMatrixProduct(x, y)
    else:
        n = len(x)
        mid = n // 2
        a = [[0 for j in range(mid)] for i in range(mid)]
        b = [[0 for j in range(mid)] for i in range(mid)]
        c = [[0 for j in range(mid)] for i in range(mid)]
        d = [[0 for j in range(mid)] for i in range(mid)]
        e = [[0 for j in range(mid)] for i in range(mid)]
        f = [[0 for j in range(mid)] for i in range(mid)]
        g = [[0 for j in range(mid)] for i in range(mid)]
        h = [[0 for j in range(mid)] for i in range(mid)]

        for i in range(mid):
            for j in range(mid):
                a[i][j] = x[i][j]
                b[i][j] = x[i][j + mid]
                c[i][j] = x[i + mid][j]
                d[i][j] = x[i + mid][j + mid]

                e[i][j] = y[i][j]
                f[i][j] = y[i][j + mid]
                g[i][j] = y[i + mid][j]
                h[i][j] = y[i + mid][j + mid]

        p1 = strassen(a, substract(f, h))
        p2 = strassen(add(a, b), h)
        p3 = strassen(add(c, d), e)
        p4 = strassen(d, substract(g, e))
        p5 = strassen(add(a, d), add(e, h))
        p6 = strassen(substract(b, d), add(g, h))
        p7 = strassen(substract(a, c), add(e, f))

        z00 = add(p5, p4)
        z00 = substract(z00, p2)
        z00 = add(z00, p6)

        z01 = add(p1, p2)

        z10 = add(p3, p4)

        z11 = add(p1, p5)
        z11 = substract(z11, p3)
        z11 = substract(z11, p7)

        z = [[0 for j in range(n)] for i in range(n)]
        for i in range(mid):
            for j in range(mid):
                z[i][j] = z00[i][j]
                z[i][j + mid] = z01[i][j]
                z[i + mid][j] = z10[i][j]
                z[i + mid][j + mid] = z11[i][j]
        return z


def main():
    with open('week-2/strassen-matrix-multiplication.in') as f:
        lines = f.readlines()
    mid = len(lines) // 2
    x = [[int(x) for x in line.rstrip('\n').split(' ')] for line in lines[:mid]]
    y = [[int(x) for x in line.rstrip('\n').split(' ')] for line in lines[mid:]]
    z = strassen(x, y)
    print(z)

if __name__ == "__main__":
    main()