# https://codeforces.com/problemset/problem/1626/B

for t in range(int(input())):
    x = input()

    ans = ""
    
    for i in range(len(x)-1, 0, -1):
        sum = int(x[i]) + int(x[i-1])
        if sum > 10:
            ans = ""
            ans += x[0:i-1]
            ans += str(sum)
            ans += x[i+1,len(x)]
            break
        else:
            ans = ""
            ans += x[0:i-1]
            ans += str(sum)
            ans += x[i+1,len(x)]

    print(ans)        