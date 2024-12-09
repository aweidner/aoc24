def generate_list(data):
    filled = True
    file_id = 0
    l = []
    for c in data:
        n = int(c)
        if filled:
            l.extend([file_id] * n)
            file_id += 1
        else:
            l.extend([-1] * n)

        filled = not filled

    return l


def part_one():
    with open("input.txt") as f:
        data = generate_list(f.read())

        current_length = len(data)
        index = 0

        while index < current_length:
            if data[index] == -1:
                data[index] = data.pop(-1)
            index += 1

            while data[-1] == -1:
                data.pop(-1)

            current_length = len(data)
        
        sum = 0
        for i, n in enumerate(data):
            sum += i * n
        
        return sum

print(part_one())

def chunks_of_empty_space(data):
    for i, n in enumerate(data):
        if n == -1:
            start = i
            end = i
            while data[end] == -1:
                end += 1
            yield (start, end - 1)

def chunks_of_data(data):
    index = len(data) - 1
    while index >= 0:
        if data[index] != -1:
            end = index
            start = index
            while end >= 0 and start >= 0 and data[end] == data[start]:
                start -= 1
            yield (start + 1, end)
            index = start
        else:
            index -= 1

def part_two():

    with open("input.txt") as f:
        data = generate_list(f.read())
        data_chunks = list(chunks_of_data(data))

        for data_start, data_end in data_chunks:
            for space_start, space_end in chunks_of_empty_space(data):

                if data_start < space_start:
                    continue

                data_segment = data[data_start:data_end + 1]
                empty_space = data[space_start:space_end + 1]

                chunk_fits = len(data_segment) <= len(empty_space)

                if chunk_fits:
                    while data_start <= data_end:
                        data[space_start] = data[data_start]
                        data[data_start] = -1
                        data_start += 1 
                        space_start += 1

                    while data[-1] == -1:
                        data.pop(-1)

                    break


        sum = 0
        for i, n in enumerate(data):
            if data[i] == -1:
                continue
            sum += i * n
        
        return sum
        
print(part_two())