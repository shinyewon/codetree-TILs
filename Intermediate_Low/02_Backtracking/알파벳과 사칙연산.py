# 문제 링크: https://www.codetree.ai/missions/2/problems/calculations-with-alphabet?utm_source=clipboard&utm_medium=text
expr = input()
num = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
Max = 0


def calculate(num):
    global expr
    answer = num[expr[0]]
    for oper_i in range(1, len(expr)-1, +2):
        if expr[oper_i] == '+':
            answer += num[expr[oper_i+1]]
        elif expr[oper_i] == '-':
            answer -= num[expr[oper_i+1]]
        else:
            answer *= num[expr[oper_i+1]]
    return answer


nums = []


def numComb(pos, comb):
    if pos == 7:
        nums.append(comb)
        return
    for i in range(1, 5):
        numComb(pos+1, comb + [i])


def findMax(num):
    global Max
    numComb(1, [])
    for i in range(len(nums)):
        num['a'] = nums[i][0]
        num['b'] = nums[i][1]
        num['c'] = nums[i][2]
        num['d'] = nums[i][3]
        num['e'] = nums[i][4]
        num['f'] = nums[i][5]
        answer = calculate(num)
        if answer > Max:
            Max = answer
    return


findMax(num)
print(Max)
