# 문제 링크: https://www.codetree.ai/missions/2/problems/collision-experiment-with-wall?&utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 10분
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    def in_range(i, j):
        return i >= 0 and i < n and j >= 0 and j < n
    board = [
        ['.' for _ in range(n)]
        for _ in range(n)
    ]
    for _ in range(m):
        x, y, d = input().split()
        x = int(x) - 1
        y = int(y) - 1
        board[x][y] = d
    dToNum = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 구슬 이동
    for _ in range(300):
        tmp_board = [
            ['.' for _ in range(n)]
            for _ in range(n)
        ]
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    dNum = dToNum[board[i][j]]
                    new_i, new_j = i + dis[dNum], j + djs[dNum]
                    if in_range(new_i, new_j):
                        if tmp_board[new_i][new_j] != '.':  # 충돌
                            tmp_board[new_i][new_j] = 'c'
                        else:
                            tmp_board[new_i][new_j] = board[i][j]
                    else:  # 공이 벽에 부딪히면
                        if tmp_board[i][j] != '.':  # 충돌
                            tmp_board[i][j] = 'c'
                        else:
                            if board[i][j] == 'U':
                                tmp_board[i][j] = 'D'
                            elif board[i][j] == 'D':
                                tmp_board[i][j] = 'U'
                            elif board[i][j] == 'L':
                                tmp_board[i][j] = 'R'
                            else:
                                tmp_board[i][j] = 'L'
        # 복사
        for i in range(n):
            for j in range(n):
                if tmp_board[i][j] == 'c':
                    board[i][j] = '.'
                else:
                    board[i][j] = tmp_board[i][j]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                cnt += 1
    print(cnt)
