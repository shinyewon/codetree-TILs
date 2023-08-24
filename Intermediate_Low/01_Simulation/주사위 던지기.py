# 문제 링크: https://www.codetree.ai/missions/2/problems/roll-a-dice?&utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 30분
n, m, r, c = map(int, input().split())
dirs = input().split()
dice = [
    [4, 1, 3],  # top
    [4, 5, 3],  # back
    [4, 6, 3],  # floor
    [4, 2, 3]  # front
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


i, j = r-1, c-1
nums = [
    [0 for _ in range(n)]
    for _ in range(n)
]
nums[i][j] = 6
map_d = {'L': 0, 'R': 1, 'U': 2, 'D': 3}
dis, djs = [0, 0, -1, 1], [-1, 1, 0, 0]
for d in dirs:
    dNum = map_d[d]
    new_i, new_j = i + dis[dNum], j + djs[dNum]
    if in_range(new_i, new_j):
        i, j = new_i, new_j
        # dice 리스트 업데이트
        top = dice[0][1]
        front = dice[3][1]
        right = dice[1][2]
        if d == 'U' or d == 'D':
            top = dice[0 + dis[dNum]][1]
            front = dice[(3 + dis[dNum]) % 4][1 + djs[dNum]]
        else:
            top = dice[0][1 - djs[dNum]]
            right = dice[1 - djs[dNum]][1]
        dice = [
            [7-right, top, right],
            [7-right, 7-front, right],
            [7-right, 7-top, right],
            [7-right, front, right]
        ]
        nums[i][j] = dice[2][1]

res = 0
for i in range(n):
    for j in range(n):
        res += nums[i][j]
print(res)
