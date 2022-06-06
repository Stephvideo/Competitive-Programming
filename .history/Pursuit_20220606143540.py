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

    low = 0
    high = 10 ** 5
    curr = 5
    while low >= high:
        mid = (low + high) //2

        k = (n + mid) - (n + mid)//4
        myPoints = ([100] * mid) + myPoints
        ilyaPoints = ilyaPoints + ([0] * mid)

        myCurrPoints = sum(myPoints[0:k])
        ilyaCurrPoints = sum(ilyaPoints[0:k])

        if myCurrPoints < ilyaCurrPoints:
            low = mid + 1
            
        else:
            high = mid - 1
            curr = mid

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




