
def trace_back(row, table):
    if len(row) == 0:
        return 0, table
    elif len(row) == 1:
        return row[0], table + [row[0]]

    take = trace_back(row[2:], table)
    skip = trace_back(row[1:], table)

    if take[0] + row[0] > skip[0]:
        return take[0] + row[0], take[1] + [row[0]]
    else:
        return skip[0], skip[1]


coins = [14, 3, 27, 4, 5, 15, 1]

print(trace_back(coins, []))
