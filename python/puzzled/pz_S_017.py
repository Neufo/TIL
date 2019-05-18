
N, M, S = input().split()
N, M, S = int(N), int(M), int(S)

stage = []
for _ in range(N):
    s = input()
    stage.append(list(s))


def fill_rect(x, y, c, size, stage):
    for iy in range(x, size):
        for ix in range(y, size):
            stage[iy][ix] = c


def tear_off(stage):
    for y in range(N-M):
        for x in range(N-M):
            square = True
            for iy in range(1, M):
                for ix in range(1, M):
                    if stage[y][x] != stage[y+iy][x+ix] and stage[iy][ix] != '_':
                        square = False
                        break
                if not square:
                    break

            if square:
                fill_rect(x, y, '_', M, stage)
                return (stage[x][y], x, y)


current = (-1, -1)
log = []
for _ in range(S):
    l = tear_off(stage)
    log.append(l)

for l in log:
    print(*l)
