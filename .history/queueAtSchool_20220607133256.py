# https://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split())

s = input()
s = list(s)
swapped = False
for T in range(t):
    for i in range(0, n-1):
        # if swapped:
        #     swapped = True
        #     continue

        if s[i] == 'B' and s[i+1] == 'G':
            swapped = True
            s[i], s[i+1] = s[i+1], s[i]

s = ''.join(s)
print(s)

