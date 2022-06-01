# https://codeforces.com/problemset/problem/1421/A

from cmath import inf


T = int(input())

for t in range(T):
    a, b = map(int, input().split())

    min = inf

    x = a

    calc = ((a and not x) or (not a and x) ) or ((b and not x) or (not b and x))

    if calc < min:
        min = calc
    
    x = b
    calc = ((a and not x) or (not a and x) ) or ((b and not x) or (not b and x))
    if calc < min:
        min = calc

    print (min)