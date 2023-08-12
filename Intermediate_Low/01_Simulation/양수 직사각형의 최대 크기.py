# 문제 링크: https://www.codetree.ai/missions/2/problems/max-area-of-positive-rectangle?utm_source=clipboard&utm_medium=text
# 소요 시간: 20분 39초
n, m = map(int, input().split())
nums = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_size = 0
for i in range(n):
    for j in range(m):
        if nums[i][j] <= 0:
            continue
        else:
            for h in range(1, n-i+1):
                for w in range(1, m-j+1):
                    size = 0
                    isPRect = True
                    for di in range(h):
                        for dj in range(w):
                            if nums[i+di][j+dj] > 0:
                                size += 1
                            else:
                                isPRect = False
                                break
                        if not isPRect:
                            break
                    if isPRect and size > max_size:
                        max_size = size

if max_size == 0:
    print(-1)
else:
    print(max_size)
