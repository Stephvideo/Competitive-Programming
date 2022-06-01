# https://codeforces.com/problemset/problem/1659/A


import math


T = int(input())

for t in range(T):
    s, r, b = [float(x) for x in input().split()]

    currString = ""
    consecutiveReds = math.ceil(r/(b+1))
    placeBlue = 0
    for i in range(0, s):
        if placeBlue == consecutiveReds:
            currString += "B"
            placeBlue = 0
        else:
            currString += "R"
            placeBlue += 1
    print (currString)

