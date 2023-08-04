# 문제 링크: https://www.codetree.ai/missions/2/problems/backward-permutation?utm_source=clipboard&utm_medium=text
n = int(input())
nums = []
for i in range(n, 0, -1):
    nums.append(i)


def dfs(pos, nums, arr):
    global n
    if pos == n:
        for num in arr:
            print(num, end=" ")
        print()
    for i in range(len(nums)):
        dfs(pos+1, nums[:i]+nums[i+1:], arr+[nums[i]])


dfs(0, nums, [])
