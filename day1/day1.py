import numpy as np
left_list = []
right_list = []

with open('input.txt') as file:
    for line in file:
        left_list.append(int(line.split('   ')[0]))
        right_list.append(int(line.split('   ')[1]))

#part 1
distance = []
left_list.sort()
right_list.sort()

for i in range(0, len(left_list)):
    distance.append(abs(left_list[i] - right_list[i]))

print(sum(distance))

#part 2
score = 0

for i in left_list:
    ii = np.where(np.array(right_list) == i)[0]
    score += i * len(ii)

print(score)