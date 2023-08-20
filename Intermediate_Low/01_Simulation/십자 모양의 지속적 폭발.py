# 문제 링크: https://www.codetree.ai/missions/2/problems/cross-shape-continuous-bomb?utm_source=clipboard&utm_medium=text
# 소요 시간: 13분
n, m = map(int, input().split())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dis, djs = [-1, 0, 1, 0], [0, 1, 0, -1]
for _ in range(m):
    j = int(input()) - 1
    bomb, bomb_i, bomb_j = 0, 0, 0
    for i in range(n):
        if nums[i][j] != 0:
            bomb = nums[i][j]
            bomb_i, bomb_j = i, j
            nums[i][j] = 0
            break
    # 폭탄 터지기
    for k in range(1, bomb):
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di*k, j + dj*k
            if in_range(new_i, new_j):
                nums[new_i][new_j] = 0
    # 중력 작용
    for j in range(n):
        for i in range(n-1, 0, -1):
            if nums[i][j] == 0:
                nums[i][j], nums[i-1][j] = nums[i-1][j], nums[i][j]

for i in range(n):
    for j in range(n):
        print(nums[i][j], end=" ")
    print()
