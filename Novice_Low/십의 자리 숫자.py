# 문제 링크: https://www.codetree.ai/missions/4/problems/number-of-tens-digit?utm_source=clipboard&utm_medium=text
nums = list(map(int, input().split()))
counts = [0] * 9
for num in nums:
    if num == 0:
        break
    else:
        ten = num // 10
        if ten != 0:
            counts[ten-1] += 1
for i in range(9):
    print("%d - %d" % (i+1, counts[i]))
