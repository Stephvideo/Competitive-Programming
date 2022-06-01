# https://codeforces.com/problemset/problem/1659/A


def getRedConsec(s):
    max = 0
    current = 0
    for char in s:
        if char == 'R':
            current += 1
        else:
            if current > max:
                max = current
            current = 0
    
    if current > max:
        max = current
    return max


T = int(input())

for t in range(T):
    s, r, b = [int(x) for x in input().split()]

    currString = ""
    
    for consecutiveReds in range (1, s):
        numRed = r
        numBlue = b
        placeBlue = 0
        
        for i in range(0, s):
            if numRed == 0:
                currString += "B"
                numBlue -= 1
                continue
            if numBlue == 0:
                currString += "R"
                numRed -= 1
                continue

            if placeBlue == consecutiveReds:
                currString += "B"
                placeBlue = 0
                numBlue -= 1
            else:
                currString += "R"
                placeBlue += 1
                numRed -= 1

        if getRedConsec(currString) <= consecutiveReds:
            print (currString)
            break
        else:
            currString = ""
        

