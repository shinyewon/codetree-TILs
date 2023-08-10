# 문제 링크: https://www.codetree.ai/missions/2/problems/slanted-rectangle?utm_source=clipboard&utm_medium=text
# 소요 시간: 2시간
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dis, djs = [-1, -1, 1, 1], [1, -1, -1, 1]
max_sum = 0
for i in range(2, n):
    for j in range(1, n-1):
        init_i, init_j = i, j
        for w in range(1, init_i):
            for h in range(1, min(init_i-w+1, init_j+1)):
                num_sum = grid[i][j]
                for di, dj in zip(dis, djs):
                    if (di == -1 and dj == 1) or (di == 1 and dj == -1):
                        l = w
                    else:
                        l = h

                    for _ in range(l):
                        new_i, new_j = i + di, j + dj
                        if in_range(new_i, new_j) and new_i != init_i:
                            i, j = new_i, new_j
                            num_sum += grid[i][j]

                if num_sum > max_sum:
                    max_sum = num_sum
                i, j = init_i, init_j

print(max_sum)
