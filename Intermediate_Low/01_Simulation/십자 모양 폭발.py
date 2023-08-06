# 문제 링크: https://www.codetree.ai/missions/2/problems/cross-shape-bomb?utm_source=clipboard&utm_medium=text
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = tuple(map(int, input().split()))


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
num = arr[r-1][c-1]
for k in range(num):
    for di, dj in zip(dis, djs):
        ni, nj = r-1 + di*k, c-1 + dj*k
        if in_range(ni, nj):
            arr[ni][nj] = 0

for i in range(n-1, 0, -1):
    for j in range(n):
        if arr[i][j] == 0:
            if j != c-1:
                arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
            else:
                i2 = i
                while arr[i2][j] == 0 and i2 > 0:
                    i2 -= 1
                arr[i][j], arr[i2][j] = arr[i2][j], arr[i][j]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
