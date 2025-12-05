def parse_range(line):
    start, end = line.split("-")
    return int(start), int(end)

def is_fresh(id_value, ranges):
    for start, end in ranges:
        if start <= id_value <= end:
            return True
    return False

def main():
    with open("data/ingredientes.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Separar rangos y IDs
    blank_index = lines.index("")

    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    # Parsear rangos
    ranges = [parse_range(r) for r in range_lines]

    # Parsear IDs
    ids = [int(x) for x in id_lines]

    # Contar frescos
    fresh_count = sum(1 for x in ids if is_fresh(x, ranges))

    print("Cantidad de ingredientes frescos:", fresh_count)

if __name__ == "__main__":
    main()
