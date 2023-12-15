import re

green = "green"
red = "red"
blue = "blue"
cubes = {"red": 12, "green": 13, "blue": 14}
sum = 0
file = open("input.txt", "r")


def get_number_from_text(text):
    number = re.findall(r"\d", text)
    number = int("".join(map(str, number)))
    return number


def process_line(line):
    valid = False
    cubes_dict = {"red": [], "green": [], "blue": []}
    splitted_line = line.split(":")
    # Get game ID
    game_id = get_number_from_text(splitted_line[0])

    balls = (splitted_line[1].replace(";", ",")).split(",")
    for ball in balls:
        if green in ball:
            ball_nr = get_number_from_text(ball)
            cubes_dict[green].append(ball_nr)
        if red in ball:
            ball_nr = get_number_from_text(ball)
            cubes_dict[red].append(ball_nr)
        if blue in ball:
            ball_nr = get_number_from_text(ball)
            cubes_dict[blue].append(ball_nr)

    for key in cubes:
        if cubes[key] >= max(cubes_dict[key]):
            valid = True
        else:
            valid = False
            break

    if valid:
        return game_id
    else:
        return 0

while True:
    line = file.readline()
    if not line:
        break

    sum += process_line(line)

# print(sum)

# test_line = "Game 1: 10 red, 7 green, 3 blue; 5 blue, 3 red, 10 green; 4 blue, 14 green, 7 red; 1 red, 11 green; 6 blue, 17 green, 15 red; 18 green, 7 red, 5 blue"

# # process_line(test_line)
