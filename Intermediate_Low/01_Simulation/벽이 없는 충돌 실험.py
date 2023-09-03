# Approach 1: 1초 간격으로 움직임을 직접 시뮬레이션 [Time Limit Exceed]

T = int(input())  # 테스트 케이스 수
dtoN = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dxs, dys = [0, 0, -0.5, 0.5], [0.5, -0.5, 0, 0]
max_xy = 1
for _ in range(T):
    balls = []
    N = int(input())  # 구슬 개수
    for i in range(1, N+1):
        x, y, w, d = input().split()
        x, y, w, dNum = float(x), float(y), int(w), dtoN[d]
        if abs(x) > max_xy:
            max_xy = abs(x)
        if abs(y) > max_xy:
            max_xy = abs(y)
        balls.append([i, x, y, w, dNum])

    colT = -1
    for t in range(1, int(max_xy*4+1)):
        # 이동
        for ball in balls:
            ball[1], ball[2] = ball[1] + dxs[ball[4]], ball[2] + dys[ball[4]]
        # 충돌 처리
        for k in range(len(balls)):
            if k < len(balls):
                dups = [balls[k]]
                pops = []
                for k2 in range(len(balls[k+1:])):
                    if balls[k][1] == balls[k+1:][k2][1] and balls[k][2] == balls[k+1:][k2][2]:
                        dups.append(balls[k+1:][k2])
                        pops.append(k+1 + k2)

                cnt = 0
                for i in pops:
                    balls.pop(i-cnt)
                    cnt += 1

                if len(dups) > 1:
                    balls.pop(k)
                    colT = t
                    max_ball = [0, 0, 0, 0, 0]
                    for dup in dups:
                        if dup[3] > max_ball[3]:
                            max_ball = dup
                        elif dup[3] == max_ball[3]:
                            if dup[0] > max_ball[0]:
                                max_ball = dup
                    balls = [max_ball] + balls

    print(colT)
