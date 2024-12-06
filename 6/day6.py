def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return i, j
    return -1, -1

def guard_in_grid(grid, guard_position):
    line, column = guard_position
    return line >= 0 and line < len(grid) and column >= 0 and column < len(grid[0])


def part_one():
    with open("input.txt") as f:
        grid = f.read().split("\n")
        grid = [list(line) for line in grid]

    direction = (-1, 0)
    guard_position = find_guard(grid) 

    while True:
        x, y = guard_position
        dx, dy = direction

        nx, ny = x + dx, y + dy
        if not guard_in_grid(grid, (nx, ny)):
            break

        if grid[nx][ny] != '#':
            grid[x][y] = 'X'
            guard_position = (nx, ny)
            continue
    
        if dx == -1 and dy == 0:
            dx, dy = 0, 1
        elif dx == 0 and dy == 1:
            dx, dy = 1, 0
        elif dx == 1 and dy == 0:
            dx, dy = 0, -1
        else:
            dx, dy = -1, 0

        direction = (dx, dy)

    
    return sum([line.count('X') for line in grid]) + 1

#print(part_one())

def part_two():
    with open("input.txt") as f:
        original_grid = f.read().split("\n")
        original_grid = [list(line) for line in original_grid]

    start_position = find_guard(original_grid)
    valid_obstacles = 0
    
    for i in range(len(original_grid)):
        for j in range(len(original_grid[i])):
            if original_grid[i][j] != '.':
                continue

            grid = [line[:] for line in original_grid]
            grid[i][j] = '#'

            direction = (-1, 0)
            guard_position = start_position

            seen_states = set()

            while True:
                x, y = guard_position
                dx, dy = direction

                nx, ny = x + dx, y + dy
                if not guard_in_grid(grid, (nx, ny)):
                    break

                if grid[nx][ny] != '#':
                    guard_position = (nx, ny)
                else: 
                    if dx == -1 and dy == 0:
                        dx, dy = 0, 1
                    elif dx == 0 and dy == 1:
                        dx, dy = 1, 0
                    elif dx == 1 and dy == 0:
                        dx, dy = 0, -1
                    else:
                        dx, dy = -1, 0

                    direction = (dx, dy)

                if (guard_position, direction) in seen_states:
                    valid_obstacles += 1
                    break
                else:
                    seen_states.add((guard_position, direction))

    return valid_obstacles

#import time
#start = time.time()
print(part_two())
#print(time.time() - start)