def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def str_list_to_int_list(str_list):
    return [int(num) for num in str_list]

def parse_file(lines):
    seeds=[]
    maps={}
    map_name = ""
    for i, line in enumerate(lines):
        if i == 0:
            seeds = str_list_to_int_list(line.split(":")[1].strip().split())
        elif line.strip() == "":
            continue
        elif any(char.isalpha() for char in line):
            map_name = line.split(" ")[0].strip()
            maps[map_name] = []
        else:
            maps[map_name].append(str_list_to_int_list(line.strip().split()))
    return seeds, maps

def is_source_number_in_map_range(source_number, source_range, range_length):
    if source_range <= source_number <= source_range + range_length:
        return True
    return False

def get_destination_number(source_number, map_values):
    for map_value in map_values:
        destination_range, source_range, range_length = map_value
        if is_source_number_in_map_range(source_number, source_range, range_length):
            return source_number - source_range + destination_range
    return source_number


def go_through_all_maps(seeds, maps):
    source_numbers = seeds
    for map_name in maps:
        map_values = maps[map_name]
        new_source_numbers = []
        for source_number in source_numbers:
            #Selvitä mitä arvoja käytetään ja sitten mappää
            dest_number = get_destination_number(source_number, map_values)
            new_source_numbers.append(dest_number)
        source_numbers = new_source_numbers
    return source_numbers

def generate_numbers(start, length):
    for i in range(length):
        yield start + i

"""Ei toimi näin, koska liian isot numerot"""
def getSeedsFromSeedRanges(seeds, maps):
    lowest_number = 111111110
    for i, seed_start_number in enumerate(seeds):
        # Joka toinen numero on aloitus numero ja joka toinen on range
        if i%2 != 0:
            continue
        if (i+1) == len(seeds):
            break
        seed_range = seeds[i+1]
        #numbers = generate_numbers(seed_start_number, seed_range)
        for number in range(seed_start_number, seed_start_number + seed_range):
            final_number = go_through_all_maps([number], maps)
            if (final_number[0] < lowest_number):
                lowest_number = final_number[0]
            print(number)
    print(lowest_number)
            
def task1(lines):
    seeds, maps = parse_file(lines)
    final_numbers = go_through_all_maps(seeds, maps)
    print("Task 1: ", min(final_numbers))

def task2(lines):
    seeds, maps = parse_file(lines)

    # Pitää käydä lista seed-to-soil map numeroita läpi. jokaisesta ensimmäinen ja vika. ja sitten tulostaa mikä on pienin tulos. Sitten katsoa tämän välin luvuista pienin, mikä löytyyy.

    #final_numbers = go_through_all_maps(seeds, maps)
    #print("Task 2: ", min(final_numbers))

def main():
    file_path = "day5\\data.txt"
    lines = read_file(file_path)
    #task1(lines)
    task2(lines)

if __name__ == "__main__":
    main()