from collections import deque

file = f = open('supply_stacks').read().splitlines()

docker_input = [
    [' ', 'G', ' ', ' ', 'P', ' ', ' ', 'M', ' '],
    [' ', 'V', ' ', 'M', 'W', 'S', ' ', 'Q', ' '],
    [' ', 'N', ' ', 'N', 'G', 'H', ' ', 'T', 'F'],
    [' ', 'J', ' ', 'W', 'V', 'Q', 'W', 'F', 'P'],
    ['C', 'H', ' ', 'T', 'T', 'G', 'B', 'Z', 'B'],
    ['S', 'W', 'S', 'L', 'F', 'B', 'P', 'C', 'H'],
    ['G', 'M', 'Q', 'S', 'Z', 'T', 'J', 'D', 'S'],
    ['B', 'T', 'M', 'B', 'J', 'C', 'T', 'G', 'N']
]


def generate_crates(n_crates: int) -> list:
    return [deque() for _ in range(n_crates)]


def populate_docker(items: list, docker: list) -> list:
    for row in reversed(items):
        for i, element in enumerate(row):
            if element != ' ':
                docker[i].append(element)

    return docker


crates_docker, crates_docker_9001 = generate_crates(9), generate_crates(9)
crates_docker, crates_docker_9001 = populate_docker(docker_input, crates_docker), populate_docker(docker_input, crates_docker_9001)


def move_items_to_new_crate(n_items: int, origin: int, destination: int):
    for i in range(n_items):
        crates_docker[destination - 1].append(crates_docker[origin - 1].pop())


def move_items_to_new_crate_9001(n_items: int, origin: int, destination: int):
    temp = deque()

    for i in range(n_items):
        temp.append(crates_docker_9001[origin - 1].pop())

    while temp:
        crates_docker_9001[destination - 1].append(temp.pop())


for index, line in enumerate(f):

    if index > 9:
        instructions = line.split(' ')

        n_items, origin, destination = int(instructions[1]), int(instructions[3]), int(instructions[5])
        move_items_to_new_crate(n_items, origin, destination)
        move_items_to_new_crate_9001(n_items, origin, destination)


first_result, second_result = '', ''
for crate in crates_docker:
    first_result += crate.pop()

for c in crates_docker_9001:
    second_result += c.pop()

print('First solution:', first_result)
print('Second solution:', second_result)