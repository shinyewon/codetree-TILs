# 문제 링크: https://www.codetree.ai/missions/2/problems/marble-movement?&utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 37분
n, m, t, k = map(int, input().split())
board = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    r, c, d, v = input().split()
    r, c, v = int(r) - 1, int(c) - 1, int(v)
    board[r][c].append([i, d, v])


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dtoN = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(t):
    tmp = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            for b in range(len(board[i][j])):  # 각각의 공에 대해서
                # v만큼 이동
                ci, cj = i, j
                move = 0
                while move < board[i][j][b][2]:
                    new_i, new_j = ci + \
                        dis[dtoN[board[i][j][b][1]]], cj + \
                        djs[dtoN[board[i][j][b][1]]]
                    if in_range(new_i, new_j):  # 이동 가능할 때
                        move += 1
                        if move == board[i][j][b][2]:
                            tmp[new_i][new_j].append(board[i][j][b])
                        ci, cj = new_i, new_j
                    else:  # 벽에 부딪혔을 때
                        if board[i][j][b][1] == 'U':
                            board[i][j][b][1] = 'D'
                        elif board[i][j][b][1] == 'D':
                            board[i][j][b][1] = 'U'
                        elif board[i][j][b][1] == 'L':
                            board[i][j][b][1] = 'R'
                        else:
                            board[i][j][b][1] = 'L'

    # 충돌 처리 및 복사
    for i in range(n):
        for j in range(n):
            while len(tmp[i][j]) > k:
                minV = 11
                minVI = -1
                for l in range(len(tmp[i][j])):
                    if tmp[i][j][l][2] < minV:
                        minV = tmp[i][j][l][2]
                        minVI = l
                    elif tmp[i][j][l][2] == minV:
                        if tmp[i][j][minVI][0] > tmp[i][j][l][0]:
                            minVI = l
                tmp[i][j].pop(minVI)
            board[i][j] = tmp[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(board[i][j])
print(cnt)
