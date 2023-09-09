# Approach 2: 1초 간격으로 움직임을 직접 시뮬레이션 + 충돌을 2차원 배열로 확인
# 런타임 에러, 격자 크기 조정중...
T = int(input())  # 테스트 케이스 수
dtoN = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(T):
    min_i, min_j, max_i, max_j = 4000, 4000, 0, 0
    marbles = []
    N = int(input())  # 구슬 개수
    for num in range(1, N+1):
        print(num)
        x, y, w, d = input().split()
        i, j, w, dNum = int(x) * 2 + 2000, (-int(y)) * \
            2 + 2000, int(w), dtoN[d]

        if i > max_i:
            max_i = i
        if i < min_i:
            min_i = i
        if j > max_j:
            max_j = j
        if j < min_j:
            min_j = j
        marbles.append([num, i, j, w, dNum])
        print(num, i, j, w, dNum)

    def in_range(i, j):
        return i >= 0 and i < max_i + 1 and j >= 0 and j < max_j + 1

    colT = -1
    row, col = max_i - min_i + 1, max_j - min_j + 1
    for t in range(1, max(row, col)+1):
        print(t)
        next_marble_index = []
        next_marbles = []
        board = [
            [[] for _ in range(col)]
            for _ in range(row)
        ]
        # 이동
        for marble in marbles:
            marble[1], marble[2] = marble[1] + \
                dis[marble[4]], marble[2] + djs[marble[4]]
            if in_range(marble[1] - min_i, marble[2] - min_j):
                if board[marble[1]-min_i][marble[2]-min_j] == []:
                    board[marble[1] - min_i][marble[2] - min_j] = marble
                    next_marble_index.append([marble[1], marble[2]])
                else:
                    colT = t
                    if board[marble[1]][marble[2]][3] < marble[3]:
                        board[marble[1]][marble[2]] = marble
                    elif board[marble[1]][marble[2]] == marble[3] and board[marble[1]][marble[2]][0] < marble[0]:
                        board[marble[1]][marble[2]] = marble

        for i in range(len(next_marble_index)):
            next_marbles.append(
                board[next_marble_index[i][0]][next_marble_index[i][1]])

        marbles = next_marbles[:]

    print(colT)
