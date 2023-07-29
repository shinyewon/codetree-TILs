# 문제 링크: https://www.codetree.ai/missions/4/problems/find-specific-location-of-array-4?utm_source=clipboard&utm_medium=text
nums = list(map(int, input().split()))
index_0 = 10
count = 0
even_sum = 0
for i in range(10):
    if nums[i] == 0:
        index_0 = i
        break
    elif nums[i] % 2 == 0:
        count += 1
        even_sum += nums[i]
ave = even_sum / index_0
print("%d %d" % (count, even_sum))
