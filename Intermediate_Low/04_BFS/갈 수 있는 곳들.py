# 문제 링크: https://www.codetree.ai/missions/2/problems/places-can-go?utm_source=clipboard&utm_medium=text
from collections import deque

n, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
q = deque()
for _ in range(k):
    r, c = map(int, input().split())
    q.append([r-1, c-1])
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def can_go(i, j):
    if not in_range(i, j):
        return False
    if board[i][j] == 1:
        return False
    if visited[i][j]:
        return False
    return True


cnt = 0
dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs():
    global cnt
    while q:
        i, j = q.popleft()
        if not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            for di, dj in zip(dis, djs):
                new_i, new_j = i + di, j + dj
                if can_go(new_i, new_j):
                    q.append([new_i, new_j])


bfs()
print(cnt)
