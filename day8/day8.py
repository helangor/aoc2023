from collections import Counter

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
    
def task1(lines):
    instructions = parse_file(lines)
    go_through_instructions(instructions)

def main():
    file_path = "day8\\data.txt"
    lines = read_file(file_path)
    task1(lines)

if __name__ == "__main__":
    main()