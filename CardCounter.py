CARD_VALUES = {
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 0,
    '8': 0,
    '9': 0,
    '0': -1,
    '1': -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1,
    '*': -1
    }

DECKS = 8

def main():
    count = 0
    cards = 0
    user_input = True
    decks_played = 0
    while user_input:
        user_input = input('CARDS >> ')
        user_input = user_input.upper()
        if user_input == "DONE":
            break
        cards += len(user_input)
        for card in user_input:
            count += CARD_VALUES[card]
        decks_played = cards / 52.0
        true_count = count / (DECKS - decks_played)
        print('Count:      {}'.format(count))
        print('True Count: {:2.2f}'.format(true_count))
    print('Decks Played: {:1.2f}'.format(decks_played))

if __name__ == '__main__':
    main()
