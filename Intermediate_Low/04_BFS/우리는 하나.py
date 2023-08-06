# 문제 링크: https://www.codetree.ai/missions/2/problems/we-are-the-one?utm_source=clipboard&utm_medium=text
from collections import deque
n, k, u, d = map(int, input().split())
cities = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
res = 0


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def can_go(i, j):
    if not in_range(i, j):
        return False
    if visited[i][j]:
        return False
    return True


q = deque()
dis, djs = [-1, 1, 0, 0], [0, 0, 1, -1]


def bfs():
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            if can_go(new_i, new_j) and u <= abs(cities[i][j] - cities[new_i][new_j]) <= d:
                q.append([new_i, new_j])
                visited[new_i][new_j] = 1
                cnt += 1
    return cnt


cnt = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            q.append([i, j])
            visited[i][j] = 1
            cnt.append(bfs())
res += max(cnt) if cnt else 0
if len(cnt) > 1:
    if k >= 2:
        max_i = cnt.index(max(cnt))
        cnt = cnt[:max_i] + cnt[max_i+1:]
        if len(cnt) >= 2:
            res += max(cnt)
            if k == 3:
                max2_i = cnt.index(max(cnt))
                cnt = cnt[:max_i] + cnt[max_i+1:]
                res += max(cnt)
        elif len(cnt) == 1:
            res += cnt[0]

print(res)
