def keys_with_value(dictionry, value):
    result = []
    for k, v in dictionry.items():
        if v == value:
            result.append(k)
    return result