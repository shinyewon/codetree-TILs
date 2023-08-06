# 문제 링크: https://www.codetree.ai/missions/2/problems/knight-movements?utm_source=clipboard&utm_medium=text
from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
# 해당 격자 칸에 도달하는 데 필요한 최소 이동 횟수를 저장
arr = [
    [-1 for _ in range(n)]
    for _ in range(n)
]
dis, djs = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def bfs():
    global can_arrive
    while q and not can_arrive:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            if in_range(new_i, new_j) and arr[new_i][new_j] == -1:
                arr[new_i][new_j] = arr[i][j] + 1
                if new_i == r2 - 1 and new_j == c2 - 1:
                    can_arrive = True
                    print(arr[r2-1][c2-1])
                    break
                else:
                    q.append([new_i, new_j])


if r1 == r2 and c1 == c2:
    print(0)
else:
    q = deque()
    q.append([r1-1, c1-1])
    arr[r1-1][c1-1] = 0
    can_arrive = False
    bfs()
    if not can_arrive:
        print(-1)
