# 문제 링크: https://www.codetree.ai/missions/2/problems/conveyor-belt?utm_source=clipboard&utm_medium=text
n, t = tuple(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(2)
]

arr[0] = list(map(int, input().split()))
arr[1] = list(map(int, input().split()))

for _ in range(t):  # t번 rotate
    i, j = 0, n-1
    tmp = arr[i][j]
    for _ in range(n-1):
        arr[i][j] = arr[i][j-1]
        j -= 1
    arr[i][j] = arr[1][n-1]
    i, j = 1, n-1
    for _ in range(n-1):
        arr[i][j] = arr[i][j-1]
        j -= 1
    arr[i][j] = tmp

for i in range(2):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
