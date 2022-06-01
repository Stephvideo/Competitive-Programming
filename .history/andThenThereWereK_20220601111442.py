# https://codeforces.com/problemset/problem/1527/A

T = int(input())

for t in range(T):
    n = int(input())
    k = n
    

    while(True):
        k -= 1
        n &= k

        if n == 0:
            print(k)
            exit()