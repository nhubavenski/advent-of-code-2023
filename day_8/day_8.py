with open('day_8_input.txt', 'r') as f:
    content = f.read()

content = content.split('\n\n')

instructions = [i for i in content[0]]
lines = content[1].split('\n')

map_dict = {}
for line in lines:
    key = line.split(' =')[0]

    left_right = line.split(' =')[1].replace('(', '')
    left_right = left_right.replace(')', '')
    left_right = left_right.replace(',', '')

    left, right = left_right.split()

    map_dict[key] = {'L': left,
                     'R': right}

steps = 0
current_el = 'AAA'
while current_el != 'ZZZ':
    for instruction in instructions:
        current_el = map_dict[current_el][instruction]

        steps += 1

print(steps)

# part 2:
import math


def count_steps(el):
    steps = 0

    while not el.endswith('Z'):
        for instruction in instructions:
            el = map_dict[el][instruction]

            steps += 1

    return steps


start_elements = [key for key in map_dict.keys() if key.endswith('A')]

steps_needed = [count_steps(el) for el in start_elements]

print(math.lcm(*steps_needed))  # least common steps needed
