from collections import Counter
import math

def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def parse_file(lines, use_jokers=False):
    input_values=[]
    direction_map={}
    for i, line in enumerate(lines):
        if (i == 0):
            input_values = line.split()
        else:
            if (line != ""):
                key = line.split("=")[0].strip()
                values = line.split("=")[1].split(",")
                cleaned_values = [s.strip().replace('(', '').replace(')', '') for s in values]
                direction_map[key] = cleaned_values
    return input_values, direction_map

def go_through_instructions(instructions):
    input_values, direction_map = instructions
    element = "AAA"
    steps = 0
    iterator = 0
    
    while element != "ZZZ":
        input = input_values[0][iterator]
        if input == "R":
            element = direction_map[element][1]
        else:   
            element = direction_map[element][0]
        steps += 1
        iterator += 1
        if (iterator >= len(input_values[0])):
            iterator = 0
    print("Steps:", steps)
    
def find_keys_ending_with_A(direction_map):
    keys = {}
    for key in direction_map:
        if key.endswith('A'):
            keys[key] = []
    return keys

def calculate_differences(start_keys):
    for key in start_keys:
        diffrence = start_keys[key][1] - start_keys[key][0]
        start_keys[key] = diffrence
    return start_keys

def append_result_to_start_keys(instructions, start_keys):
    input_values, direction_map = instructions
    for key in start_keys:
        element = key
        iterator = 0
        for i in range(100000):
            input = input_values[0][iterator]
            if input == "R":
                element = direction_map[element][1]
            else:   
                element = direction_map[element][0]
            if element.endswith('Z'):

                #Kaksi ensimmäistä arvoa riittää. 
                if (len(start_keys[key]) == 2):
                    continue
                start_keys[key].append(i)

            iterator += 1
            if (iterator >= len(input_values[0])):
                iterator = 0
    return start_keys

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def get_lcm(numbers):
    lcm_value = numbers[0]
    for i in numbers[1:]:
        lcm_value = lcm(lcm_value, i)
    return lcm_value

def go_through_instructions_two_start_values(instructions):
    start_keys = find_keys_ending_with_A(instructions[1])
    start_keys = append_result_to_start_keys(instructions, start_keys)
    start_keys = calculate_differences(start_keys)
    lcm = get_lcm(list(start_keys.values()))
    print("Task 2: ", lcm)

def task1(lines):
    instructions = parse_file(lines)
    go_through_instructions(instructions)

def task2(lines):
    instructions = parse_file(lines)
    go_through_instructions_two_start_values(instructions)

def main():
    file_path = "day8\\data.txt"
    lines = read_file(file_path)
    task1(lines)
    task2(lines)

if __name__ == "__main__":
    main()