#v https://codeforces.com/contest/1690/problem/D

inf = 1000000000
for t in range(int(input())):   
    n, k = map(int, input().split())
    s = input()

    numB = 0
    for i in range(k):
        if s[i] == 'B':
            numB += 1
    best = k - numB

    for i in range(k, n):
        if s[i] == 'B':
            numB += 1
        if s[i-k] == 'B':
            numB -= 1

        best = min(best, k - numB)
    
    print (best)

