# 문제 링크: https://www.codetree.ai/missions/2/problems/move-to-max-adjacent-cell-simultaneously?utm_source=clipboard&utm_medium=text
n, m, t = tuple(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    arr[i] = list(map(int, input().split()))

pos = [
    [0] * n
    for _ in range(n)
]
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    pos[r-1][c-1] = 1


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]


def max_i(i, j):
    maxNum = 0
    maxIndex = [-1, -1]
    for di, dj in zip(dis, djs):
        ni, nj = i + di, j + dj
        if in_range(ni, nj) and arr[ni][nj] > maxNum:
            maxNum = arr[ni][nj]
            maxIndex[0] = ni
            maxIndex[1] = nj
    return maxIndex


for _ in range(t):
    maxArr = []
    for i in range(n):
        for j in range(n):
            if pos[i][j] == 1:
                maxIndex = max_i(i, j)
                maxArr += [maxIndex]
                pos[i][j] = 0
    for i in range(len(maxArr)):
        pos[maxArr[i][0]][maxArr[i][1]] += 1
    for i in range(n):
        for j in range(n):
            if pos[i][j] >= 2:
                m -= pos[i][j]
                pos[i][j] = 0

print(m)
