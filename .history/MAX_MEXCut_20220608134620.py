# https://codeforces.com/problemset/problem/1566/C

for t in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    ans = 0
    stretch = False
    for i in range(len(a)):
        if a[i] != b[i]:
            stretch = False
            ans += 2
        
        elif a[i] == '0' and b[i] == '0':
            stretch = False
            ans += 1
        
        else:
            continue
    print (ans)