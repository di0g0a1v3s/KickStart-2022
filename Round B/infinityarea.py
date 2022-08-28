import math
import sys

test_cases = []
n = (int)(sys.stdin.readline())

for i in range(n):
    str_i = (str)(sys.stdin.readline()).replace('\n', '')
    str_split = str_i.split(" ")
    R = str_split[0]
    A = str_split[1]
    B = str_split[2]
    test_cases.append({'R': int(R), 'A': int(A), 'B': int(B)})

i = 0
for case in test_cases:
    i = i+1
    radiuses = []

    radius = case['R']
    radiuses.append(case['R'])

    while True:
        radius = math.floor(radius*case['A'])
        if radius == 0:
            break
        radiuses.append(radius)

        radius = math.floor(radius/case['B'])
        if radius == 0:
            break
        radiuses.append(radius)

    sum_areas = 0
    # print(radiuses)
    for radius in radiuses:
        sum_areas += radius*radius

    sum_areas = sum_areas*math.pi

    print("Case #" + (str)(i) + ": {:.6f}".format(sum_areas))
