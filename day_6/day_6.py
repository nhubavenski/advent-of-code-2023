def calculate_better_distance(time, record_distance):
    better_distances = []
    for speed in range(time+1):
        distance = (time-speed)*speed
        if distance > record_distance:
            better_distances.append(distance)

    return len(better_distances)


with open('day_6_input.txt', 'r') as f:
    content = f.read()

times = content.split('\n')[0].split(':')[1].split()
record_distances = content.split('\n')[1].split(':')[1].split()

times = [int(t) for t in times]
record_distances = [int(d) for d in record_distances]

dictionary = dict(zip(times, record_distances))

result = 1
for time, record_distance in dictionary.items():
    result *= calculate_better_distance(time, record_distance)

print(result)

# part 2:

time = int(''.join(content.split('\n')[0].split(':')[1].split()))
record_distance = int(''.join(content.split('\n')[1].split(':')[1].split()))

better_dist_count = calculate_better_distance(time, record_distance)
print(better_dist_count)
