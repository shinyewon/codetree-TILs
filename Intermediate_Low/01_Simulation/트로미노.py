# 문제 링크: https://www.codetree.ai/missions/2/problems/tromino?utm_source=clipboard&utm_medium=text
# 소요 시간: 25분, 수행시간: O(nm)
n, m = tuple(map(int, input().split()))
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_sum = 0
# ㄴ자 블록에 대해 최댓값 구하기
dis, djs = [0, 1, 1], [1, 0, 1]
for i in range(n-1):
    for j in range(m-1):
        nums4 = [nums[i][j]]
        sum4 = nums[i][j]
        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            nums4.append(nums[new_i][new_j])
            sum4 += nums[new_i][new_j]
        sum4 -= min(nums4)
        if sum4 > max_sum:
            max_sum = sum4

# ㅡ자 블록에 대해 최댓값 구하기
for i in range(n):
    for sj in range(m-2):
        row_sum = 0
        for j in range(sj, sj+3):
            row_sum += nums[i][j]
        if row_sum > max_sum:
            max_sum = row_sum
for j in range(m):
    for si in range(n-2):
        col_sum = 0
        for i in range(si, si+3):
            col_sum += nums[i][j]
        if col_sum > max_sum:
            max_sum = col_sum

print(max_sum)
