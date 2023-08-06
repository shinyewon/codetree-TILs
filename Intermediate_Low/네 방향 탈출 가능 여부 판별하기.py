# 문제 링크: https://www.codetree.ai/missions/2/problems/determine-escapableness-with-4-ways?utm_source=clipboard&utm_medium=text
from collections import deque

n, m = map(int, input().split())
snake = [
    [1 for _ in range(m)]
    for _ in range(n)
]
for i in range(n):
    snake[i] = list(map(int, input().split()))

q = deque()
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < m


def can_go(i, j):
    if not in_range(i, j):
        return False
    if visited[i][j] or snake[i][j] == 0:
        return False
    return True


def bfs():
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            if can_go(new_i, new_j):
                q.append((new_i, new_j))
                visited[new_i][new_j] = 1


q.append((0, 0))
visited[0][0] = 1
bfs()
if visited[n-1][m-1]:
    print(1)
else:
    print(0)
