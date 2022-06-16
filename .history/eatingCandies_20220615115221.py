# https://codeforces.com/problemset/problem/1669/F

for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    front = 0
    back = n-1

    frontSum = lst[0]
    backSum = lst[-1]
    ans = 0
    while front < back:
        if frontSum == backSum:
            ans = front+1 + (n-back)
            front += 1
            back -= 1
            frontSum += lst[front]
            backSum += lst[back]
        elif frontSum < backSum:
            front += 1
            frontSum += lst[front]
        else:
            back -= 1
            backSum += lst[back]
    print(ans)