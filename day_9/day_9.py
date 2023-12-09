def generate_last_el(history):
    history = [int(h) for h in history]

    last_elements = []
    while not set(history) == {0}:
        for i in range(len(history) - 1):
            history[i] = (history[i+1] - history[i])

        last_elements.append(history[-1])
        history = history[:-1]  # remove last element

    return sum(last_elements)


with open('day_9_input.txt', 'r') as f:
    content = f.read()

histories = content.split('\n')
histories = [h.split() for h in histories]

result = 0
for history in histories:
    result += generate_last_el(history)

print(result)

# part 2:


def generate_first_elements_list(history):
    history = [int(h) for h in history]

    first_elements = [history[0]]
    while not set(history) == {0}:
        for i in range(len(history) - 1):
            history[i] = (history[i+1] - history[i])
        first_elements.append(history[0])
        history = history[:-1]  # remove last element

    return first_elements


def generate_prev_el(first_elements_list):
    prev_el = 0
    for el in first_elements_list[::-1]:  # loop backwards
        prev_el = el - prev_el

    return prev_el


result = 0
for history in histories:
    first_elements_list = generate_first_elements_list(history)
    result += generate_prev_el(first_elements_list)

print(result)
