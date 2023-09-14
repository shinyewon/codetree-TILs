# 문제 링크: https://www.codetree.ai/missions/2/problems/merge-marbles?&utm_source=clipboard&utm_medium=text
# 소요 시간: 33분 48초
n, m, t = map(int, input().split())
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
for num in range(1, m + 1):
    r, c, d, w = input().split()
    i, j, w = int(r) - 1, int(c) - 1, int(w)
    grid[i][j] = [num, d, w]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dtoN = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(t):
    tmp_grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if grid[i][j] != []:
                dNum = dtoN[grid[i][j][1]]
                new_i, new_j = i + dis[dNum], j + djs[dNum]
                if not in_range(new_i, new_j):
                    d = grid[i][j][1]
                    if d == "L":
                        d = "R"
                    elif d == "R":
                        d = "L"
                    elif d == "U":
                        d = "D"
                    else:
                        d = "U"
                    grid[i][j][1] = d
                    new_i, new_j = i, j
                # 충돌 처리
                if tmp_grid[new_i][new_j] != []:  # 충돌하면
                    grid[i][j][2] += tmp_grid[new_i][new_j][2]
                    if grid[i][j][0] < tmp_grid[new_i][new_j][0]:
                        grid[i][j][0] = tmp_grid[new_i][new_j][0]
                        grid[i][j][1] = tmp_grid[new_i][new_j][1]
                # 임시 격자에 저장
                tmp_grid[new_i][new_j] = grid[i][j]
    grid = tmp_grid

cnt = 0
max_w = 1
for i in range(n):
    for j in range(n):
        if grid[i][j] != []:
            cnt += 1
            if grid[i][j][2] > max_w:
                max_w = grid[i][j][2]

print(cnt, max_w)
