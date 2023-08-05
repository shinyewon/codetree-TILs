n = int(input())
inputs = list(map(int, input().split()))
nums = []
for i in range(1, n+1):
    nums.append(i)
for input in inputs:
    for i in range(len(nums)):
        if nums[i] == input:
            nums.pop(i)
            break
print(nums[0])
