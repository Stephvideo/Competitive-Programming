# https://codeforces.com/problemset/problem/1626/B

for t in range(int(input())):
    x = input()

    ans = ""
    
    for i in range(len(x)-1):
        if int(x[i]) + int(x[i+1]) < 10:
            ans += x[0:i] 
            ans += str(int(x[i]) + int(x[i+1]))
            ans += x[i+2:len(x)]
            break
        if i == 0:
            ans += str(int(x[i]) + int(x[i+1]))
            ans += x[i+2:len(x)]


    print(ans)        