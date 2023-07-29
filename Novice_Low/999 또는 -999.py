# 문제 링크: https://www.codetree.ai/missions/4/problems/999-or-999?utm_source=clipboard&utm_medium=text
nums = list(map(int, input().split()))
end_i = 100
for i in range(len(nums)):
    if nums[i] == -999 or nums[i] == 999:
        end_i = i
        break
m = min(nums[:i])
M = max(nums[:i])
print(M, m)
