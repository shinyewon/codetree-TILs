# 문제 링크: https://www.codetree.ai/missions/2/problems/minimax-path-in-square?utm_source=clipboard&utm_medium=text
n = int(input())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [1000001 for _ in range(n)]
    for _ in range(n)
]
dp[0][0] = nums[0][0]


def initialize():
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], nums[0][j])
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], nums[i][0])


initialize()

dis, djs = [0, -1], [-1, 0]
for i in range(1, n):
    for j in range(1, n):
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            dp[i][j] = min(max(dp[new_i][new_j], nums[i][j]), dp[i][j])

print(dp[n-1][n-1])
