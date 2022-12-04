f = open('camp_cleanup').read().splitlines()

count = 0
count_total_overlaps = 0


def is_single_overlap(section_one, section_two) -> bool:
    return section_one[0] <= section_two[0] <= section_one[1] or section_one[0] <= section_two[1] <= section_one[1]


def is_overlap(section_one, section_two) -> bool:
    return section_one[0] <= section_two[0] and section_one[1] >= section_two[1]


for line in f:
    sections = line.split(',')
    first_section, second_section = sections.__getitem__(0).split('-'), sections.__getitem__(1).split('-')
    first_section, second_section = list(map(int, first_section)), list(map(int, second_section))

    if is_overlap(first_section, second_section) or is_overlap(second_section, first_section):
        count_total_overlaps += 1
        count += 1

    elif is_single_overlap(first_section, second_section):
        count_total_overlaps += 1

print('The number of overlaps are:', count)
print('The number of total overlaps is:', count_total_overlaps)
