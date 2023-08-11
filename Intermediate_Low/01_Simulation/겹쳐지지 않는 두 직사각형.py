# 문제 링크: https://www.codetree.ai/missions/2/problems/non-overlapping-two-rectangles?utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 43분 31초
n, m = map(int, input().split())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]
total_sum = -2000
rect1_pos = [0, 0, 0, 0]
rect2_pos = [0, 0, 0, 0]
# 가능한 모든 rect1을 구한다.
for i in range(n):
    for j in range(m):
        for w in range(1, m-j+1):
            for h in range(1, n-i+1):
                rect1 = 0
                for rect_i in range(i, i+h):
                    for rect_j in range(j, j+w):
                        rect1 += nums[rect_i][rect_j]
                rect1_pos = [i, j, i+h-1, j+w-1]
                # 정해진 rect1에 대해 가능한 최대 rect2를 구한다.
                max_rect2 = -1000
                for i2 in range(n):
                    for j2 in range(m):
                        if i2 >= rect1_pos[0] and i2 <= rect1_pos[2] and j2 >= rect1_pos[1] and j2 <= rect1_pos[3]:
                            continue
                        for w2 in range(1, m-j2+1):
                            for h2 in range(1, n-i2+1):
                                ok = True
                                rect2 = 0
                                for rect_i2 in range(i2, i2+h2):
                                    for rect_j2 in range(j2, j2+w2):
                                        if rect_i2 >= rect1_pos[0] and rect_i2 <= rect1_pos[2] and rect_j2 >= rect1_pos[1] and rect_j2 <= rect1_pos[3]:
                                            ok = False
                                            break
                                        else:
                                            rect2 += nums[rect_i2][rect_j2]
                                    if not ok:
                                        break
                                if ok and rect2 > max_rect2:
                                    max_rect2 = rect2
                                    rect2_pos = [i2, j2, i2+h2-1, j2+w2-1]
                if rect1 + max_rect2 > total_sum:
                    total_sum = rect1 + max_rect2

print(total_sum)
