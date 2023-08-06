# 문제 링크: https://www.codetree.ai/missions/2/problems/climbing-stairs?utm_source=clipboard&utm_medium=text
n = int(input())
dp = [0 for _ in range(n+1)]
if n >= 2:
    dp[2] = 1
    if n >= 3:
        dp[3] = 1
for i in range(4, n+1):
    if dp[i-2] != 0:
        dp[i] = dp[i-2]
    if dp[i-3] != 0:
        dp[i] += dp[i-3]

print(dp[n] % 10007 if dp[n] != 0 else 0)
