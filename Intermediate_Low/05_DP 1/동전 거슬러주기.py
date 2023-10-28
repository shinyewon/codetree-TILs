# 문제 링크: https://www.codetree.ai/missions/2/problems/coin-change?&utm_source=clipboard&utm_medium=text
# 소요 시간: 13분 49초

n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [-1 for _ in range(m+1)]
dp[0] = 0  # 해당 금액에서 가능한 최소 동전의 개수


def in_range(i):
    return i >= 0 and i <= m


for i in range(1, m+1):
    for coin in coins:
        if in_range(i-coin) and dp[i-coin] != -1:
            if dp[i] == -1:
                dp[i] = dp[i-coin] + 1
            elif dp[i-coin] + 1 < dp[i]:
                dp[i] = dp[i-coin] + 1

print(dp[m])
