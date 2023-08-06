# 문제 링크: https://www.codetree.ai/missions/2/problems/jenga-1d?utm_source=clipboard&utm_medium=text
n = int(input())
nums = [0] * n
tmp_nums = [0] * n

for i in range(n):
    nums[i] = int(input())

for _ in range(2):
    s, e = map(int, input().split())
    tmp_nums = [0] * (n-(e-s+1))
    tmp_i = 0
    for i in range(n):
        if i < s-1 or i > e-1:
            tmp_nums[tmp_i] = nums[i]
            tmp_i += 1
    nums = tmp_nums
    n = n - (e-s+1)

print(len(nums))
for i in range(n):
    print(nums[i])
