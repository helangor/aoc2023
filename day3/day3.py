def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

def is_symbol(char):
    return char != "." and not char.isalpha() and not char.isdigit()

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

def is_symbol_nearby(matrix, x, y):
    #Check if there is a symbol in the 8 nearby squares
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_x, new_y = x + i, y + j
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                if is_symbol(matrix[new_x][new_y]):
                    return True
    return False

def go_through_matrix_numbers(matrix):
    total_sum = 0
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
                        if is_symbol_nearby(matrix, i, index):
                            total_sum += int(''.join(found_number))
                            break
                    found_number = []
    print(total_sum)

def task1(lines):
    matrix = create_2d_list(lines)
    go_through_matrix_numbers(matrix)
    

def main():
    file_path = "day3\\data.txt"
    lines = read_file(file_path)
    task1(lines)

if __name__ == "__main__":
    main()