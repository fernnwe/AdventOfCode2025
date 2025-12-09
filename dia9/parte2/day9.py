import itertools
with open("day9.txt") as f:
    red_points = [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]
valid_points = set(red_points)

for i in range(len(red_points)):
    x1, y1 = red_points[i]
    x2, y2 = red_points[(i + 1) % len(red_points)]  # siguiente punto, con wrap
    if x1 == x2:  # misma columna
        for y in range(min(y1, y2), max(y1, y2) + 1):
            valid_points.add((x1, y))
    elif y1 == y2:  # misma fila
        for x in range(min(x1, x2), max(x1, x2) + 1):
            valid_points.add((x, y1))
    else:
        raise ValueError("Dos puntos consecutivos no están alineados en fila o columna")

def rect_inside(a, b):
    x1, y1 = a
    x2, y2 = b
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x, y) not in valid_points:
                return False
    return True
max_area = 0
for a, b in itertools.combinations(red_points, 2):
    if rect_inside(a, b):
        width = abs(a[0] - b[0]) + 1
        height = abs(a[1] - b[1]) + 1
        area = width * height
        if area > max_area:
            max_area = area

print("Largest rectangle area (Part 2):", max_area)
