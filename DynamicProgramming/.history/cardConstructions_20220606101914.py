pyramidCost = {}
pyramidCost[1] = 2 

def makePyramid(height):
    if height in pyramidCost:
        return pyramidCost[height]

    else:
        pyramidCost[height] = makePyramid(height-1) + (height - 1) + height * pyramidCost[1]
        return pyramidCost[height]




for t in range(int(input())):

    numCards = int(input())

    ans = 0
    while numCards > 0:
        if numCards < 2:
            break

        i = 1
        currHeight = 0
        cost = 0
        while True:
            cost = makePyramid(i)
            if cost <= numCards:
                currHeight += 1
                i += 1
            else:
                break

        numCards -= pyramidCost[currHeight]
        ans += 1
    
    print(ans)