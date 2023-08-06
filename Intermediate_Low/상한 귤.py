# 문제 링크: https://www.codetree.ai/missions/2/problems/oranges-have-gone-bad?utm_source=clipboard&utm_medium=text
from collections import deque
n, k = map(int, input().split())
status = [
    list(map(int, input().split()))
    for _ in range(n)
]
res = [
    [-2 for _ in range(n)]
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


q = deque()
for i in range(n):
    for j in range(n):
        if status[i][j] == 2:
            q.append([i, j])
            res[i][j] = 0
            k -= 1
            if k == 0:
                break
    if k == 0:
        break

dis, djs = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            if in_range(new_i, new_j) and res[new_i][new_j] == -2 and status[new_i][new_j] == 1:
                res[new_i][new_j] = res[i][j] + 1
                q.append([new_i, new_j])


bfs()
for i in range(n):
    for j in range(n):
        if status[i][j] == 0:
            print(-1, end=" ")
        else:
            print(res[i][j], end=" ")
    print()
