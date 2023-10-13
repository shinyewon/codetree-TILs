# 문제 링크: https://www.codetree.ai/missions/2/problems/two-thieves?&utm_source=clipboard&utm_medium=text
# 소요 시간: 2시간
# 미해결 - 테스트케이스 80% 통과

N, M, C = map(int, input().split())
rooms = [
    list(map(int, input().split()))
    for _ in range(N)
]


def theif1(cur_i):
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
        value = 0
        if weight <= C:
            for i in range(M):
                value += weights[i] ** 2
        else:  # 무게가 C보다 크면
            # 최대한 큰 무게들로 이루어진 조합을 찾는다.
            weights.sort()
            weight = 0
            for i in range(M-1, -1, -1):
                if weights[i] <= C - weight:
                    value += weights[i] ** 2
                    weight += weights[i]
                if weight == C:
                    break
        if value > max_value:
            max_value = value
            selected_i, selected_j = cur_i, cur_j
        cur_j += 1
    theif1(cur_i + 1)


def theif2(cur_i):
    global max_value2
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
                for i in range(M):
                    value += weights[i] ** 2
            else:  # 무게가 C보다 크면
                # 최대한 큰 무게들로 이루어진 조합을 찾는다.
                weights.sort()
                weight = 0
                for i in range(M-1, -1, -1):
                    if weights[i] <= C - weight:
                        value += weights[i] ** 2
                        weight += weights[i]
                    if weight == C:
                        break
            if value > max_value2:
                max_value2 = value
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
                for i in range(M):
                    value += weights[i] ** 2
            else:  # 무게가 C보다 크면
                # 최대한 큰 무게들로 이루어진 조합을 찾는다.
                weights.sort()
                weight = 0
                for i in range(M-1, -1, -1):
                    if weights[i] <= C - weight:
                        value += weights[i] ** 2
                        weight += weights[i]
                    if weight == C:
                        break
            if value > max_value2:
                max_value2 = value
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
                for i in range(M):
                    value += weights[i] ** 2
            else:  # 무게가 C보다 크면
                # 최대한 큰 무게들로 이루어진 조합을 찾는다.
                weights.sort()
                weight = 0
                for i in range(M-1, -1, -1):
                    if weights[i] <= C - weight:
                        value += weights[i] ** 2
                        weight += weights[i]
                    if weight == C:
                        break
            if value > max_value2:
                max_value2 = value
            cur_j += 1
    theif2(cur_i + 1)


max_value = 0
selected_i, selected_j = 0, 0
theif1(0)

max_value2 = 0
theif2(0)

print(max_value + max_value2)
