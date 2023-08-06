# 문제 링크: https://www.codetree.ai/missions/2/problems/conveyor-belt-triangle?utm_source=clipboard&utm_medium=text
n, t = map(int, input().split())
arr = [
    [0] * n
    for _ in range(3)
]
for i in range(3):
    arr[i] = list(map(int, input().split()))

for _ in range(t):
    tmp = arr[2][n-1]
    for i in range(2, -1, -1):
        for j in range(n-1, 0, -1):
            arr[i][j] = arr[i][j-1]
        arr[i][0] = (arr[i-1][n-1] if i >= 1 else tmp)

for i in range(3):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
