# https://codeforces.com/problemset/problem/1421/A

inf = 100000000000000


T = int(input())

for t in range(T):
    a, b = map(int, input().split())

    min = inf

    x = a

    calc = ((a &  ~x) | ( ~a & x) ) or ((b & ~x) or (~b & x))

    if calc < min:
        min = calc
    
    x = b
    calc = ((a &  ~x) | ( ~a & x) ) or ((b & ~x) or (~b & x))
    if calc < min:
        min = calc

    print (min)