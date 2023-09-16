# 문제 해결 중...
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt = 0


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            pass

print(cnt)
