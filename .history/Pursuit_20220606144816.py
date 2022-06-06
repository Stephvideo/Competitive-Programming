# https://codeforces.com/problemset/problem/1530/C

for t in range(int(input())):

    n = int(input())
    myPoints = list(map(int, input().split()))
    ilyaPoints = list(map(int, input().split()))

    k = n - (n//4)

    myPoints = sorted(myPoints)
    myPoints.reverse()

    ilyaPoints = sorted(ilyaPoints)
    ilyaPoints.reverse()
    #print (myPoints)

    ans = 0
    myCurrPoints = sum(myPoints[0:k])
    ilyaCurrPoints = sum(ilyaPoints[0:k])
    if myCurrPoints >= ilyaCurrPoints:
        print(0)
        continue

    low = 1
    high = n + 1
    curr = high

    while high >= low:
        mid = (low + high) //2
        #print("mid: ", mid)
        k = (n + mid) - ((n + mid)//4)
        myNewPoints = ([100] * mid) + myPoints
        ilyaNewPoints = ilyaPoints + ([0] * mid)
        #print (myPoints)
        myCurrPoints = sum(myNewPoints[0:k])
        ilyaCurrPoints = sum(ilyaNewPoints[0:k])

        if myCurrPoints >= ilyaCurrPoints:
            curr = mid
            high = mid - 1
        else:
            low = mid + 1

    print (curr)

    # while myCurrPoints < ilyaCurrPoints:
    #     ans += 1
    #     n += 1
    #     k = n - (n//4)
    #     myPoints = [100] + myPoints
    #     ilyaPoints = ilyaPoints + [0]

    #     myCurrPoints = sum(myPoints[0:k])
    #     ilyaCurrPoints = sum(ilyaPoints[0:k])

    # print (ans)




