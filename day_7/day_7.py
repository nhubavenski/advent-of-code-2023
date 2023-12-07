def calc_strength(hand):
    cards = [card for card in hand]
    unique_cards = list(set(cards))

    if len(unique_cards) == 1:  # five of a kind
        return 6

    if len(unique_cards) == 2:
        if cards.count(unique_cards[0]) == 4 or cards.count(unique_cards[1]) == 4:  # four of a kind
            return 5
        return 4   # full house

    if len(unique_cards) == 3:  # three of a kind
        if 3 in [cards.count(unique_card) for unique_card in unique_cards]:
            return 3
        return 2  # two pairs

    if len(unique_cards) == 4:  # one pair
        return 1

    return 0  # high card


def change_hand_cards(hand):
    hand_cards = [card for card in hand]
    hand_cards_changed = []
    for card in hand_cards:
        if card in cards_strength:
            hand_cards_changed.append(cards_strength[card])
        else:
            hand_cards_changed.append(card)
    return hand_cards_changed


def custom_sort(item):
    return tuple(map(int, item[1]))


def read_data(file):
    with open(file, 'r') as f:
        content = f.read()

    content = content.split('\n')

    hands = [c.split()[0] for c in content]
    hands_bids = [c.split()[1] for c in content]
    hands_bids = [int(bid) for bid in hands_bids]

    hands_bids_dict = dict(zip(hands, hands_bids))

    return hands, hands_bids_dict


hands, hands_bids_dict = read_data('day_7_input.txt')

cards_strength = {'A': '14',
                  'K': '13',
                  'Q': '12',
                  'J': '11',
                  'T': '10'}

hands_strength_dict = {}
for hand in hands:
    hands_strength_dict[hand] = [calc_strength(hand)]

    hands_strength_dict[hand].extend(change_hand_cards(hand))

sorted_hands = dict(sorted(hands_strength_dict.items(), key=custom_sort))

result = 0
rank = 1
for hand in sorted_hands.keys():
    result += hands_bids_dict[hand] * rank
    rank += 1

print(result)


# part 2:


def replace_jokers_in_hand(hand):
    cards = [card for card in hand]

    no_jokers_cards = [card for card in cards if card != 'J']

    if no_jokers_cards:
        most_common_card = max(set(no_jokers_cards), key=no_jokers_cards.count)
    else:
        most_common_card = 'J'

    for i in range(len(cards)):
        if cards[i] == 'J':
            cards[i] = most_common_card

    return ''.join(cards)


hands, hands_bids_dict = read_data('day_7_input.txt')

cards_strength['J'] = '0'

hands_strength_dict = {}

for hand in hands:
    hand_replaced_jokers = replace_jokers_in_hand(hand)
    hands_strength_dict[hand] = [calc_strength(hand_replaced_jokers)]

    hands_strength_dict[hand].extend(change_hand_cards(hand))

sorted_hands = dict(sorted(hands_strength_dict.items(), key=custom_sort))

result = 0
rank = 1
for hand in sorted_hands.keys():
    result += hands_bids_dict[hand] * rank
    rank += 1

print(result)
