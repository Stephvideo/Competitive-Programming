# https://codeforces.com/problemset/problem/1626/B
# My solution is the same as the intended solution from the editorial
# I am receiving a TLE 
import io,os,sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

for t in range(int(input())):
    x = input()

    ans = ""
    
    for i in range(len(x)-1, 0, -1):
        sum = int(x[i]) + int(x[i-1])
        if sum >= 10:
            ans = ""
            ans += x[0:i-1]
            ans += str(sum) 
            ans += x[(i+1):len(x)]
            break
        else:
            ans = ""
            ans += x[0:i-1]
            ans += str(sum)
            ans += x[i+1:len(x)]

    sys.stdout.write(ans + "\n")        