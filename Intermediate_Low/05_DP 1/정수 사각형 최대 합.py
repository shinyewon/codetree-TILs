# 문제 링크: https://www.codetree.ai/missions/2/problems/maximum-sum-path-in-square?utm_source=clipboard&utm_medium=text
n = int(input())
a = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0] * n
    for _ in range(n)
]


def initialize(n):
    dp[0][0] = a[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + a[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + a[0][j]


def fillDp(n):
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + a[i][j]


initialize(n)
fillDp(n)
print(dp[n-1][n-1])
