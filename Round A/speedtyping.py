import sys


def searchForCharInStrStartingAt(char, string, start):
    for i in range(start, len(string)):
        if (char == string[i]):
            return i
    return -1


test_cases = []
n = (int)(sys.stdin.readline())

for i in range(n):
    str_i = (str)(sys.stdin.readline()).replace('\n', '')
    str_p = (str)(sys.stdin.readline()).replace('\n', '')
    test_cases.append({'str_i': str_i, 'str_p': str_p})

i = 0
for case in test_cases:
    i = i+1
    if len(case['str_i']) > len(case['str_p']):
        print("Case #" + (str)(i) + ": IMPOSSIBLE")
        continue

    last_match = 0
    possible = True

    for j in range(len(case['str_i'])):
        match = searchForCharInStrStartingAt(
            case['str_i'][j], case['str_p'], last_match)

        if match == -1:
            possible = False
            break
        else:
            last_match = match+1

    if possible:
        print("Case #"+(str)(i) + ": "+str
              ((len(case['str_p']) - len(case['str_i']))))
    else:
        print("Case #" + (str)(i) + ": IMPOSSIBLE")
