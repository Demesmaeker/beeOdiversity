def qtt_pesticides(row, *args):
    total = 0
    for arg in args:
        if row[arg] > 0:
            total += row[arg]
    return total


def nb_pesticides(row, *args):
    total = 0
    for arg in args:
        if row[arg] > 0:
            total += 1
    return total