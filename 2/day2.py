def is_monotonically_increasing(s):
    return all(s[i] < s[i+1] for i in range(len(s)-1))

def is_monotonically_decreasing(s):
    return all(s[i] > s[i+1] for i in range(len(s)-1))
    
def levels_no_greater_than_diff_of_3(s):
    return all(abs(s[i+1] - s[i]) <= 3 for i in range(len(s)-1))

def part_one():
    total = 0
    with open("input.txt") as r:
        for line in r:
            s = [int(x) for x in line.strip().split()]
            if (is_monotonically_increasing(s) or is_monotonically_decreasing(s)) and levels_no_greater_than_diff_of_3(s):
                total += 1

    return total

#print(part_one())

# Slowest method in the world
def dampen(s):
    for i in range(len(s)):
        s_copy = s[:]
        s_copy.pop(i)
        yield s_copy

def part_two():
    total = 0
    with open("input.txt") as r:
        for line in r:
            s = [int(x) for x in line.strip().split()]
            for dampen_s in dampen(s):
                if (is_monotonically_increasing(dampen_s) or is_monotonically_decreasing(dampen_s)) and levels_no_greater_than_diff_of_3(dampen_s):
                    total += 1
                    break

    return total

print(part_two())