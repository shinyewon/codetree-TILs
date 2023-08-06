# 문제 링크: https://www.codetree.ai/missions/2/problems/rectangle-fill?utm_source=clipboard&utm_medium=text
n = int(input())
rect = [
    [0 for _ in range(n)]
    for _ in range(2)
]
dp = [0 for _ in range(n+1)]
dp[1] = 1
if n >= 2:
    dp[2] = 2
    if n >= 3:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
