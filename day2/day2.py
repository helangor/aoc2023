def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

"""Etsii pelin suurimman saman väristen määrän"""
def parse_line(line):
    parts = line.split(':')
    game_id = parts[0].split()[1] 
    gems = {}
    gem_parts = ''.join(parts[1:]).split(';')
    for gem_part in gem_parts:
        gem_info = gem_part.split(',')
        for info in gem_info:
            count, color = info.split()
            if color not in gems or int(count) > gems[color]:
                gems[color] = int(count)
    return game_id, gems

"""Peli mahdollinen, jos pelin kuulia tietylle värille ei ole enempää kuin haluttu määrä"""
def is_game_possible(wanted_cubes, line_cubes):
    for color, count in wanted_cubes.items():
        if line_cubes[color] > count:
            return False
    return True

def multiply_dict_values(d):
    result = 1
    for value in d.values():
        result *= value
    return result

def task1(lines):
    total_game_id_sum = 0
    wanted_cubes = {"red": 12, "green": 13, "blue": 14}

    for line in lines:
        game_id, game_gems = parse_line(line.strip())
        if is_game_possible(wanted_cubes, game_gems):
            total_game_id_sum += int(game_id)

    print(total_game_id_sum)

def task2(lines):
    total_sum = 0
    for line in lines:
        game_id, game_gems = parse_line(line.strip())
        gem_multiplication = multiply_dict_values(game_gems)
        total_sum += gem_multiplication
    print(total_sum)

def main():
    file_path = "C:\\Users\\henri\\Desktop\\aoc\\day2\\day2.txt"
    lines = read_file(file_path)
    task1(lines)
    task2(lines)

if __name__ == "__main__":
    main()