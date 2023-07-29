# 문제 링크: https://www.codetree.ai/missions/4/problems/sum-of-10-elements?utm_source=clipboard&utm_medium=text
arr = input().split()
sum = 0
for i in range(len(arr)):
    sum += int(arr[i])
print(sum)
