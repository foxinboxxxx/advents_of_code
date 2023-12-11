import re

def check_length_of_numbers(numbers):
    num1 = numbers[0]
    num2 = numbers[-1]
    if len(numbers) > 1:
        if len(numbers[0]) > 1:
            num1 = num1[0]
        if len(numbers[-1]) > 1:
            num2 = num2[-1]
        return int(num1 + num2)
    elif len(numbers) == 1:
        return int(num1[0] + num2[-1])
    else:
        pass

sum = 0

digits_as_string_dict= [{"name": "one", "value": 1}, {"name": "two", "value": 2}, {"name": "three", "value": 3},
                        {"name": "four", "value": 4}, {"name": "five", "value": 5}, {"name": "six", "value": 6},
                        {"name": "seven", "value": 7}, {"name": "eight", "value": 8}, {"name": "nine", "value": 9}]

def check_digits_as_strings_in_line(digits_as_string_dict, string_line):
    digits_as_string_per_line = []
    for number_string in digits_as_string_dict:
        if number_string.get("name") in string_line:
            first_letter_position = [m.start() for m in re.finditer(number_string.get("value"), 'nottesttestyes')]
            digits_as_string_dict.append({"value": number_string.get("value"), "position": })


file = open("input.txt", 'r')

while True:
    line = file.readline()
    if not line:
        break
    digits_list = re.findall(r'\d+', line)
    # digits_list = [42, 25] => 45
    # digits_list = [724] => 74
    # digits_list[0] = digits_list[-1]
    sum += check_length_of_numbers(digits_list)
    
print(sum)

