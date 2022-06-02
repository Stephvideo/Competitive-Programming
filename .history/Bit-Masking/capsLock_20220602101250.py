# https://codeforces.com/problemset/problem/131/A

s = input()

if len(s) == 1:
    print(s.upper())
    exit()
if s.isupper():
    print(s.lower())
    exit()

firstUpper = False
flag = False
for i in range(len(s)):
    if i == 0:
        if s[i].isupper():
            firstUpper = True
            break
        continue
    if s[i].islower():
        flag = True
        break
if firstUpper or flag:
    print(s)
    exit()
else:
    ans = ""
    for i in range(len(s)):
        if i == 0:
            ans += s[i].upper()
        else:
            ans += s[i].lower
    print(ans)
