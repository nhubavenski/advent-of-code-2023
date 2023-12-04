def is_inside_of_matrix(curr_row_idx, curr_col_idx, matrix_rows_len, matrix_cols_len):
    if curr_row_idx < 0 or curr_col_idx < 0 or curr_row_idx > matrix_rows_len - 1 or curr_col_idx > matrix_cols_len - 1:
        return False
    return True


def get_adjacent_cells_coordinates(row_idx, col_idx):
    adj_cells_coordinates = [
        (row_idx - 1, col_idx - 1), (row_idx - 1, col_idx), (row_idx - 1, col_idx + 1),  # prev row
        (row_idx, col_idx - 1), (row_idx, col_idx + 1),  # current row
        (row_idx + 1, col_idx - 1), (row_idx + 1, col_idx), (row_idx + 1, col_idx + 1)  # next row
    ]

    return adj_cells_coordinates


matrix = []
size = 140

for i in range(size):
    row_input = input()
    matrix.append([])

    for el in row_input:
        matrix[i].append(el)

valid_numbers = []
valid_numbers_coordinates = []

for row_id in range(len(matrix)):
    number = ''
    num_coordinates = []
    is_whole_number_valid = False

    for col_id in range(len(matrix[row_id])):
        el = matrix[row_id][col_id]

        adj_cells_coord = get_adjacent_cells_coordinates(row_id, col_id)
        adj_cells_coord = [cell_c for cell_c in adj_cells_coord if is_inside_of_matrix(*cell_c, size, size)]

        adj_cells_elements = [matrix[cell_c[0]][cell_c[1]] for cell_c in adj_cells_coord]
        adj_cells_symbols = [cell for cell in adj_cells_elements if not cell.isdigit() and cell != '.']

        if el.isdigit():
            number += el
            num_coordinates.append((row_id, col_id))

            if adj_cells_symbols:
                is_whole_number_valid = True

        else:
            if number and is_whole_number_valid:
                valid_numbers.append(number)
                valid_numbers_coordinates.append(num_coordinates)
            number = ''
            num_coordinates = []
            is_whole_number_valid = False

    if number and is_whole_number_valid:  # if row ends with digit
        valid_numbers.append(number)
        valid_numbers_coordinates.append(num_coordinates)
print(f'result: {sum([int(i) for i in valid_numbers])}')


# part 2:

def count_adj_valid_numbers(adjacent_digits_coordinates, valid_numbers_coordinates):
    count = 0
    for coord_list in valid_numbers_coordinates:
        for coordinates in coord_list:
            if coordinates in adjacent_digits_coordinates:
                count += 1
    return count


def get_adj_valid_numbers_product(adj_digits_coord, valid_numbers_coordinates):
    gears = []
    output = 1

    for coord_list in valid_numbers_coordinates:
        for coordinates in coord_list:
            if coordinates in adj_digits_coord:
                if coord_list not in gears:
                    gears.append(coord_list)

    if len(gears) == 2:
        for gear in gears:
            num = ''
            for n in gear:
                num += matrix[n[0]][n[1]]
            output *= int(num)
        return output
    return 0


output = 0
for row_id in range(len(matrix)):
    for col_id in range(len(matrix[row_id])):
        el = matrix[row_id][col_id]

        adj_cells_coord = get_adjacent_cells_coordinates(row_id, col_id)
        adj_cells_coord = [cell_c for cell_c in adj_cells_coord if is_inside_of_matrix(*cell_c, size, size)]

        adj_digits_coord = [cell_c for cell_c in adj_cells_coord if matrix[cell_c[0]][cell_c[1]].isdigit()]

        if el == '*':
            output += get_adj_valid_numbers_product(adj_digits_coord, valid_numbers_coordinates)

print(f'result: {output}')
