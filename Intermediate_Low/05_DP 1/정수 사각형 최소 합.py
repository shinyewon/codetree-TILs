# 문제 링크: https://www.codetree.ai/missions/2/problems/minimum-sum-path-in-square?utm_source=clipboard&utm_medium=text
n = int(input())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [-1 for _ in range(n)]
    for _ in range(n)
]
dp[0][n-1] = nums[0][n-1]


def initialize():
    for j in range(n-1, 0, -1):
        dp[0][j-1] = dp[0][j] + nums[0][j-1]
    for i in range(n-1):
        dp[i+1][n-1] = dp[i][n-1] + nums[i+1][n-1]


initialize()

dis, djs = [0, -1], [1, 0]
for i in range(1, n):
    for j in range(n-2, -1, -1):
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            if dp[i][j] == -1:
                dp[i][j] = dp[new_i][new_j] + nums[i][j]
            else:
                dp[i][j] = min([dp[i][j], dp[new_i][new_j] + nums[i][j]])

print(dp[n-1][0])
