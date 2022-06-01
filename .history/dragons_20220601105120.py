# https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())

str = list(map(int, input().split()))
bonus = list(map(int, input().split()))
dragons = []
for i in range(n):
    str, bonus = map(int, input().split())

    dragons.append((str, bonus))

dragons.sort(key = lambda x: x[0])

for i in range(len(dragons)):
    if s < dragons[i][0]:
        flag = True
        break
    else:
        s += dragons[i][1]

if flag:
    print("NO")
else:
    print("YES")
