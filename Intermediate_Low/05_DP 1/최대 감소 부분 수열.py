# 문제 링크: https://www.codetree.ai/missions/2/problems/longest-decreasing-subsequence?utm_source=clipboard&utm_medium=text
n = int(input())
nums = list(map(int, input().split()))
# dp[i]는 i번째까지 수열 중 i번째를 포함한 최대 감소 부분 수열의 길이
dp = [1] * n

# dp[i] 값을 채우는 함수


def findDp(i):
    for j in range(i):
        if nums[j] <= nums[i]:
            continue
        else:
            dp[i] = max(dp[i], dp[j]+1)


for i in range(1, n):
    findDp(i)

max_l = 0
for length in dp:
    if length > max_l:
        max_l = length
print(max_l)
