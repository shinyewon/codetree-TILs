# 문제 링크: https://www.codetree.ai/missions/2/problems/maximum-number-of-jumps?utm_source=clipboard&utm_medium=text
n = int(input())
jumps = list(map(int, input().split()))
# i번째에 도달하기 위한 최대 점프 가능 횟수(단, i번째로 오는게 불가능할 경우 -1)
dp = [-1] * n

# dp[i] 값을 채우는 함수


def findDp(i):
    for j in range(i):
        if jumps[j] < i - j or dp[j] == -1:
            continue
        else:
            dp[i] = max(dp[i], dp[j]+1)


dp[0] = 0
for i in range(1, n):
    findDp(i)

max_jump = 0
for jump_cnt in dp:
    if jump_cnt > max_jump:
        max_jump = jump_cnt
print(max_jump)
