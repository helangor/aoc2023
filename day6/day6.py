def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def parse_lines(lines):
    races={}
    for i, line in enumerate(lines):
        # Times are in the first row
        if i == 0:
            times = line.split(":")[1].strip().split()
            for j, time in enumerate(times):
                races[j] = {}
                races[j]['time'] = int(time)
        else: 
            distances = line.split(":")[1].strip().split()
            for k, distance in enumerate(distances):
                races[k]['distance'] = int(distance)
    return races

def parse_lines_task2(lines):
    race=[]
    for i, line in enumerate(lines):
        val = "".join(line.split(":")[1].strip().split())
        race.append(int(val)) 
    return race

def calculate_distance(hold_button_time, max_time):
    time_left_to_drive = max_time - hold_button_time
    distance_reached = hold_button_time * time_left_to_drive
    return distance_reached

def add_number_of_ways_to_beat_distance(race_dict):
    for i in race_dict:
        distance_to_beat = race_dict[i]['distance']
        time =  race_dict[i]['time']
        sum_of_ways = 0
        for j in range(0, time):
            distance = calculate_distance(j+1, time)
            if (distance > distance_to_beat):
                sum_of_ways += 1
        race_dict[i]['ways'] = sum_of_ways
    return race_dict

def multiply_ways(race_dict):
    product = 1
    for key in race_dict:
        product *= race_dict[key]['ways']
    return product

def task1(lines):
    race_dict = parse_lines(lines)
    race_dict = add_number_of_ways_to_beat_distance(race_dict)
    number_of_ways_to_beat_record = multiply_ways(race_dict)
    print("Task 1: ", number_of_ways_to_beat_record)

def task2(lines):
    race = parse_lines_task2(lines)
    time=race[0]
    distance_to_beat=race[1]
    sum_of_ways = 0
    for j in range(0, time):
        distance = calculate_distance(j+1, time)
        if (distance > distance_to_beat):
            sum_of_ways += 1
    print(sum_of_ways)
    #print("Task 2: ", number_of_ways_to_beat_record)

def main():
    file_path = "day6\\data.txt"
    lines = read_file(file_path)
    #task1(lines)
    task2(lines)

if __name__ == "__main__":
    main() 