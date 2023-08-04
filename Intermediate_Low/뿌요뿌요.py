# 문제 링크: https://www.codetree.ai/missions/2/problems/puyo-puyo?utm_source=clipboard&utm_medium=text
n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
cnt = 0
size = 1
max_size = 1


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(i, j):
    global cnt
    global size
    global max_size
    if size > max_size:
        max_size = size

    if size == 4:
        cnt += 1
    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj
        if in_range(new_i, new_j) and (not visited[new_i][new_j]) and board[i][j] == board[new_i][new_j]:
            visited[new_i][new_j] = True
            size += 1
            dfs(new_i, new_j)


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            size = 0
            dfs(i, j)

print(cnt, max_size)
