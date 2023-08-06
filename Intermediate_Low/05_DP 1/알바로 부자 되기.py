# 문제 링크: https://www.codetree.ai/missions/2/problems/being-rich-by-working-part-time?utm_source=clipboard&utm_medium=text
n = int(input())
info = [
    list(map(int, input().split()))
    for _ in range(n)
]
# dp[i]는 i번째까지 알바들 중에서, i번째 알바를 포함하여 선택해 벌 수 있는 최대 금액
dp = [0] * n

# dp[i] 값을 채우는 함수


def findDp(i):
    for j in range(i):
        if info[j][1] >= info[i][0]:  # 기간이 겹치면
            dp[i] = max(dp[i], info[i][2])
        else:
            dp[i] = max(dp[i], dp[j]+info[i][2])


dp[0] = info[0][2]
for i in range(1, n):
    findDp(i)

print(max(dp))
