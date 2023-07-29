# 문제 링크: https://www.codetree.ai/missions/4/problems/filling-array?utm_source=clipboard&utm_medium=text
nums = list(map(int, input().split()))
index_0 = 10
for i in range(10):
    if nums[i] == 0:
        index_0 = i
        break
for i in range(index_0-1, -1, -1):
    print(nums[i], end=" ")
