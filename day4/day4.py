def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def parse_file(lines):
    cards = {}
    for line in lines:
        game_name, numbers = line.split(":")
        game_number = int(game_name.split()[1])
        winning_numbers, lottery_numbers = numbers.split("|")
        winning_numbers = winning_numbers.strip().split()
        lottery_numbers = lottery_numbers.strip().split()
        cards[game_number] = {"winning numbers": winning_numbers, "lottery numbers": lottery_numbers}
    return cards

def get_amount_of_winning_numbers(winning_numbers, lottery_numbers):
    amount_of_winning_numbers = 0
    for number in lottery_numbers:
        if number in winning_numbers:
            amount_of_winning_numbers += 1
    return amount_of_winning_numbers

def get_points(amount_of_winning_numbers):
    if amount_of_winning_numbers < 3:
        return amount_of_winning_numbers
    else:
        return 2**(amount_of_winning_numbers-1)

def task1(game_info):
    sum_of_points = 0
    for game in game_info:
        winning_numbers = game_info[game]["winning numbers"]
        lottery_numbers = game_info[game]["lottery numbers"]
        game_info[game]["copies"] = 0
        amount_of_wins = get_amount_of_winning_numbers(winning_numbers, lottery_numbers)
        points = get_points(amount_of_wins)
        sum_of_points += points
    print("Task 1: ", sum_of_points)

def add_copies_to_game_info(game_info, game, amount_of_wins, amount_of_copies):
    for i in range(game+1, game + amount_of_wins + 1):
        game_info[i]['copies'] += amount_of_copies + 1
            
def task2(game_info):
    amount_of_scratch_cards = 0
    for game in game_info:
        winning_numbers = game_info[game]["winning numbers"]
        lottery_numbers = game_info[game]["lottery numbers"]
        amount_of_wins = get_amount_of_winning_numbers(winning_numbers, lottery_numbers)
        amount_of_copies = game_info[game]["copies"]
        add_copies_to_game_info(game_info, game, amount_of_wins, amount_of_copies)
        game_instances = amount_of_copies + 1
        amount_of_scratch_cards += game_instances
    print("Task 2: ", amount_of_scratch_cards)

def main():
    file_path = "day4\\data.txt"
    lines = read_file(file_path)
    game_info = parse_file(lines)
    task1(game_info)
    task2(game_info)

if __name__ == "__main__":
    main()