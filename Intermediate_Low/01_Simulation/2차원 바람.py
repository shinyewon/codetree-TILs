# 문제 링크: https://www.codetree.ai/missions/2/problems/The-2D-wind-blows?utm_source=clipboard&utm_medium=text
# 소요 시간: 35분
n, m, q = map(int, input().split())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    i1, j1, i2, j2 = r1-1, c1-1, r2-1, c2-1
    # 시계 방향으로 회전
    tmp = nums[i1][j1]
    for i in range(i1+1, i2+1):
        nums[i-1][j1] = nums[i][j1]
    for j in range(j1, j2):
        nums[i2][j] = nums[i2][j+1]
    for i in range(i2, i1, -1):
        nums[i][j2] = nums[i-1][j2]
    for j in range(j2, j1, -1):
        nums[i1][j] = nums[i1][j-1]
    nums[i1][j1+1] = tmp

    # 평균값으로 바꾸기
    tmp_nums = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

    def in_range(i, j):
        return i >= 0 and i < n and j >= 0 and j < m
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            num_sum = nums[i][j]
            cnt = 1
            for di, dj in zip(dis, djs):
                new_i, new_j = i + di, j + dj
                if in_range(new_i, new_j):
                    num_sum += nums[new_i][new_j]
                    cnt += 1
            tmp_nums[i][j] = num_sum // cnt
    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            nums[i][j] = tmp_nums[i][j]

for i in range(n):
    for j in range(m):
        print(nums[i][j], end=" ")
    print()
