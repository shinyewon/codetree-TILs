# 문제 링크: https://www.codetree.ai/missions/4/problems/print-square-of-elements?utm_source=clipboard&utm_medium=text
n = int(input())
nums = list(map(int, input().split()))
for i in range(n):
    nums[i] = nums[i] ** 2
    print(nums[i], end=" ")
