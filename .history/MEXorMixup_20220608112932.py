# https://codeforces.com/problemset/problem/1567/B



for t in range(int(input())):
    a, b = map(int, input().split())
    ans = a

    currXor = a-1

    rem = currXor % 4

    if rem == 1:
        currXor = 1
    elif rem == 2:
        currXor +=1
    elif rem == 3:
        curXor = 0


    candidate = currXor ^ b
    
    if b > currXor:
        ans += 1
        if candidate == a:
            ans += 1
    elif b < currXor:
        ans += 1
        if candidate == a:
            ans += 1   
    print(ans)