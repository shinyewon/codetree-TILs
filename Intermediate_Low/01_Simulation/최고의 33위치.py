# 문제 링크: https://www.codetree.ai/missions/2/problems/best-place-of-33?utm_source=clipboard&utm_medium=text
n = int(input())
max_coin = 0
arr = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    arr[i] = list(map(int, input().split()))


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def num_of_coin(i, j):
    coin = 0
    for k in range(3):
        for l in range(3):
            if in_range(i+k, j+l) and arr[i+k][j+l] == 1:
                coin += 1
    return coin


for i in range(n-2):
    for j in range(n-2):
        coin_cnt = num_of_coin(i, j)
        if coin_cnt > max_coin:
            max_coin = coin_cnt
print(max_coin)
