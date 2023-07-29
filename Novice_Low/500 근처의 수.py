# 문제 링크: https://www.codetree.ai/missions/4/problems/near-500?utm_source=clipboard&utm_medium=text
nums = list(map(int, input().split()))
nums.sort()
sNums = []
lNums = []
for num in nums:
    if num < 500:
        sNums.append(num)
    elif num > 500:
        lNums.append(num)
print(max(sNums), min(lNums))
