import math
import sys

from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def isPalindrome(str_array):
    # print(str(str_array))
    for i in range(math.floor(len(str_array)/2)):
        if str_array[i] != str_array[-1-i]:
            return False
    return True


test_cases = []
n = (int)(sys.stdin.readline())

for i in range(n):
    case = (int)(sys.stdin.readline())
    test_cases.append(case)

i = 0
for case in test_cases:
    i = i+1

    sum = 0
    for j in factors(case):
        if isPalindrome([*str(j)]):
            sum += 1

    print("Case #" + (str)(i) + ": " + str(sum))
