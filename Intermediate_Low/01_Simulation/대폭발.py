# 문제 링크: https://www.codetree.ai/missions/2/problems/big-explosion?&utm_source=clipboard&utm_medium=text
# 소요 시간: 20분
n, m, r, c = map(int, input().split())
i, j = r - 1, c - 1
bombs = [
    [0 for _ in range(n)]
    for _ in range(n)
]
bombs[i][j] = 1


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
for t in range(1, m+1):
    # 복사
    tmp_bombs = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            tmp_bombs[i][j] = bombs[i][j]

    d = 2**(t - 1)
    for i in range(n):
        for j in range(n):
            if bombs[i][j] == 1:
                for di, dj in zip(dis, djs):
                    new_i, new_j = i + di * d, j + dj * d
                    if in_range(new_i, new_j):
                        tmp_bombs[new_i][new_j] = 1
    for i in range(n):
        for j in range(n):
            bombs[i][j] = tmp_bombs[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        if bombs[i][j] == 1:
            cnt += 1
print(cnt)
