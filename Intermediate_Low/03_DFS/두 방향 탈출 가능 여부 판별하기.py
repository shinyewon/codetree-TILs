# 문제 링크: https://www.codetree.ai/missions/2/problems/determine-escapableness-with-2-ways?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for i in range(n):
    arr[i] = list(map(int, input().split()))


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True


escape = 0


def dfs(x, y):
    dxs, dys = [1, 0], [0, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)


visited[0][0] = True
dfs(0, 0)
if visited[n-1][m-1]:
    escape = 1
print(escape)
