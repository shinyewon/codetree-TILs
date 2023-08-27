# 문제 링크: https://www.codetree.ai/missions/2/problems/pinball-game?&utm_source=clipboard&utm_medium=text
# 소요 시간: 52분
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


max_time = 0
dToNum = {'D': 0, 'L': 1, 'U': 2, 'R': 3}
dis, djs = [1, 0, -1, 0], [0, -1, 0, 1]


def game(s_i, s_j, d):
    time = 0
    ball_i, ball_j = s_i, s_j
    dNum = dToNum[d]
    while True:
        time += 1
        new_i, new_j = ball_i + dis[dNum], ball_j + djs[dNum]
        if in_range(new_i, new_j):
            ball_i, ball_j = new_i, new_j
            if grid[ball_i][ball_j] == 1:
                if dNum == 2 or dNum == 0:
                    dNum = (dNum + 1) % 4
                else:
                    dNum = (dNum - 1 + 4) % 4
            elif grid[ball_i][ball_j] == 2:
                if dNum == 2 or dNum == 0:
                    dNum = (dNum - 1 + 4) % 4
                else:
                    dNum = (dNum + 1) % 4
        else:
            break
    return time


# 위, 아래에서 시작하는 경우
for j in range(n):
    time = game(-1, j, 'D')
    if time > max_time:
        max_time = time
    time = game(n, j, 'U')
    if time > max_time:
        max_time = time
# 왼쪽, 오른쪽에서 시작하는 경우
for i in range(n):
    time = game(i, -1, 'R')
    if time > max_time:
        max_time = time
    time = game(i, n, 'L')
    if time > max_time:
        max_time = time
print(max_time)
