import os

num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_first_word(s, num_dict):
    for i in range(len(s)):
        for word in num_dict.keys():
            if s[i:].startswith(word):
                return word
    return None

""" Korvaa ekan löytyneen sanan dictin arvolla"""
def replace_first_string_with_number(s, num_dict):    
    first_found_word = get_first_word(s, num_dict)
    if (first_found_word == None):
        return s
    s = s.replace(first_found_word, str(num_dict[first_found_word]), 1)
    return s

def reverse_dict_keys(num_dict):
    return {k[::-1]: v for k, v in num_dict.items()}

""" Ottaa dictin ja sanan ja korvaa sanan dictin arvolla """
def replace_last_string_with_number(s, num_dict):    
    reversed_dict = reverse_dict_keys(num_dict)
    reversed_word = s[::-1]
    first_found_word = get_first_word(reversed_word, reversed_dict)
    if (first_found_word == None):
        return s

    reversed_word = reversed_word.replace(first_found_word, str(reversed_dict[first_found_word]), 1)
    s = reversed_word[::-1]
    return s


def remove_non_numeric(word):
    return ''.join(char for char in word if char.isdigit())


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combine the script directory with the file name to get the full path
file_path = os.path.join(script_dir, "day1.txt")

# Open the file in read mode
with open(file_path, "r") as file:
    lines = file.readlines()
    totalsum = 0

    for line in lines:
        first = remove_non_numeric(replace_first_string_with_number(line, num_dict))
        last = remove_non_numeric(replace_last_string_with_number(line, num_dict))
        sumValue = int(first[0] + last[-1], 10)
        totalsum += sumValue
    print(totalsum)


