lines = 211

total_points = 0
for i in range(lines):
    row_input = input()
    winning_cards = row_input.split('|')[0].split(':')[1].split()
    my_cards = row_input.split('|')[1].split()

    matches = [card for card in my_cards if card in winning_cards]

    if not matches:
        continue

    total_points += 2 ** (len(matches)-1)

print(total_points)

# part 2:

cards_dict = {}
for i in range(lines):
    row_input = input()
    card_id = int(row_input.split('|')[0].split(':')[0].split()[1])

    winning_cards = row_input.split('|')[0].split(':')[1].split()
    my_cards = row_input.split('|')[1].split()

    matches = [card for card in my_cards if card in winning_cards]

    cards_dict[card_id] = {'matches': len(matches), 'copies': 1}

for card, info in cards_dict.items():
    for copy in range(1, info['copies'] + 1):
        for match in range(1, info['matches'] + 1):
            cards_dict[card + match]['copies'] += 1

print(sum([card['copies'] for card in cards_dict.values()]))
