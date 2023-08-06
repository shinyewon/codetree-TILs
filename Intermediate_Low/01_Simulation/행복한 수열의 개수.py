# 문제 링크: https://www.codetree.ai/missions/2/problems/number-of-happy-sequence?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(n)
]
happy = 0
for i in range(n):
    arr[i] = list(map(int, input().split()))
    cnt = 0
    for j in range(n):
        if arr[i][j] == (arr[i][j-1] if j > 1 else arr[i][0]):
            cnt += 1
        else:
            cnt = 1
        if cnt == m:
            happy += 1
            break
for j in range(n):
    cnt = 0
    for i in range(n):
        if arr[i][j] == (arr[i-1][j] if i > 1 else arr[0][j]):
            cnt += 1
        else:
            cnt = 1
        if cnt == m:
            happy += 1
            break
print(happy)
