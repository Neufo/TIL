def found(s, target):
    upper = len(s)
    skip_count = 0
    for i in range(upper - len(target) + 1):
        i_s = i
        i_t = 0
        while i_s < upper:
            if s[i_s] == target[i_t]:
                i_t += 1
                i_s += 1
            elif skip_count == 0 and i_t > 0:
                skip_count += 1
            else:
                break

            if i_t == len(target):
                return True

    return False


N = int(input())
S = input()

for _ in range(N):
    s = input()
    result = found(s, S)
    print('valid' if result else 'invalid')
