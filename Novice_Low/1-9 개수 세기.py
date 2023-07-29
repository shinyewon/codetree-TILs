# 문제 링크: https://www.codetree.ai/missions/4/problems/count-one-to-nine?utm_source=clipboard&utm_medium=text
n = int(input())
nums = list(map(int, input().split()))
counts = [0 for _ in range(9)]
for num in nums:
    counts[num-1] += 1
for count in counts:
    print(count)
