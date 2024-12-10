def find_zero_positions(grid):
    for line in range(len(grid)):
        for column in range(len(grid[line])):
            if grid[line][column] == 0:
                yield (line, column)

def part_one():
    with open("input.txt") as f:
        grid = f.read().split("\n")
        grid = [list(int(n) for n in line) for line in grid]

    total_score = 0
    zero_positions = find_zero_positions(grid)

    for line, column in zero_positions:
        queue = [(line, column)]
        considered = set()

        while queue:
            l, c = queue.pop(0)

            if (l, c) in considered:
                continue
            considered |= {(l, c)}

            n = grid[l][c]
            if grid[l][c] == 9:
                total_score += 1
                continue

            if l + 1 < len(grid) and grid[l + 1][c] == n + 1:
                queue.append((l + 1, c))
            if l - 1 >= 0 and grid[l - 1][c] == n + 1:
                queue.append((l - 1, c))
            if c + 1 < len(grid[l]) and grid[l][c + 1] == n + 1:
                queue.append((l, c + 1))
            if c - 1 >= 0 and grid[l][c - 1] == n + 1:
                queue.append((l, c - 1))

    return total_score


print(part_one())

def part_two():
    with open("input3.txt") as f:
        grid = f.read().split("\n")
        grid = [list(int(n) for n in line) for line in grid]

    total_score = 0
    zero_positions = find_zero_positions(grid)

    for line, column in zero_positions:
        queue = [(line, column)]

        while queue:
            l, c = queue.pop()

            n = grid[l][c]
            if grid[l][c] == 9:
                total_score += 1

            if l + 1 < len(grid) and grid[l + 1][c] == n + 1:
                queue.append((l + 1, c))
            if l - 1 >= 0 and grid[l - 1][c] == n + 1:
                queue.append((l - 1, c))
            if c + 1 < len(grid[l]) and grid[l][c + 1] == n + 1:
                queue.append((l, c + 1))
            if c - 1 >= 0 and grid[l][c - 1] == n + 1:
                queue.append((l, c - 1))

    return total_score


print(part_two())