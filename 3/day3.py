import re

def parse_instructions(contents):
    pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")

    for instruction in pattern.findall(contents):
        instruction = instruction.replace("mul(", "").replace(")", "")
        instruction = instruction.split(",")
        instruction = [int(i) for i in instruction]
        yield instruction


def parse_instructions_start_until_dont(contents):
    pattern = re.compile(r"^(.*?mul\([0-9]+,[0-9]+\).*?)don't\(\)")

    match = pattern.search(contents)
    instructions = parse_instructions(match.group(1))
    end = match.end(1)

    return instructions, end

def parse_instructions_do_until_dont(contents):
    pattern = re.compile(r"do\(\)(.*?mul\([0-9]+,[0-9]+\).*?)don't\(\)")

    for instruction_group in pattern.findall(contents):
        instructions = parse_instructions(instruction_group)
        for instruction in instructions:
            yield instruction

def parse_instructions_do_until_end(contents):
    pattern = re.compile(r"^(.*?\)[0-9]+,[0-9]+\(lum.*?)\)\(od")
    match = pattern.search(contents[::-1])

    instructions = parse_instructions(match.group(1)[::-1])
    end = len(contents) - match.end(1)

    return instructions, end

def part_one():
    with open("input.txt") as r:
        contents = "".join(r.read().split("\n"))
        total = 0
        for instruction in parse_instructions(contents):
            x, y = instruction
            total += x * y
        return total

#print(part_one())

def part_two():
    with open("input.txt") as r:
        contents = "".join(r.read().split("\n"))
        total = 0
        instructions, start = parse_instructions_start_until_dont(contents)
        for instruction in instructions:
            x, y = instruction
            total += x * y
        instructions, end = parse_instructions_do_until_end(contents)
        for instruction in instructions:
            x, y = instruction
            total += x * y

        instructions = parse_instructions_do_until_dont(contents[start:end])
        for instruction in instructions:
            x, y = instruction
            total += x * y

        return total

print(part_two())