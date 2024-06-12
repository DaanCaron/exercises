def rle_encode(data):
    data = iter(data)
    try:
        last_checked = next(data)
        count = 1
        for data in data:
            if data == last_checked:
                count += 1
            else:
                yield(last_checked, count)
                last_checked = data
                count = 1
        yield(last_checked, count)
    except StopIteration:
        pass

def rle_decode(data):
    for data, count in data:
        for _ in range(count):
            yield data