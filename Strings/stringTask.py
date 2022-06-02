# https://codeforces.com/problemset/problem/118/A

def isVowel(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    if s in vowels:
        return True
    return False

s = input()
s = s.lower()
ans = ""
for i in range(len(s)):
    if isVowel(s[i]):
        continue

    ans += '.'
    ans += s[i]

print (ans)

