def is_smaller(calories, n) -> bool:
    return calories < n


f = open("calorie_counting").read().splitlines()

max_calories = second_max = third_max = temp = 0

for line in f:

    if line == '':
        if is_smaller(max_calories, temp):
            third_max = second_max
            second_max = max_calories
            max_calories = temp
        elif is_smaller(second_max, temp):
            third_max = second_max
            second_max = temp
        elif is_smaller(third_max, temp):
            third_max = temp
        temp = 0
    else:
        temp += int(line)

total = max_calories + second_max + third_max
print(total, max_calories, second_max, third_max)

