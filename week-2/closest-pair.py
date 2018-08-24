import math

def dist(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def closestSplitPair(px, py, delta):
    len_px = len(px)
    midpoint = px[len_px // 2]

    print(py)
    sy = [p for p in py if midpoint[0] - delta <= p[0] <= midpoint[1] + delta]

    best = delta
    bestPair = (None, None)
    l = len(sy)
    for i in range(l):
        for j in range(i + 1, min(i + 7, l)):
            d = dist(sy[i], sy[j])
            if d < best:
                best = d
                bestPair = (sy[i], sy[j])
    return bestPair[0], bestPair[1], best


def closestPair(px, py):
    len_px = len(px)
    if len_px <= 3:
        return brute(px)
    mid = len_px // 2
    lx = px[:mid]
    rx = px[mid:]

    ly = list()
    ry = list()
    midp = px[mid][0]
    for p in py:
        if p[0] <= midp:
            ly.append(p)
        else:
            ry.append(p)

    l1, l2, dl = closestPair(lx, ly)
    r1, r2, dr = closestPair(rx, ry)

    if dl < dr:
        dm = dl
        p1 = l1
        p2 = l2
    else:
        dm = dr
        p1 = r1
        p2 = r2

    s1, s2, ds = closestSplitPair(px, py, dm)

    if ds < dm:
        return s1, s2, ds
    else:
        return p1, p2, dm

def brute(px):
    len_px = len(px)
    min = float('inf')
    p1 = None
    p2 = None
    for i in range(len_px - 1):
        for j in range(i + 1, len_px):
            d = dist(px[i], px[j])
            if d < min:
                min = d
                p1 = px[i]
                p2 = px[j]
    return p1, p2, min

def main():
    # line 1 is x
    # line 2 is y
    with open('week-2/closest-pair.in') as f:
        lines = f.readlines()
    x = [int(x) for x in lines[0].rstrip('\n').split(' ')]
    y = [int(x) for x in lines[1].rstrip('\n').split(' ')]

    # https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2
    p = list(zip(x, y))  # This produces list of tuples
    px = sorted(p, key=lambda x: x[0])  # Presorting x-wise
    py = sorted(p, key=lambda x: x[1])  # Presorting y-wise
    bestX, bestY, bestDistance = closestPair(px, py)
    print(bestX, bestY, bestDistance)


if __name__ == '__main__':
    main()
