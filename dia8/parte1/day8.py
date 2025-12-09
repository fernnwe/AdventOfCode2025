from itertools import product

# ---------- Leer input ----------
points = []
with open("data/day9.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            x, y = map(int, line.split(","))
            points.append((x, y))

# ---------- Crear los tiles válidos ----------
valid_tiles = set(points)  # los puntos rojos ya son válidos

# Conectar puntos consecutivos con segmentos verdes
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % len(points)]  # wrap-around
    if x1 == x2:  # línea vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            valid_tiles.add((x1, y))
    elif y1 == y2:  # línea horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
            valid_tiles.add((x, y1))
    else:
        raise ValueError("Los puntos consecutivos no están en línea recta!")

# ---------- Rasterizar el interior del polígono ----------
# Usaremos bounding box + scanline para llenar el interior
min_x = min(x for x, y in points)
max_x = max(x for x, y in points)
min_y = min(y for x, y in points)
max_y = max(y for x, y in points)

def point_in_polygon(px, py, poly):
    inside = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > py) != (yj > py)):
            x_intersect = (xj - xi) * (py - yi) / (yj - yi + 0.0) + xi
            if px < x_intersect:
                inside = not inside
        j = i
    return inside

# Llenar todos los tiles dentro del polígono como verdes
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if (x, y) not in valid_tiles and point_in_polygon(x, y, points):
            valid_tiles.add((x, y))

# ---------- Parte 1 ----------
def answer1():
    biggest = 0
    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i+1:]:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > biggest:
                biggest = area
    return biggest

# ---------- Parte 2 ----------
def answer2():
    biggest = 0
    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i+1:]:
            xmin, xmax = min(x1, x2), max(x1, x2)
            ymin, ymax = min(y1, y2), max(y1, y2)
            # Verificar si todo el rectángulo está dentro de valid_tiles
            if all((x, y) in valid_tiles for x, y in product(range(xmin, xmax + 1), range(ymin, ymax + 1))):
                area = (xmax - xmin + 1) * (ymax - ymin + 1)
                if area > biggest:
                    biggest = area
    return biggest

print("answer 1 =", answer1())
print("answer 2 =", answer2())
