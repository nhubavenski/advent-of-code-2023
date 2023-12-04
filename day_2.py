def is_game_possible(game):
    all_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for reveal in game:
        reveal_cubes = reveal.split(', ')
        for reveal_cube in reveal_cubes:
            colour = reveal_cube.split()[1]
            count = int(reveal_cube.split()[0])
            if count > all_cubes[colour]:
                print(f'not possible - too much {colour}')
                return False
    return True


games = {}

print("Enter/Paste your content:")
while True:
    line = input()
    if line == 'end':
        break

    game_id = line.split(':')[0].replace('Game ', '')
    game_info = line.split(': ')[1]
    revealed_sets = game_info.split('; ')

    games[game_id] = revealed_sets


possible_gammes_ids = []
for game_id, game in games.items():
    if is_game_possible(game):
        possible_gammes_ids.append(int(game_id))

print(f'Sum of the ids: {sum(possible_gammes_ids)}')


# part 2:
def calc_fewest_poss_cubes(game):
    fewest_possible_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    power = 1

    for reveal in game:
        reveal_cubes = reveal.split(', ')
        for reveal_cube in reveal_cubes:
            colour = reveal_cube.split()[1]
            count = int(reveal_cube.split()[0])

            if count > fewest_possible_cubes[colour]:
                fewest_possible_cubes[colour] = count

    for value in fewest_possible_cubes.values():
        power *= value

    return power


total_power = 0

for game in games.values():
    game_power = calc_fewest_poss_cubes(game)

    total_power += game_power

print(f'total_power: {total_power}')
