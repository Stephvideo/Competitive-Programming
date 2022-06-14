def subStringCheck(s, length, needed):
    if length < needed:
        return False

    numOnes = s[0:length].count(1)
    if numOnes == needed:
        return True
    for i in range(1, len(s) - length):
        if s[i-1] != s[i-1 + length]:
            if s[i-1] == 1:
                numOnes -= 1
            else:
                numOnes += 1

        if numOnes == needed:
            return True
    return False

for t in range(int(input())):
    n, s = map(int, input().split())

    lst = list(map(int, input().split()))
    ans = -1

    low = 0
    high = n

    while high > low:
        mid = (low + high)//2

        if subStringCheck(lst, mid, s):
            ans = mid
            low = mid + 1
        else:
            if mid < s:
                low = mid + 1
            else:
                high = mid - 1


    #print(*lst[front:last+1])
    if ans == -1:
        print(ans)
    else:
        print(n - ans)
    