# 문제 링크: https://www.codetree.ai/missions/4/problems/filling-array-and-print?utm_source=clipboard&utm_medium=text
arr = input().split()
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end="")
