def get_input():
    with open("data/day7.txt", "r") as f:
        # Cada línea se convierte en lista de caracteres
        return [list(line.strip()) for line in f.readlines()]

def answer1():
    grid = get_input()
    total = 0
    H = len(grid)
    W = len(grid[0])
    
    for y in range(H - 1):
        for x in range(1, W - 1):
            char = grid[y][x]
            if char == "S" and grid[y + 1][x] == ".":
                grid[y + 1][x] = "|"
            elif char == "|":
                if grid[y + 1][x] == "^":
                    if x > 0:
                        grid[y + 1][x - 1] = "|"
                    if x < W - 1:
                        grid[y + 1][x + 1] = "|"
                    total += 1
                elif grid[y + 1][x] == ".":
                    grid[y + 1][x] = "|"
    return total

def answer2():
    grid = get_input()
    H = len(grid)
    W = len(grid[0])
    
    ways = [[0] * W for _ in range(H)]
    total = 0
    
    for y in range(H):
        for x in range(W):
            char = grid[y][x]
            
            if char == "S":
                ways[y][x] = 1
            elif char == "." and y > 0:
                ways[y][x] += ways[y - 1][x]
            elif char == "^" and y > 0:
                if x > 0:
                    ways[y][x - 1] += ways[y - 1][x]
                else:
                    total += ways[y][x]
                if x < W - 1:
                    ways[y][x + 1] += ways[y - 1][x]
                else:
                    total += ways[y][x]
            
            if y == H - 1:
                total += ways[y][x]
    
    return total

if __name__ == "__main__":
    print("Answer 1:", answer1())
    print("Answer 2:", answer2())
