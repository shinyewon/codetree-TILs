# 문제 링크: https://www.codetree.ai/training-field/search/problems/DFS-and-BFS?page=1&pageSize=20&name=dfsutm_source=clipboard&utm_medium=text
from collections import deque
n, m, s = map(int, input().split())
edges = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]
for _ in range(m):
    i, j = map(int, input().split())
    edges[i][j] = 1
    edges[j][i] = 1

visited = [False for _ in range(n+1)]
res = []


def dfs(n, m, s, visited, res):
    for j in range(1, n+1):
        if edges[s][j] == 1 and not visited[j]:
            visited[j] = True
            res.append(j)
            dfs(n, m, j, visited, res)


visited[s] = True
res.append(s)
dfs(n, m, s, visited, res)
for num in res:
    print(num, end=" ")
print()

visited = [False for _ in range(n+1)]
res = []
q = deque()


def bfs(n, m, s, visited, res):
    while q:
        v = q.popleft()
        for j in range(1, n+1):
            if edges[v][j] == 1 and not visited[j]:
                visited[j] = True
                q.append(j)
                res.append(j)


q.append(s)
res.append(s)
visited[s] = True
bfs(n, m, s, visited, res)
for num in res:
    print(num, end=" ")
print()
