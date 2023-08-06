# 문제 링크: https://www.codetree.ai/missions/2/problems/move-to-larger-adjacent-cell?utm_source=clipboard&utm_medium=text
n, r, c = tuple(map(int, input().split()))
visited = []
arr = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    arr[i] = list(map(int, input().split()))
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


i, j = r-1, c-1

visited.append(arr[i][j])
while True:
    move = False
    for di, dj in zip(dis, djs):
        ni, nj = i + di, j + dj
        if in_range(ni, nj) and arr[ni][nj] > arr[i][j]:
            i, j = ni, nj
            visited.append(arr[i][j])
            move = True
        if move:
            break
    if not move:
        break

for num in visited:
    print(num, end=" ")
