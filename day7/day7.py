from collections import Counter

def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def parse_file(lines, use_jokers=False):
    hands=[]
    for line in lines:
        hand = line.split()[0]
        bid = line.split()[1]
        value = get_hand_value(hand, use_jokers)
        hands.append({"hand":hand, "bid":bid, "value": value})
    return hands

def all_chars_same(s):
    return s == len(s) * s[0]

def get_char_counts(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def has_n_same_chars(s, amount_of_same_chars):
    char_counts = get_char_counts(s)
    return amount_of_same_chars in char_counts.values()

def has_all_unique_chars(s):
    return len(s) == len(set(s))

def has_two_pairs(s):
    char_counts = get_char_counts(s)
    return list(char_counts.values()).count(2) == 2

def has_full_house(s):
    char_counts = get_char_counts(s)
    values = char_counts.values()
    return 3 in values and 2 in values

def transfrom_hand_to_numeric_value(hand, use_jokers=False):
    j_value = use_jokers and "01" or "11"
    replace_dict = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "T": "10",
        "9": "09",
        "8": "08",
        "7": "07",
        "6": "06",
        "5": "05",
        "4": "04",
        "3": "03",
        "2": "02",
        "J": j_value
    }
    translation_table = str.maketrans(replace_dict)
    return hand.translate(translation_table)

def get_highest_card(hand):
    values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    smallest_integer = 500
    for char in hand:
        if char in values:
            if values.index(char) < smallest_integer:
                smallest_integer = values.index(char)
    return values[smallest_integer]

def has_multiple_pairs(s):
    char_counts = Counter(s)
    return list(char_counts.values()).count(2) > 1

def replace_jokers(hand):
    #Aluksi poistetaan jokerit
    hand_without_jokers = hand.replace('J', '')
    if hand_without_jokers == "":
        return "AAAAA"
    
    #Sitten etsitään tyypillisin kortti, se korvataan. 
    char_counts = Counter(hand_without_jokers)
    most_common_char = max(char_counts, key=char_counts.get)
    replace_char = most_common_char

    if has_multiple_pairs(hand_without_jokers) or has_all_unique_chars(hand_without_jokers):
        replace_char = get_highest_card(hand_without_jokers)

    #Korvataan jokeri valitulla kortilla.
    hand_jokers_replaced = hand.replace('J', replace_char)
    return hand_jokers_replaced


def get_hand_value(hand, use_jokers=False):
    first_number = "0"
    hand_without_jokers = hand

    if use_jokers:
        hand = replace_jokers(hand)

    if (all_chars_same(hand)):
        first_number = "7"
    elif has_n_same_chars(hand, 4):
        first_number = "6"
    elif has_full_house(hand):
        first_number = "5"
    elif has_n_same_chars(hand, 3):
        first_number = "4"
    elif has_two_pairs(hand):
        first_number = "3"
    elif has_n_same_chars(hand, 2):
        first_number = "2"
    else:  
        first_number = "1"

    return int(first_number + transfrom_hand_to_numeric_value(hand_without_jokers, use_jokers))

def count_total_winnings(sorted_hands):
    total_winnings = 0
    for i, hand in enumerate(sorted_hands):
        rank = i+1
        win_amount = rank * int(hand['bid'])
        total_winnings += win_amount
    return total_winnings

def task1(lines):
    hands = parse_file(lines)   
    sorted_hands = sorted(hands, key=lambda x: x['value'])
    total_winnings = count_total_winnings(sorted_hands)
    print("Task 1:", total_winnings)

def task2(lines):
    hands = parse_file(lines, True)   
    sorted_hands = sorted(hands, key=lambda x: x['value'])
    total_winnings = count_total_winnings(sorted_hands)
    print("Task 2:", total_winnings)

def main():
    file_path = "day7\\data.txt"
    lines = read_file(file_path)
    task1(lines)
    task2(lines)

if __name__ == "__main__":
    main()