# 문제 링크: https://www.codetree.ai/missions/4/problems/multiple-of-numbers?utm_source=clipboard&utm_medium=text
n = int(input())
count = 0
i = 1
nums = list()
while count != 2:
    nums.append(n*i)
    if (n*i) % 5 == 0:
        count += 1
    i += 1
for num in nums:
    print(num, end=" ")
