file = open('treetop_tree_house').read().splitlines()

tree_score = 0
t = 0


def get_score(col_i, row_i) -> bool:
    return get_top_score(col_i, row_i) \
           * get_bottom_score(col_i, row_i) \
           * get_left_score(col_i, row_i) \
           * get_right_score(col_i, row_i)


def get_top_score(col_i, row_i) -> bool:
    c = 0
    tree = grid[row_i][col_i]
    while row_i > 0:
        row_i -= 1
        c += 1
        if grid[row_i][col_i] >= tree:
            return c

    return c


def get_bottom_score(col_i, row_i) -> bool:
    c = 0
    tree = grid[row_i][col_i]
    while row_i < len(grid) - 1:
        row_i += 1
        c += 1
        if grid[row_i][col_i] >= tree:
            return c

    return c


def get_left_score(col_i, row_i) -> bool:
    c = 0
    tree = grid[row_i][col_i]
    while col_i > 0:
        col_i -= 1
        c += 1
        if grid[row_i][col_i] >= tree:
            return c

    return c


def get_right_score(col_i, row_i) -> bool:
    c = 0
    tree = grid[row_i][col_i]
    while col_i < len(grid[row_i]) - 1:
        col_i += 1
        c += 1
        if grid[row_i][col_i] >= tree:
            return c

    return c

visible_trees_count, grid = 0, []
for line in file:
    listed_line = [int(x) for x in line]
    grid.append(listed_line)

for idx, trees_row in enumerate(grid):
    for i, tree in enumerate(grid[idx]):
        new_score = get_score(i, idx)
        if tree_score < new_score:
            tree_score = new_score

print('Second solution', tree_score)
