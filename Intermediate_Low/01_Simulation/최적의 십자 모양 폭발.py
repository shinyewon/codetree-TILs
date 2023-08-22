# 문제 링크: https://www.codetree.ai/missions/2/problems/best-cross-shape-bomb?utm_source=clipboard&utm_medium=text
# 소요 시간: 42분
n = int(input())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


cnt = 0
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        pair = 0
        dup_nums = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        for r in range(n):
            for c in range(n):
                dup_nums[r][c] = nums[r][c]
        # 폭탄 터지기
        dup_nums[i][j] = 0
        for k in range(1, nums[i][j]):
            for di, dj in zip(dis, djs):
                new_i, new_j = i + di*k, j + dj*k
                if in_range(new_i, new_j):
                    dup_nums[new_i][new_j] = 0
        # 중력
        for col in range(n):
            for row in range(n-1, 0, -1):
                if dup_nums[row][col] == 0:
                    for upRow in range(row-1, -1, -1):
                        if dup_nums[upRow][col] != 0:
                            dup_nums[row][col], dup_nums[upRow][col] = dup_nums[upRow][col], dup_nums[row][col]
                            break

        # 쌍 개수 세기(중복 방지를 위해 오른쪽과 아래만 탐색)
        for r in range(n):
            for c in range(n):
                if dup_nums[r][c] != 0:
                    for di, dj in zip([0, 1], [1, 0]):
                        new_i, new_j = r + di, c + dj
                        if in_range(new_i, new_j) and (dup_nums[r][c] == dup_nums[new_i][new_j]):
                            pair += 1
        if pair > cnt:
            cnt = pair

print(cnt)
