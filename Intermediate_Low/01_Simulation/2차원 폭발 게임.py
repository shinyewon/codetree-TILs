# 문제 링크: https://www.codetree.ai/missions/2/problems/The-2D-bomb-game?utm_source=clipboard&utm_medium=text
# 소요 시간: 2시간 14분
n, m, k = map(int, input().split())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]


def gravity():
    for j in range(n):
        for i in range(n-1, -1, -1):
            if nums[i][j] == 0:
                for row in range(i-1, -1, -1):
                    if nums[row][j] != 0:
                        nums[row][j], nums[i][j] = nums[i][j], nums[row][j]
                        break


def baam():
    baam = 0
    for j in range(n):
        last_num = nums[0][j]
        cnt = 1
        bombs = [0]
        for i in range(1, n):
            if last_num == nums[i][j]:
                cnt += 1
                bombs.append(i)
            else:
                if cnt >= m and last_num != 0:
                    for row in bombs:
                        nums[row][j] = 0
                    baam += 1
                last_num = nums[i][j]
                cnt = 1
                bombs = [i]
        if cnt >= m and last_num != 0:
            for row in bombs:
                nums[row][j] = 0
            baam += 1
    return baam


for _ in range(k):
    while baam():
        gravity()
    # 90도 회전 i j => ? n-1-i
    tmp_nums = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n-1, -1, -1):
            if nums[i][j] != 0:
                for r in range(n-1, -1, -1):
                    if tmp_nums[r][n-1-i] == 0:
                        tmp_nums[r][n-1-i] = nums[i][j]
                        break
    nums = tmp_nums

while baam():
    gravity()

# 남은 폭탄 개수 계산 및 출력
res = 0
for i in range(n):
    for j in range(n):
        if nums[i][j] != 0:
            res += 1
print(res)
