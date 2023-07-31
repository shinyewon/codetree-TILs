# 문제 링크: https://www.codetree.ai/missions/2/problems/n-permutations-of-k-with-repetition?utm_source=clipboard&utm_medium=text
k, n = map(int, input().split())
answer = []


def combination(n):
    if n == 0:
        for elem in answer:
            print(elem, end=" ")
        print()
        return
    for num in range(1, k+1):
        answer.append(num)
        combination(n-1)
        answer.pop()


combination(n)
