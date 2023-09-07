# Approach 2: 1초 간격으로 움직임을 직접 시뮬레이션 + 충돌을 2차원 배열로 확인
# 메모리 초과
T = int(input())  # 테스트 케이스 수
dtoN = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(T):
    max_ij = 0
    marbles = []
    N = int(input())  # 구슬 개수
    for num in range(1, N+1):
        x, y, w, d = input().split()
        i, j, w, dNum = int(x) * 2 + 2000, (-int(y)) * \
            2 + 2000, int(w), dtoN[d]
        # 아래의 주석 부분으로 인해 메모리 초과가 발생한다.
        # if i > max_ij:
        #    max_ij = i
        # if j > max_ij:
        #    max_ij = j
        marbles.append([num, i, j, w, dNum])

    def in_range(i, j):
        return i >= 0 and i < max_ij + 1 and j >= 0 and j < max_ij + 1

    colT = -1
    for t in range(1, max_ij+1):
        print(t)
        next_marble_index = []
        next_marbles = []
        board = [
            [[] for _ in range(max_ij+1)]
            for _ in range(max_ij+1)
        ]
        # 이동
        for marble in marbles:
            marble[1], marble[2] = marble[1] + \
                dis[marble[4]], marble[2] + djs[marble[4]]
            if in_range(marble[1], marble[2]):
                if board[marble[1]][marble[2]] == []:
                    board[marble[1]][marble[2]] = marble
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
