def add_new_rows(matrix):
    new_matrix = []
    for row in matrix:
        if '#' not in row:
            new_matrix.append(row)
        new_matrix.append(row)

    return new_matrix


def find_galaxies(matrix):
    galaxies = []
    for row_id in range(len(matrix)):
        for col_id in range(len(matrix[row_id])):
            el = matrix[row_id][col_id]

            if el == '#':
                galaxies.append((row_id, col_id))

    return galaxies


def calc_distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2

    distance = abs(x1 - x2) + abs(y1 - y2)

    return distance


matrix = []
with open('day_11_input.txt', 'r') as f:
    for line in f.readlines():
        matrix.append([i for i in line.strip()])

matrix_rows_added = add_new_rows(matrix)

transposed_matrix = list(map(list, zip(*matrix_rows_added)))
transposed_matrix_rows_added = add_new_rows(transposed_matrix)

matrix_expanded = list(map(list, zip(*transposed_matrix_rows_added)))

galaxies = find_galaxies(matrix_expanded)

all_distances = []
while galaxies:
    distances = []
    current_galaxy = galaxies.pop()

    for galaxy in galaxies:
        distances.append(calc_distance(current_galaxy, galaxy))

    all_distances.extend(distances)

print(sum(all_distances))

# part 2:


def get_empty_rows_ids(matrix):
    empty_rows_ids = []
    for row_id in range(len(matrix)):
        if '#' not in matrix[row_id]:
            empty_rows_ids.append(row_id)

    return empty_rows_ids


def calc_distance_after_expand(point_1, point_2, expansion_number):
    x1, y1 = point_1
    x2, y2 = point_2

    x_distance = abs(x1 - x2)
    y_distance = abs(y1 - y2)

    for x in range(min(x1, x2), max(x1, x2)):
        if x in empty_rows_ids:
            x_distance += expansion_number-1

    for y in range(min(y1, y2), max(y1, y2)):
        if y in empty_cols_ids:
            y_distance += expansion_number-1

    distance = x_distance + y_distance

    return distance


empty_rows_ids = get_empty_rows_ids(matrix)

transposed_matrix = list(map(list, zip(*matrix)))

empty_cols_ids = get_empty_rows_ids(transposed_matrix)

galaxies = find_galaxies(matrix)

all_distances = []
while galaxies:
    distances = []
    current_galaxy = galaxies.pop()

    for galaxy in galaxies:
        distances.append(calc_distance_after_expand(current_galaxy, galaxy, 1000000))

    all_distances.extend(distances)

print(sum(all_distances))
