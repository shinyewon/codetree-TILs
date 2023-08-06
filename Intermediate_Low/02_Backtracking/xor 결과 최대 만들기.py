# 문제 링크: https://www.codetree.ai/missions/2/problems/max-of-xor?utm_source=clipboard&utm_medium=text
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
maximum = 0


def XOR(n, m, nums, xor):
    global maximum
    if m == 0:
        if xor > maximum:
            maximum = xor
    for i in range(0, len(nums)):
        XOR(n, m-1, nums[i+1:], xor ^ nums[i])


XOR(n, m, nums, 0)
print(maximum)
