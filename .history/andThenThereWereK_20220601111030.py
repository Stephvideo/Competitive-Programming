# https://codeforces.com/problemset/problem/1527/A

T = int(input())

for t in range(T):
    n = int(input())
    n = bin(n)
    k = n

    while(True):
        k -= 1
        n &= bin(k)

        if n == 0b0:
            print(k)
            exit()