# 문제 링크: https://www.codetree.ai/missions/2/problems/fibonacci-number?utm_source=clipboard&utm_medium=text
n = int(input())
memo = [-1] * (n+1)


def fibo(n):
    if memo[n] != -1:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


print(fibo(n))
