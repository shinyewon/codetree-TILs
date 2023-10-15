# 문제 링크: https://www.codetree.ai/missions/2/problems/two-thieves?&utm_source=clipboard&utm_medium=text
# 소요 시간: 4시간
# 미해결

N, M, C = map(int, input().split())
rooms = [
    list(map(int, input().split()))
    for _ in range(N)
]


def find_max(weights, weight, value):
    '''무게가 C를 넘지 않으면서 가질 수 있는 최대 가치를 구함'''
    global max_value, C
    if len(weights) == 0:
        if value > max_value:
            max_value = value
        return
    selected_w = weights.pop()
    if weight + selected_w <= C:
        find_max(weights, weight+selected_w, value+selected_w**2)
    find_max(weights, weight, value)


def theif1(cur_i):
    global max_value, selected_i, selected_j
    if cur_i == N:
        return
    cur_j = 0
    cur_max_value = max_value
    while cur_j <= N - M:
        weight = 0
        weights = []
        for k in range(M):
            weight += rooms[cur_i][cur_j + k]
            weights.append(rooms[cur_i][cur_j + k])
        if weight <= C:
            value = 0
            for i in range(M):
                value += weights[i] * weights[i]
            if value > max_value:
                max_value = value
                selected_i, selected_j = cur_i, cur_j
        else:  # 무게가 C보다 크면 가장 가치가 큰 조합을 찾는다.
            find_max(weights, 0, 0)
            if cur_max_value != max_value:
                selected_i, selected_j = cur_i, cur_j
        cur_j += 1
    theif1(cur_i + 1)


def theif2(cur_i):
    global max_value
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
                    value += weights[i] * weights[i]
                if value > max_value:
                    max_value = value
            else:  # 무게가 C보다 크면 가장 가치가 큰 조합을 찾는다.
                find_max(weights, 0, 0)
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
                    value += weights[i] * weights[i]
                if value > max_value:
                    max_value = value
            else:  # 무게가 C보다 크면 가장 가치가 큰 조합을 찾는다.
                find_max(weights, 0, 0)
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
                    value += weights[i] * weights[i]
                if value > max_value:
                    max_value = value
            else:  # 무게가 C보다 크면 가장 가치가 큰 조합을 찾는다.
                find_max(weights, 0, 0)
            cur_j += 1
    theif2(cur_i + 1)


res = 0
max_value = 0
selected_i, selected_j = 0, 0
theif1(0)
res += max_value

max_value = 0
theif2(0)
res += max_value

print(res)
