import math
import sys


def isPalindrome(str_array):
    for i in range(math.floor(len(str_array)/2)):
        if str_array[i] != str_array[-1-i]:
            return False
    return True


def hasPalindromesLengthFiveOrSix(str_array):
    str_lengths = [5, 6]
    for str_length in str_lengths:
        for start_index in range(0, len(str_array)+1-str_length):
            if isPalindrome(str_array[start_index:start_index+str_length]):
                # print(str(str_array[start_index:start_index +
                # str_length]) + ": is palindrome")
                return True
            # else:
                # print(str(str_array[start_index:start_index +
                # str_length]) + ": not palindrome")
    return False


test_cases = []
n = (int)(sys.stdin.readline())

for i in range(n):
    a = (str)(sys.stdin.readline()).replace('\n', '')
    case = (str)(sys.stdin.readline()).replace('\n', '')
    test_cases.append(case)

i = 0
for case in test_cases:
    i = i+1

    case_array = [*case]

    possible = False

    number_question_marks = 0
    for digit in case_array:
        if digit == '?':
            number_question_marks += 1

    for test in range(0, 2**number_question_marks):
        binary_string = "{0:b}".format(test).zfill(number_question_marks)
        binary_string_array = [*binary_string]
        current_index = 0
        case_array_copy = case_array.copy()
        for j in range(len(case_array)):
            if case_array[j] == '?':
                case_array_copy[j] = binary_string[current_index]
                current_index += 1
        #print("NEW TEST: " + str(case_array_copy))
        if not hasPalindromesLengthFiveOrSix(case_array_copy):
            possible = True
            break

    if possible:
        print("Case #"+(str)(i) + ": POSSIBLE")
    else:
        print("Case #" + (str)(i) + ": IMPOSSIBLE")
