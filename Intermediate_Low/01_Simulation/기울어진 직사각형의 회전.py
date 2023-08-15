# 문제 링크: https://www.codetree.ai/missions/2/problems/rotate-slanted-rectangle?utm_source=clipboard&utm_medium=text
# 소요 시간: 33분 55초
n = int(input())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c, m1, m2, m3, m4, d = map(int, input().split())
i, j = r-1, c-1
tmp = nums[i][j]

if d == 0:
    ms = [m4, m3, m2, m1-1]
    dis, djs = [-1, -1, 1, 1], [-1, 1, 1, -1]
    for m, di, dj in zip(ms, dis, djs):
        for _ in range(m):
            nums[i][j] = nums[i+di][j+dj]
            i += di
            j += dj
    nums[i][j] = tmp
else:
    ms = [m1, m2, m3, m4-1]
    dis, djs = [-1, -1, 1, 1], [1, -1, -1, 1]
    for m, di, dj in zip(ms, dis, djs):
        for _ in range(m):
            nums[i][j] = nums[i+di][j+dj]
            i += di
            j += dj
    nums[i][j] = tmp

for row in range(n):
    for col in range(n):
        print(nums[row][col], end=" ")
    print()
