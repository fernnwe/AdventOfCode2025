# Advent of Code - Dia 4 - parte 1
with open("data/rollos.txt") as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1, 0), (1, 1)
]

accesibles = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            vecinos = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        vecinos += 1
            
            if vecinos < 4:
                accesibles += 1

print("Rollos accesibles:", accesibles)
