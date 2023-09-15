n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt = 0


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


print(cnt)
