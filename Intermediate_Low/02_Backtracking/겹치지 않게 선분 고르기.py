n = int(input())
lines = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append([x1, x2])


def selectMaxLine(selectedLines, i):
    global maxCnt
    if len(selectedLines) > maxCnt:
        maxCnt = len(selectedLines)

    if i >= n:
        return

    isOverlap = False
    for line in selectedLines:
        if (line[0] <= lines[i][0] and lines[i][0] <= line[1]) or (line[0] <= lines[i][1] and lines[i][1] <= line[1]) or (lines[i][0] < line[0] and lines[i][1] > line[1]):
            isOverlap = True
            break
    if not isOverlap:
        selectMaxLine(selectedLines + [lines[i]], i+1)
    selectMaxLine(selectedLines, i+1)


maxCnt = 0
selectMaxLine([], 0)
print(maxCnt)
