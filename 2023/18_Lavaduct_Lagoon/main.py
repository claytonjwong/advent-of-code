# https://en.wikipedia.org/wiki/Shoelace_formula
segments = lambda V: zip(V, V[1:] + [V[0]])
shoelace = lambda V: abs(sum((x1 * y2) - (x2 * y1) for ((x1, y1), (x2, y2)) in segments(V))) // 2

def run(part1=True):
    i, j = 0, 0
    V, P = [(i, j)], 0  # Vertices, Perimeter
    with open('input.txt') as input:
        for line in input:
            d, step, color = line.split(); step = int(step)
            if not part1:
                step, last = int(color[2:-2], 16), int(color[-2])
                d = 'R' if last == 0 else 'D' if last == 1 else 'L' if last == 2 else 'U'
            di, dj = (-1, 0) if d == 'U' else (1, 0) if d == 'D' else (0, -1) if d == 'L' else (0, 1)
            i += di * step
            j += dj * step
            V.append((i, j)); P += step
    return shoelace(V) + (P // 2) + 1

print(f'part 1: {run(True)}')
print(f'part 2: {run(False)}')
# part 1: 47045
# part 2: 147839570293376
