f = open('camp_cleanup').read().splitlines()

count = 0


def is_overlap(section_one, section_two) -> bool:
    return int(section_one[0]) <= int(section_two[0]) and int(section_one[1]) >= int(section_two[1])


for line in f:
    sections = line.split(',')

    first_section, second_section = sections.__getitem__(0).split('-'), sections.__getitem__(1).split('-')

    if is_overlap(first_section, second_section) or is_overlap(second_section, first_section):
        count += 1

print('The number of overlaps are: ', count)
