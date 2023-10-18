# 문제 링크: https://www.codetree.ai/missions/2/problems/two-thieves?&utm_source=clipboard&utm_medium=text
# 소요 시간: 4시간 30분
N, M, C = map(int, input().split())
rooms = [
    list(map(int, input().split()))
    for _ in range(N)
]


def findMaxVal(weights, selected_w, weight, value):
    '''최대 가치를 찾는 함수'''
    global C, max_value
    if len(weights) == 1:
        if weight + weights[0] <= C and value + weights[0]**2 > max_value:
            max_value = value + weights[0]**2
        elif weight <= C and max_value < value:
            max_value = value
        return
    findMaxVal(weights[1:], selected_w + [weights[0]],
               weight + weights[0], value + weights[0]**2)
    findMaxVal(weights[1:], selected_w, weight, value)


def thief1(cur_i):
    global max_value, selected_i, selected_j
    if cur_i == N:
        return
    cur_j = 0
    while cur_j <= N - M:
        weight = 0
        weights = []
        for k in range(M):
            weight += rooms[cur_i][cur_j + k]
            weights.append(rooms[cur_i][cur_j + k])
        if weight <= C:
            value = 0
            for i in range(M):
                value += weights[i] ** 2
            if value > max_value:
                max_value = value
                selected_i, selected_j = cur_i, cur_j
        else:  # 무게가 C보다 크면
            before_maxV = max_value
            findMaxVal(weights, [], 0, 0)
            if before_maxV < max_value:
                selected_i, selected_j = cur_i, cur_j
        cur_j += 1
    thief1(cur_i + 1)


def thief2(cur_i):
    global max_value, selected_i, selected_j
    if cur_i == N:
        return
    cur_j = 0
    if cur_i == selected_i:
        while cur_j <= selected_j - M:
            weight = 0
            weights = []
            for k in range(M):
                weight += rooms[cur_i][cur_j + k]
                weights.append(rooms[cur_i][cur_j + k])
            value = 0
            if weight <= C:
                value = 0
                for i in range(M):
                    value += weights[i] ** 2
                if value > max_value:
                    max_value = value
            else:  # 무게가 C보다 크면
                before_maxV = max_value
                findMaxVal(weights, [], 0, 0)
            cur_j += 1

        cur_j = selected_j + M
        while cur_j <= N - M:
            weight = 0
            weights = []
            for k in range(M):
                weight += rooms[cur_i][cur_j + k]
                weights.append(rooms[cur_i][cur_j + k])
            value = 0
            if weight <= C:
                value = 0
                for i in range(M):
                    value += weights[i] ** 2
                if value > max_value:
                    max_value = value
            else:  # 무게가 C보다 크면
                before_maxV = max_value
                findMaxVal(weights, [], 0, 0)
            cur_j += 1

    else:
        while cur_j <= N - M:
            weight = 0
            weights = []
            for k in range(M):
                weight += rooms[cur_i][cur_j + k]
                weights.append(rooms[cur_i][cur_j + k])
            value = 0
            if weight <= C:
                value = 0
                for i in range(M):
                    value += weights[i] ** 2
                if value > max_value:
                    max_value = value
            else:  # 무게가 C보다 크면
                before_maxV = max_value
                findMaxVal(weights, [], 0, 0)
            cur_j += 1
    thief2(cur_i + 1)


res = 0
max_value = 0
selected_i, selected_j = 0, 0
thief1(0)
res += max_value

max_value = 0
thief2(0)
res += max_value

print(res)
