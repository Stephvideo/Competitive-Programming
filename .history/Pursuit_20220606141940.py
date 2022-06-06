# https://codeforces.com/problemset/problem/1530/C

for t in range(int(input())):

    n = int(input())
    myPoints = list(map(int, input().split()))
    ilyaPoints = list(map(int, input().split()))

    k = n + (n//4)

    myPoints = sorted(myPoints).reverse()
    ilyaPoints = sorted(ilyaPoints).reverse()
    print (myPoints)

    ans = 0
    myCurrPoints = sum(myPoints[0:k])
    ilyaCurrPoints = sum(ilyaPoints[0:k])

    while myCurrPoints < ilyaCurrPoints:
        ans += 1
        n += 1
        k = n + (n//4)
        myPoints = [100] + myPoints
        ilyaPoints = ilyaPoints + [0]

        myCurrPoints = sum(myPoints[0:k])
        ilyaCurrPoints = sum(ilyaPoints[0:k])

    print (ans)




