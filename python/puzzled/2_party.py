
sched = [(6,8), (6,12), (6,7),
         (7,8), (7,10), (8,9),
         (8,10), (9,12), (9,10),
         (10,11), (10, 12), (11,12)]
    
def best_time_to_party(sched):
    flat_sched = []
    for start, end in sched:
        flat_sched.append((start, 's'))
        flat_sched.append((end, 'e'))
    
    flat_sched.sort(key=lambda x: x[0])

    max_count = -1
    current_count = 0
    best_time = -1
    for t in flat_sched:
        if t[1] == 's':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                best_time = t[0]
        else:
            current_count -= 1
    
    return best_time

print(best_time_to_party(sched))
