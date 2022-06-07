# https://codeforces.com/contest/1690/problem/B
inf = 10000000000
for t in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    minDiff = inf
    flag = False
    for i in range(len(a)):
        if a[i] < b[i]:
            flag = True
            break
        
        if b[i] != 0:
            diff = a[i] - b[i]
            if diff < minDiff:
                minDiff = diff
    
    for i in range(n):
        if a[i] - b[i] > minDiff:
            flag = True
            break

    if flag: 
        print("NO")
    else:
        print("YES")