# https://codeforces.com/problemset/problem/1613/C
def checkDamage(attacks, k, h):
    damage = 0
    for i in range(len(attacks)):
        if i == len(attacks) - 1:
            damage += k
            continue

        if attacks[i] + k > attacks[i+1]:
            damage += attacks[i+1] - attacks[i]
        else:
            damage += k
    if damage >= h:
        return True
    else:
        return False

    
for t in range(int(input())):
    n, h = map(int, input().split())

    attacks = list(map(int, input().split()))


    ans = None
    guess = None
    low = 0
    high = 100 ** 500

    while high >= low:
        mid = (high + low) // 2
        possible = checkDamage(attacks, mid, h)
        if possible:
            guess = mid
            high = mid - 1
        else:
            low = mid + 1





    print (guess)