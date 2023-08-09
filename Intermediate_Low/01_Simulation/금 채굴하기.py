#문제 링크: https://www.codetree.ai/missions/2/problems/gold-mining?utm_source=clipboard&utm_medium=text
#소요 시간: 1시간
n, m = tuple(map(int, input().split()))
gold = [
    list(map(int, input().split()))
    for _ in range(n)
]
def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n
max_cnt = 0

for k in range(n):
    cost = k * k + (k+1) * (k+1)
    for i in range(n):
        for j in range(n):
            cnt = 0
            for di in range(-k, k+1):     
                for dj in range(-(k-abs(di)), k-abs(di)+1):
                    if in_range(i+di, j+dj) and gold[i+di][j+dj] == 1:
                        cnt += 1
            if cnt * m >= cost and cnt > max_cnt:
                max_cnt = cnt

print(max_cnt)