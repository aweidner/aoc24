import re


def vertical(grid):
    lines = grid.split("\n")

    transposed = []
    for character_position in range(len(lines)):
        new_line = []
        for line in lines:
            new_line.append(line[character_position])
        transposed.append("".join(new_line))
    return horizontal("\n".join(transposed))


def horizontal(grid):
    return sum(within_line(line) for line in grid.split("\n"))


def within_line(search_surface):
    proper = [m.start() for m in re.finditer("XMAS", search_surface)]
    reversed = [m.start() for m in re.finditer("SAMX", search_surface)]
    return len(proper) + len(reversed)


def diagonal_lr(grid, start):
    line = []
    while start[0] < len(grid) and start[1] < len(grid[start[0]]):
        line.append(grid[start[0]][start[1]])
        start = (start[0] + 1, start[1] + 1)

    return "".join(line)

def diagonal_rl(grid, start):
    line = []
    while start[0] < len(grid) and start[1] >= 0:
        line.append(grid[start[0]][start[1]])
        start = (start[0] + 1, start[1] - 1)

    return "".join(line)


def diagonals_lr(grid):
    total = 0
    lines = grid.split("\n")
    for i in range(1, len(lines)):
        total += within_line(diagonal_lr(lines, (0, i)))

    total += within_line(diagonal_lr(grid.split("\n"), (0, 0)))

    for i in range(1, len(lines[0])):
        total += within_line(diagonal_lr(lines, (i, 0)))

    return total

def diagonals_rl(grid):
    total = 0
    lines = grid.split("\n")

    for i in range(0, len(lines[0]) - 1):
        total += within_line(diagonal_rl(lines, (0, i)))

    total += within_line(diagonal_rl(lines, (0, len(lines[0]) - 1)))

    for i in range(1, len(lines)):
        total += within_line(diagonal_rl(lines, (i, len(lines[0]) - 1)))

    return total

def part_one():
    with open("input.txt") as f:
        contents = f.read()
        return vertical(contents) + horizontal(contents) + diagonals_lr(contents) + diagonals_rl(contents)

#print(part_one())

def is_xmas(grid, x, y):
    return (
        grid[x-1][y-1] == "M" and grid[x-1][y+1] == "M" and grid[x+1][y-1] == "S" and grid[x+1][y+1] == "S"
    ) or (
        grid[x-1][y-1] == "S" and grid[x-1][y+1] == "S" and grid[x+1][y-1] == "M" and grid[x+1][y+1] == "M"
    ) or (
        grid[x-1][y-1] == "M" and grid[x-1][y+1] == "S" and grid[x+1][y-1] == "M" and grid[x+1][y+1] == "S"
    ) or (
        grid[x-1][y-1] == "S" and grid[x-1][y+1] == "M" and grid[x+1][y-1] == "S" and grid[x+1][y+1] == "M"
    )


def part_two():
    with open("input.txt") as f:
        grid = f.read().split("\n")

        a_positions = []

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] == "A":
                    a_positions.append((i, j))

        total = 0

        for x, y in a_positions:
            if is_xmas(grid, x, y):
                total += 1

        return total

print(part_two())