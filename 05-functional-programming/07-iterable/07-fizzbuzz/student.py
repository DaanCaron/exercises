def fizzbuzz():
    current = 1
    while True:
        result = ""
        if current % 3 == 0:
            result += "fizz"
        if current % 5 == 0:
            result += "buzz"
        yield result or str(current)
        current += 1