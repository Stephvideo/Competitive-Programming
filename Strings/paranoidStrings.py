# 
for t in range(int(input())):
    n = int(input())

    s= input()

    ans = len(s)

    for i in range(n-1, 0, -1):
        curr = s[i]
        prev = s[i - 1]

        if curr != prev:
            ans += i
    print(ans)
