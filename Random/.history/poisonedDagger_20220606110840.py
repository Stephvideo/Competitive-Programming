# https://codeforces.com/problemset/problem/1613/C
def checkDamage(attacks, k, h):
    damage = 0
    for i in range(len(attacks)):
        if attacks[i] + k > attacks[i+1]:
            #

for t in range(int(input())):
    n, h = map(int, input().split())

    attacks = list(map(int, input().split()))

    damage = 0

    ans = None

    low = 0
    high = 100 ** 500

    while high >= low:
        mid = (high + low) // 2




    

    print (ans)