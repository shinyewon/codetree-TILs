# 문제 링크: https://www.codetree.ai/missions/2/problems/sequential-movement-of-numbers?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    arr[i] = list(map(int, input().split()))


def findNumIndex(num):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                return i, j


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def findMaxIndex(i, j):
    Max = 0
    Max_i, Max_j = 0, 0
    for di, dj in zip(dis, djs):
        ni, nj = i + di, j + dj
        if in_range(ni, nj) and arr[ni][nj] > Max:
            Max = arr[ni][nj]
            Max_i, Max_j = ni, nj
    return Max_i, Max_j


dis, djs = [1, -1, 0, 0, -1, -1, 1, 1], [0, 0, 1, -1, -1, 1, -1, 1]
for _ in range(m):
    for num in range(1, n*n+1):
        i, j = findNumIndex(num)
        Max_i, Max_j = findMaxIndex(i, j)
        arr[i][j], arr[Max_i][Max_j] = arr[Max_i][Max_j], arr[i][j]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
