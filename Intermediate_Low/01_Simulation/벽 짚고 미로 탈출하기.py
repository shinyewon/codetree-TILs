# 문제 링크: https://www.codetree.ai/missions/2/problems/escape-maze-with-wall-following?&utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 20분
n = int(input())
x, y = map(int, input().split())
s_i, s_j = x - 1, y - 1
maze = [
    [c for c in input()]
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


time = 0
d = 0  # 방향
dis, djs = [0, -1, 0, 1], [1, 0, -1, 0]  # 우 상 좌 하
while in_range(s_i, s_j):
    new_i, new_j = s_i + dis[d], s_j + djs[d]
    if in_range(new_i, new_j):
        # 바라보고 있는 방향으로 이동하는 것이 가능하지 않은 경우
        if maze[new_i][new_j] == '#':
            d = (d+1) % 4
        # 만약 그 방향으로 이동했다 가정했을 때
        elif in_range(new_i+dis[(d-1+4) % 4], new_j+djs[(d-1+4) % 4]):
            # 그 방향으로 한 칸 이동
            s_i, s_j = new_i, new_j
            time += 1
            new_d = (d-1+4) % 4
            # 해당 방향을 기준으로 오른쪽에 벽이 존재하지 않는다면,
            if maze[new_i+dis[new_d]][new_j+djs[new_d]] == '.':
                d = new_d
                s_i, s_j = s_i + dis[d], s_j + djs[d]
                time += 1
        else:
            time = -1
            s_i = n
    # 바로 앞이 격자 밖이라면 이동하여 탈출
    else:
        s_i, s_j = new_i, new_j
        time += 1
    # 처음의 방향과 자리로 돌아온 경우(탈출 불가능한 경우)
    if d == 0 and s_i == x-1 and s_j == y-1:
        time = -1
        break

print(time)
