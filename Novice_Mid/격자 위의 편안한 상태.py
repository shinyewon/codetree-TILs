# 문제 링크: https://www.codetree.ai/missions/5/problems/comfortable-state-on-the-grid?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(n)
]
dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


for _ in range(m):
    isComft = 0
    r, c = tuple(map(int, input().split()))
    arr[r-1][c-1] = 1
    colored = 0
    for dx, dy in zip(dxs, dys):
        if in_range(r-1+dx, c-1+dy) and arr[r-1+dx][c-1+dy] == 1:
            colored += 1
    if colored == 3:
        isComft = 1
    print(isComft)
