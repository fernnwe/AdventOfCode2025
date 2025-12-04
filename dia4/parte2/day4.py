def cargar_mapa():
    with open("data/rollos.txt", encoding="utf-8") as f:
        return [list(line.strip()) for line in f if line.strip()]


directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1, 0), (1, 1)
]

grid = cargar_mapa()
rows = len(grid)
cols = len(grid[0])

total_removidos = 0

while True:
    a_remover = []

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
                    a_remover.append((r, c))

    if not a_remover:
        break

    for r, c in a_remover:
        grid[r][c] = '.'

    total_removidos += len(a_remover)

print("Total de rollos removidos:", total_removidos)
