def subStringCheck(s, length, needed):
    if length < needed:
        return False

    numOnes = s[0:length].count(1)
    if numOnes == needed:
        return True
    for i in range(1, len(s) - length+1):
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
    cumSum = [lst[0]]
    for i in range(1,n):
        cumSum.append(lst[i] + cumSum[i-1])

    ans = -1
    for i in range(n):
        low = i
        high = n-1

        while (high >= low):
            mid = (low + high)//2
            check = 0
            if i == 0:
                check = cumSum[mid]
            else:
                check = cumSum[mid] - cumSum[i-1]
            

            if check == s:
                if ans == -1:
                    ans = mid - i + 1
                elif n - (mid - i + 1) > ans:
                    ans = n - mid - i + 1
                low = mid + 1
           
            elif check < s:
                low = mid + 1
            else:
                high = mid - 1

    if ans == -1:
        print(-1)
    else:
        print (n-ans)