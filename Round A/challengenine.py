import sys


def sumDigitsInN(N):
    sum = 0
    for digit in N:
        sum = sum + int(digit)
    return sum


def isDivisibleByNine(n):
    return n % 9 == 0


def findNextMultipleOfNine(n):
    for i in range(9):
        if isDivisibleByNine(n+i):
            return i


test_cases = []
n = int(sys.stdin.readline())


for i in range(n):
    N = str(int(sys.stdin.readline()))
    test_cases.append(N)

k = 0
for N in test_cases:
    k = k+1
    N_array = [*N]
    # if the sum of digits of the number is divisible by 9, then the number itself is divisible by 9
    sum_of_digits = sumDigitsInN(N_array)
    digit_to_add = findNextMultipleOfNine(sum_of_digits)

    assigned = False
    result = 0
    for i in range(len(N_array)):
        if digit_to_add < int(N_array[i]):
            option_arr = N_array[0:i] + [str(digit_to_add)] + N_array[i:]
            option = ''.join(option_arr)

            if (option[0] != '0'):
                result = option
                assigned = True
                break
    if not assigned:
        option_arr = N_array[:] + [str(digit_to_add)]
        result = ''.join(option_arr)

    print("Case #" + (str)(k) + ": " + str(result))
