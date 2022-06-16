# https://codeforces.com/problemset/problem/1669/F

for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    front = 0
    back = n-1

    frontSum = 0
    backSum = 0
    ans = 0
    while front <= back:
        frontSum += lst[front]
        backSum += lst[back]

        if frontSum == backSum:
            ans = front+1
            front += 1
            back -= 1
        elif frontSum < backSum:
            front += 1
        else:
            back -= 1

    print(ans)