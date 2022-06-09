# https://codeforces.com/problemset/problem/1684/C

for t in range(int(input())):
    n, m = map(int, input().split())
    relativeOrder = [0] * m
    flag = False
    for row in range(n):
        currRow = list(map(int, input().split()))
        firstRow = -1
        secondRow = -1
        if row == 0:
            sortedRow = sorted(currRow)

            numDiff = 0
            
            for i in range(len(currRow)):
                if currRow[i] != sortedRow[i]:
                    numDiff += 1
                    if firstRow == -1:
                        firstRow = i
                        continue
                    elif secondRow == -1:
                        secondRow == i
                        continue                    
            if numDiff > 2:
                print(-1)
                flag = True
                break

            for i in range(len(currRow)):
                for j in range(len(sortedRow)):
                    if currRow[i] == sortedRow[j]:
                        relativeOrder[i] = j
                        break
        else:
            sortedRow = sorted(currRow)

            numDiff = 0
            for i in range(len(currRow)):
                if currRow[i] != sortedRow[i]:
                    numDiff += 1
            if numDiff != 2:
                print(-1)
                flag = True
                break
    if firstRow == -1 and secondRow == -1 and not flag:
        print("1 1")
    elif not flag:
        print(firstRow, " ", secondRow)

                        
        
                