import string

f = open("rucksack_input").read().splitlines()

alphabet = list(string.ascii_letters)
priority_count = badges_priority_count = three_lines_count = 0
lines_set = []

for line in f:

    three_lines_count += 1
    lines_set.append(line)
    first_item, second_item = line[:len(line)//2], line[len(line)//2:]

    repeated_items = []
    for element in first_item:

        if second_item.__contains__(element) and element not in repeated_items:
            repeated_items.append(element)
            priority_count += alphabet.index(element) + 1

    if three_lines_count == 3:
        three_lines_count = 0

        for element in lines_set.__getitem__(0):
            if element in lines_set.__getitem__(1) and element in lines_set.__getitem__(2):
                badges_priority_count += alphabet.index(element) + 1
                break

        lines_set = []


print(priority_count)
print(badges_priority_count)
