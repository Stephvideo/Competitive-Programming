# https://codeforces.com/problemset/problem/1566/C

for t in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    ans = 0
    stretch = False
    i = 0
    while i < n:
        if a[i] != b[i]:
            stretch = False
            ans += 2
        
        elif a[i] == '0' and b[i] == '0':
            ans += 1
            if stretch:
                stretch = False
                ans += 1
            elif i < n-1 and a[i+1] == '1' and b[i+1] == '1':
                stretch = False
                ans +=1
                i += 1
        else:
            stretch = True

    print (ans)