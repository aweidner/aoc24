def part_one():
    a, b = [], []

    with open("input.txt") as r:
        for line in r:
            x, y = line.strip().split()
            a.append(x)
            b.append(y)

    a = sorted(a)
    b = sorted(b)

    total = 0
    for i in range(len(a)):
        total += abs(int(a[i]) - int(b[i]))

    return total

#print(part_one())


def part_two():
    left = set() 
    right = dict()

    with open("input.txt") as r:
        for line in r:
            x, y = line.strip().split()
            left.add(x)

            if y in right:
                right[y] += 1
            else:
                right[y] = 1

    total = 0
    for v in left:
        total += int(v) * right.get(v, 0)

    return total


print(part_two())