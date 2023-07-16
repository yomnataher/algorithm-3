import math
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

def bruteForce(P, n):
    minVal = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < minVal:
                minVal = dist(P[i], P[j])
    return minVal

def stripClosest(strip, size, d):
    minVal = d
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < minVal:
            minVal = dist(strip[i], strip[j])
            j += 1
    return minVal

def closestUtil(P, Q, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n // 2
    midPoint = P[mid]
    Pl = P[:mid]
    Pr = P[mid:]
    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid)
    d = min(dl, dr)
    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])

    stripP.sort(key=lambda point: point.y)
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripQ, len(stripQ), d))
    return min(min_a, min_b)


def closest(P, n):
    P.sort(key=lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)
    return closestUtil(P, Q, n)


# main
n = int(input())
Pt = []
for i in range(n):
    A = list(map(int, input().strip().split()))[:2]
    Pt.append(Point(A[0], A[1]))

print(closest(Pt, n))
