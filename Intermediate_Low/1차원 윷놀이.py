# 문제 링크: https://www.codetree.ai/missions/2/problems/yutnori-1d?utm_source=clipboard&utm_medium=text
n, m, k = tuple(map(int, input().split()))
pos = [1 for _ in range(k)]  # 각 말의 위치 기록
dis = list(map(int, input().split()))
score = 0


def dfs(n, m, k, dis, pos):
    global score
    global total_dis
    if n == 0:
        point = 0
        for p in pos:
            if p >= m:
                point += 1
        if point > score:
            score = point
        return

    if score == (1 + total_dis) // m or score == k:
        return

    for d in dis:
        for game_piece in range(k):
            if pos[game_piece] >= m:  # 이미 m번에 도달한 말은 움직이지 않는다.
                point = 0
                for p in pos:
                    if p >= m:
                        point += 1
                if point > score:
                    score = point
                continue
            pos[game_piece] += d
            dfs(n-1, m, k, dis[1:], pos)
            pos[game_piece] -= d
    return


total_dis = 0
for d in dis:
    total_dis += d
if 1 + total_dis < m:
    print(0)
else:
    dfs(n, m, k, dis, pos)
    print(score)
