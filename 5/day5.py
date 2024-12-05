def is_valid(sequence, orderings):
    numbers = sequence.strip().split(",")

    for i, n in enumerate(numbers):
        if any(f"{n}|{m}" not in orderings for m in numbers[i+1:]):
            return False
    return True

def part_one():
    with open("input.txt") as f:
        full_text = f.read().strip()
        orderings, sequences = full_text.split("\n\n")
        orderings = orderings.split("\n")

        sequences = sequences.split("\n")
        sequences = [s for s in sequences if is_valid(s, orderings)]

    total = 0
    for s in sequences:
        numbers = s.strip().split(",")
        integer_sequence = [int(n) for n in numbers]
        total += integer_sequence[len(integer_sequence)//2]
    
    return total


#print(part_one())