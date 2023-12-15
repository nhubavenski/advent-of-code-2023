def calc_hash_value(string):
    current_value = 0

    for char in string:
        char_value = ord(char)
        current_value += char_value

        current_value *= 17

        current_value %= 256
    return current_value


with open('day_15_input.txt', 'r') as f:
    line = f.readline()

result = 0
strings = line.split(',')

for string in strings:
    result += calc_hash_value(string)

print(result)

# part 2:

steps = line.split(',')
boxes = {box_num: {} for box_num in range(256)}

for step in steps:
    if '=' in step:
        label, focal_len = step.split('=')
        box_number = calc_hash_value(label)

        boxes[box_number][label] = focal_len

    elif '-' in step:
        label = step.split('-')[0]
        box_number = calc_hash_value(label)

        if label in boxes[box_number].keys():
            del boxes[box_number][label]

result = 0
for box_num, slots in boxes.items():
    slot_idx = 1
    if slots:
        for focal_len in slots.values():
            result += (box_num + 1) * slot_idx * int(focal_len)
            slot_idx += 1

print(result)
