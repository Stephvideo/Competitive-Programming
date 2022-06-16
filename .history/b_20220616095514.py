# 
for t in range(int(input())):
    n = int(input())

    s= input()

    ans = len(s)

    for i in range(n-1, 0, -1):
        curr = s[i]
        for j in range(i-1, -1, -1):
            if s[j] != curr:
                ans +=1
            else:
                break
    print(ans)
