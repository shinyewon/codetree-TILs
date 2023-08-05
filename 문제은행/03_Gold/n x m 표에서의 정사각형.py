# 문제 링크: https://www.codetree.ai/training-field/search/problems/squares-in-an-n-x-m-table?page=1&pageSize=20&name=n+x+m+utm_source=clipboard&utm_medium=text
from collections import deque
n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
dis, djs = [0, 1, 1], [1, 1, 0]
cnt = 0


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < m


def dfs(i, j, k):
    global cnt
    ok = True
    for di in range(k):
        for dj in range(k):
            if not in_range(i+di, j+dj) or arr[i+di][j+dj] != 1:
                ok = False
                break
        if not ok:
            break
    if ok:
        cnt += 1
        dfs(i, j, k+1)


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            dfs(i, j, 2)
print(cnt)
