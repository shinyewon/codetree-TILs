# 문제 링크: https://www.codetree.ai/missions/2/problems/n-choose-m?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
answer = []


def choose(cnt, last_num):
    if cnt == m+1:
        for elem in answer:
            print(elem, end=" ")
        print()
        return
    for num in range(last_num, n+1):
        answer.append(num)
        choose(cnt+1, num+1)
        answer.pop()


choose(1, 1)
