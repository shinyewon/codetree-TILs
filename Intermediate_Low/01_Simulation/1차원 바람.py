# 문제 링크: https://www.codetree.ai/missions/2/problems/The-1D-wind-blows?utm_source=clipboard&utm_medium=text
# 소요 시간: 45분
n, m, q = map(int, input().split())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]


def shiftL(i):
    tmp = nums[i][0]
    for j in range(1, m):
        nums[i][j-1] = nums[i][j]
    nums[i][m-1] = tmp


def shiftR(i):
    tmp = nums[i][m-1]
    for j in range(m-2, -1, -1):
        nums[i][j+1] = nums[i][j]
    nums[i][0] = tmp


def can_go(i, i2):
    for j in range(m):
        if nums[i][j] == nums[i2][j]:
            return True
    return False


for _ in range(q):
    r, d = input().split()
    i = int(r) - 1
    init_d = d
    if d == 'L':
        shiftR(i)
    else:
        shiftL(i)
    for i2 in range(i-1, -1, -1):
        if can_go(i, i2):
            if d == 'L':
                d = 'R'
                shiftL(i2)
            else:
                d = 'L'
                shiftR(i2)
            i -= 1
        else:
            break
    i = int(r) - 1
    d = init_d
    for i2 in range(i+1, n):
        if can_go(i, i2):
            if d == 'L':
                d = 'R'
                shiftL(i2)
            else:
                d = 'L'
                shiftR(i2)
            i += 1
        else:
            break

for i in range(n):
    for j in range(m):
        print(nums[i][j], end=" ")
    print()
