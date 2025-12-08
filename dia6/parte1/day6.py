def load_input(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    return lines


def build_grid(lines):
    H = len(lines)
    W = max(len(line) for line in lines)

    # normalizar ancho con espacios
    lines = [line.ljust(W) for line in lines]

    grid = [list(line) for line in lines]
    return grid, H, W


def is_empty_column(grid, x, H):
    for y in range(H):
        if grid[y][x] != " ":
            return False
    return True


def find_groups(grid, H, W):
    groups = []
    x = 0
    while x < W:
        if is_empty_column(grid, x, H):
            x += 1
        else:
            L = x
            while x < W and not is_empty_column(grid, x, H):
                x += 1
            R = x - 1
            groups.append((L, R))
    return groups


def answer1(grid, groups, H):
    total = 0

    for L, R in groups:
        op = None
        # buscar operador en la última fila (fila H-1)
        for x in range(L, R + 1):
            c = grid[H - 1][x]
            if c in ['+', '*']:
                op = c
                break

        if op:
            nums = []
            # cada fila (0..H-2) puede contener un número
            for y in range(H - 1):
                substr = ''.join(grid[y][x] for x in range(L, R + 1))
                digits = substr.replace(" ", "")
                if digits != "":
                    try:
                        nums.append(int(digits))
                    except:
                        pass

            if nums:
                if op == "+":
                    acc = sum(nums)
                else:
                    acc = 1
                    for n in nums:
                        acc *= n

                total += acc

    return total


def answer2(grid, groups, H):
    total = 0

    for L, R in groups:
        op = None
        # operador en la fila inferior
        for x in range(L, R + 1):
            c = grid[H - 1][x]
            if c in ['+', '*']:
                op = c
                break

        if op:
            nums = []

            # cada columna (de derecha a izquierda) es un número vertical
            for x in range(R, L - 1, -1):
                digits = ""
                for y in range(H - 1):
                    c = grid[y][x]
                    if c.isdigit():
                        digits += c

                if digits != "":
                    try:
                        nums.append(int(digits))
                    except:
                        pass

            if nums:
                if op == "+":
                    acc = sum(nums)
                else:
                    acc = 1
                    for n in nums:
                        acc *= n

                total += acc

    return total


def solve_day6(filename="data/total.txt"):
    lines = load_input(filename)
    grid, H, W = build_grid(lines)
    groups = find_groups(grid, H, W)

    part1 = answer1(grid, groups, H)
    part2 = answer2(grid, groups, H)

    print("The answer 1 is:", part1)
    print("The answer 2 is:", part2)


if __name__ == "__main__":
    solve_day6("data/total.txt")
