# 문제 링크: https://www.codetree.ai/missions/4/problems/receive-10-inputs?utm_source=clipboard&utm_medium=text
nums = list(map(int, input().split()))
index_0 = 10
sum = 0
for i in range(10):
    sum += nums[i]
    if nums[i] == 0:
        index_0 = i
        break
ave = sum / index_0
print("%d %.1f" % (sum, ave))
