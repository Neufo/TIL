
def recursive_tile(yard, size, originR, originC, rMiss, cMiss, nextPiece):
    quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)
    if size == 2:
        piecePos = [(0, 0), (0, 1), (1, 0), (1, 1)]
        piecePos.pop(quadMiss)
        for (r, c) in piecePos:
            yard[originR + r][originC + c] = nextPiece
        nextPiece += 1
        return nextPiece
    for quad in range(4):
        shiftR = size//2 * (quad >= 2)
        shiftC = size//2 * (quad % 2 == 1)
        if quad == quadMiss:
            nextPiece = recursive_tile(yard, size//2, originR + shiftR,
                                       originC + shiftC, rMiss - shiftR, cMiss - shiftC, nextPiece)
        else:
            newrMiss = (size//2 - 1) * (quad < 2)
            newcMiss = (size//2 - 1) * (quad % 2 == 0)
            nextPiece = recursive_tile(yard, size//2, originR + shiftR,
                                       originC + shiftC, newrMiss, newcMiss, nextPiece)
    centerPos = [(r + size//2 - 1, c + size//2 - 1)
                 for (r, c) in [(0, 0), (0, 1), (1, 0), (1, 1)]]
    centerPos.pop(quadMiss)
    for (r, c) in centerPos:
        yard[originR + r][originC + c] = nextPiece
    nextPiece += 1
    return nextPiece
