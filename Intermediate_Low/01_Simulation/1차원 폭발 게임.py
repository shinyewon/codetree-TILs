# 문제 링크: https://www.codetree.ai/missions/2/problems/The-1D-bomb-game?utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 16분
n, m = map(int, input().split())
bombs = [
    int(input())
    for _ in range(n)
]
l = len(bombs)
del_i = []
last_b = bombs[0]
cnt = 0
while True:
    for i in range(l):
        if bombs[i] == last_b:
            cnt += 1
        else:
            last_b = bombs[i]
            if cnt >= m:
                del_i.append(i-cnt)
                del_i.append(i-1)
            cnt = 1
        if i == l-1 and cnt >= m:
            del_i.append(i+1-cnt)
            del_i.append(i)

    if len(del_i) == 0:
        break
    else:
        mini_bombs = [bombs[:del_i[0]]]
        for i in range(2, len(del_i), 2):
            mini_bombs.append(bombs[del_i[i-1]+1:del_i[i]])
        mini_bombs.append(bombs[del_i[-1]+1:])
        bombs = []
        for mini in mini_bombs:
            bombs += mini
        l = len(bombs)
        if l == 0:
            break
        del_i = []
        last_b = bombs[0]
        cnt = 0

print(len(bombs))
for bomb in bombs:
    print(bomb)
