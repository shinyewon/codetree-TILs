# 문제 링크: https://www.codetree.ai/missions/2/problems/n-permutation?utm_source=clipboard&utm_medium=text
n = int(input())
answer = []
visited = [False] * n


def combination(cnt):
    if cnt == n:
        for elem in answer:
            print(elem, end=" ")
        print()
        return
    for num in range(1, n+1):
        if visited[num-1] == True:
            continue
        visited[num-1] = True
        answer.append(num)

        combination(cnt+1)

        visited[num-1] = False
        answer.pop()


combination(0)
