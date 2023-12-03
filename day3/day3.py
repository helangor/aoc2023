def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

def is_symbol(char):
    return char != "." and not char.isalpha() and not char.isdigit()

def is_gear(char):
    return char == "*"

def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
#Create 2d list from lines
def create_2d_list(lines):
    matrix = []
    for line in lines:
        row = []
        for char in line:
            if (char == "\n"):
                continue
            row.append(char)
        matrix.append(row)
    return matrix

def get_nearby_marks(matrix, x, y, neardy_function):
    nearby_marks = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_x, new_y = x + i, y + j
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                if neardy_function(matrix[new_x][new_y]):
                    coords = [new_x, new_y]
                    nearby_marks.append(coords)
    return nearby_marks

def get_numbers_with_adjacent_symbol(matrix):
    numbers = []
    for i in range(len(matrix)):
        found_number = []
        for j in range(len(matrix[i])):
            if is_number(matrix[i][j]):
                found_number.append(matrix[i][j])   
                row_length = len(matrix[i])
                if j+1 < row_length and is_number(matrix[i][j+1]):
                    continue
                if j+1 == row_length or (j+1 < row_length and not is_number(matrix[i][j+1])):
                    #Käy läpi löydetyn numeron ja katsoo onko sen ympärillä symboleja                    
                    begin_index = j+1 - len(found_number)
                    stop_index = j
                    for index in range(begin_index, stop_index+1):
                        if get_nearby_marks(matrix, i, index, is_symbol):
                            numbers.append(int(''.join(found_number)))
                            break
                    found_number = []
    return numbers

def get_number_with_start_coords(matrix, number_coordinates):
    row = matrix[number_coordinates[0]]
    y_coord = number_coordinates[1]
    number=[]
    while (y_coord < len(row) and is_number(row[y_coord])):
        number.append(row[y_coord])
        y_coord += 1
    return number

def get_number_start_coordinants(matrix, number_coordinates):
    #aina sama rivi, joten käydään läpi vain y-koordinaatit
    row = matrix[number_coordinates[0]]
    y_coord = number_coordinates[1]
    while (y_coord > 0 and is_number(row[y_coord-1])):
        y_coord -= 1
    start_coordinate = [number_coordinates[0], y_coord]
    return start_coordinate

def get_gear_ratios(matrix):
    sum_of_ratios = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_gear(matrix[i][j]):
                numbers_nearby_gear = get_nearby_marks(matrix, i, j, is_number)
                gear_start_coords =[]
                for number_coords in numbers_nearby_gear:
                    start_coords = get_number_start_coordinants(matrix, number_coords)
                    #Tää ois voinu palauttaa dictin, jossa numeron aloitus koordinaatit ja se numero. 

                    if start_coords not in gear_start_coords:
                        gear_start_coords.append(start_coords)
                amount_of_numbers_neardy = len(gear_start_coords)
                if (amount_of_numbers_neardy == 2):
                    first_number = get_number_with_start_coords(matrix, gear_start_coords[0])
                    second_number = get_number_with_start_coords(matrix, gear_start_coords[1])
                    gear_ration = int(''.join(first_number)) * int(''.join(second_number))
                    sum_of_ratios += gear_ration
    return sum_of_ratios

def task1(matrix):
    found_numbers = get_numbers_with_adjacent_symbol(matrix)
    print("Task 1:", sum(found_numbers))
    
def task2(matrix):
    gear_ratios_sum = get_gear_ratios(matrix)
    print("Task 2:", gear_ratios_sum)

def main():
    file_path = "day3\\data.txt"
    lines = read_file(file_path)
    matrix = create_2d_list(lines)
    task1(matrix)
    task2(matrix)

if __name__ == "__main__":
    main()