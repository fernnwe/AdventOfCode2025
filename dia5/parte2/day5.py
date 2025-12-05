def parse_range(line):
    start, end = line.split("-")
    return int(start), int(end)

def merge_ranges(ranges):
    # Ordenar los rangos por inicio
    ranges.sort()
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        # Si se solapa o toca, unirlos
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged

def main():
    with open("data/ingredientes.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Separar rangos (antes de la línea en blanco)
    blank_index = lines.index("")
    range_lines = lines[:blank_index]

    # Parsear rangos
    ranges = [parse_range(r) for r in range_lines]

    # Fusionar rangos
    merged = merge_ranges(ranges)

    # Contar IDs frescos
    total_fresh = sum((end - start + 1) for start, end in merged)

    print("Total de ingredient IDs frescos según los rangos:", total_fresh)

if __name__ == "__main__":
    main()
