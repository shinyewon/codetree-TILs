# Approach 2: 1초 간격으로 움직임을 직접 시뮬레이션 + 충돌을 2차원 배열로 확인
# 오답노트: next_marble_index 배열의 크기가 매우 크기 때문에 전역 변수로 선언한 후,
#          매초마다 초기화해야 할 인덱스만 선택적으로 초기화해주어야 한다.
COORD_SIZE = 4000
BLANK = -1

T = int(input())  # 테스트 케이스 수
dtoN = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]

next_marble_index = [
    [BLANK for _ in range(COORD_SIZE + 1)]
    for _ in range(COORD_SIZE + 1)
]

for _ in range(T):
    marbles = []
    N = int(input())  # 구슬 개수
    for num in range(1, N+1):
        x, y, w, d = tuple(input().split())
        i, j, w, dNum = (-int(y)) * 2 + 2000, int(x) * \
            2 + 2000, int(w), dtoN[d]
        marbles.append((num, i, j, w, dNum))

    colT = -1

    def in_range(i, j):
        return i >= 0 and i < COORD_SIZE + 1 and j >= 0 and j < COORD_SIZE + 1

    for t in range(1, COORD_SIZE + 1):
        next_marbles = []
        # 이동
        for marble in marbles:
            num, i, j, w, dNum = marble
            new_i, new_j = i + dis[dNum], j + djs[dNum]
            if in_range(new_i, new_j):
                if next_marble_index[new_i][new_j] == BLANK:
                    next_marbles.append((num, new_i, new_j, w, dNum))
                    next_marble_index[new_i][new_j] = len(next_marbles) - 1
                else:
                    colT = t
                    # 무게가 크면
                    if next_marbles[next_marble_index[new_i][new_j]][3] < w:
                        next_marbles[next_marble_index[new_i][new_j]] = (
                            num, new_i, new_j, w, dNum)
                    # 무게가 같고 번호가 크면
                    elif next_marbles[next_marble_index[new_i][new_j]][3] == w and next_marbles[next_marble_index[new_i][new_j]][0] < num:
                        next_marbles[next_marble_index[new_i][new_j]] = (
                            num, new_i, new_j, w, dNum)

        marbles = next_marbles[:]

        # 다음 수행을 위한 초기화
        for marble in next_marbles:
            next_marble_index[marble[1]][marble[2]] = BLANK

    print(colT)
