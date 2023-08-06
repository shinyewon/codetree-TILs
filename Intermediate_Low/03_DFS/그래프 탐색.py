# 문제 링크: https://www.codetree.ai/missions/2/problems/graph-traversal?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

res = 0


def dfs(v):
    global res
    for adj_v in arr[v]:
        if not visited[adj_v]:
            res += 1
            visited[adj_v] = True
            dfs(adj_v)


visited[1] = True
dfs(1)
print(res)
