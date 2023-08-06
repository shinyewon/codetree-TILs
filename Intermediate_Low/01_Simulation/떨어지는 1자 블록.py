# 문제 링크: https://www.codetree.ai/missions/2/problems/falling-horizontal-block?utm_source=clipboard&utm_medium=text
n, m, k = tuple(map(int, input().split()))
k -= 1
arr = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    arr[i] = list(map(int, input().split()))

if n == 1:
    for j in range(k, k+m):
        arr[0][j] = 1

filled = False
for i in range(1, n):
    for j in range(k, k+m):
        if arr[i][j] == 1:
            for j2 in range(k, k+m):
                filled = True
                arr[i-1][j2] = 1
            break
    if filled:
        break

if not filled:
    for j in range(k, k+m):
        arr[n-1][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
