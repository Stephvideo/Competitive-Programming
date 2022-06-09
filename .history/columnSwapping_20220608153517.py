# https://codeforces.com/problemset/problem/1684/C

for t in range(int(input())):
    n, m = map(int, input().split())
    relativeOrder = [0] * m
    for row in range(n):
        currRow = list(map(int, input().split()))
        firstRow = -1
        secondRow = -1
        if row == 0:
            sortedRow = sorted(row)

            numDiff = 0
            
            for i in range(len(currRow)):
                if currRow[i] != sortedRow[i]:
                    if firstRow == -1:
                        firstRow = i
                    elif secondRow == -1:
                        secondRow == i

                    numDiff += 1

            if numDiff > 2:
                print(-1)
                continue

            for i in range(len(row)):
                for j in range(len(sortedRow)):
                    if row[i] == sortedRow[j]:
                        relativeOrder[i] = j
                        break
        else:
            sortedRow = sorted(row)

            numDiff = 0
            for i in range(len(row)):
                if row[i] != sortedRow[i]:
                    numDiff += 1
            if numDiff != 2:
                print(-1)
                continue
    if firstRow == -1 and secondRow == -1:
        print("1 1")
    else:
        print(firstRow, " ", secondRow)

                        
        
                