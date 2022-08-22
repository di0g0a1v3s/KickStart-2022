import sys


def isInteresting(n):
    n_array = [*(str(n))]
    sum_digits = 0
    mult_digits = 1
    for digit in n_array:
        if digit == '0':
            return True
        sum_digits = sum_digits+int(digit)
        mult_digits = mult_digits*int(digit)
    if mult_digits % sum_digits == 0:
        return True


test_cases = []
n = int(sys.stdin.readline())


for i in range(n):
    line = sys.stdin.readline()
    line_split = line.split(" ")
    A = line_split[0]
    B = line_split[1]
    test_cases.append({'A': A, 'B': B})

k = 0
for case in test_cases:
    k = k+1
    sum = 0
    for i in range(int(case['A']), int(case['B'])+1):
        if isInteresting(i):
            sum = sum+1
    print("Case #" + (str)(k) + ": " + str(sum))
