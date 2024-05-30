def median(ns):
    sorted_list = sorted(ns)
    mid_index = len(sorted_list) // 2

    if len(sorted_list) % 2 == 0:
        return (sorted_list[mid_index -1] + sorted_list[mid_index]) / 2
    else:
        return sorted_list[mid_index]