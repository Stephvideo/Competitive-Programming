# https://codeforces.com/problemset/problem/1374/C

T = int(input())

for t in range(T):

    n = int(input())

    numLeft = 0
    ans = 0

    s = input()

    for i in range(len(s)):
        if s[i] == '(':
            numLeft += 1
        else:
            if numLeft == 0:
                ans += 1
            else:
                numLeft -=1
    print(ans)