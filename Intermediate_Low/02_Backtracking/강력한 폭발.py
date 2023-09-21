# 문제 링크: https://www.codetree.ai/missions/2/problems/strong-explosion?&utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 30분
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
maxCnt = 0


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


bombs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append([i, j])

dis, djs = [[-2, -1, 1, 2], [-1, 0, 1, 0], [-1, -1, 1, 1]
            ], [[0, 0, 0, 0], [0, 1, 0, -1], [-1, 1, 1, -1]]


def maxExplode(grid, bombs, cnt):
    global maxCnt
    if len(bombs) == 0:
        if cnt > maxCnt:
            maxCnt = cnt
        return

    i, j = bombs[0][0], bombs[0][1]
    for k in range(3):  # 3종류의 폭탄
        next_grid = [
            grid[i][:] for i in range(n)
        ]
        next_grid[i][j] = 2
        cnt2 = 1
        for index in range(4):
            new_i, new_j = i + dis[k][index], j + djs[k][index]
            if in_range(new_i, new_j) and next_grid[new_i][new_j] == 0:
                next_grid[new_i][new_j] = 2
                cnt2 += 1
        maxExplode(next_grid, bombs[1:], cnt+cnt2)


maxExplode(grid, bombs, 0)
print(maxCnt)
