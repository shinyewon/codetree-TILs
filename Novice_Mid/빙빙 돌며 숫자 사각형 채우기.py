# 문제 링크: https://www.codetree.ai/missions/5/problems/snail-number-square?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
arr = [
    [0]*m
    for _ in range(n)
]


def in_range(i, j):
    return 0 <= i and i < n and 0 <= j and j < m


    # R   D  L   U
dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
i, j = 0, 0

for num in range(1, n*m+1):
    arr[i][j] = num
    ni, nj = i + dis[dir_num], j + djs[dir_num]
    if (not in_range(ni, nj)) or arr[ni][nj] != 0:
        dir_num = (dir_num + 1) % 4
        i, j = i + dis[dir_num], j + djs[dir_num]
    else:
        i, j = ni, nj
for k in range(n):
    for l in range(m):
        print(arr[k][l], end=" ")
    print()
