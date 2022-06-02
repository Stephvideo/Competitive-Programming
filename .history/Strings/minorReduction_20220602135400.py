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
            ans = ''.join((x[0:i], str(sum), x[i+1:]))
            break
        else:
            ans = ''.join((x[0:i-2], str(sum), x[i+1:]))
    sys.stdout.write(ans + "\n")        