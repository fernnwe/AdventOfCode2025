def parse_input(path):
    points = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(int, line.split(","))
            points.append((x, y))
    return points

def largest_rectangle(points):
    max_area = 0
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            width = abs(x2 - x1) + 1   # INCLUSIVO
            height = abs(y2 - y1) + 1  # INCLUSIVO

            area = width * height

            if area > max_area:
                max_area = area

    return max_area

def main():
    points = parse_input("data/day9.txt")
    res = largest_rectangle(points)
    print("Largest rectangle area:", res)

if __name__ == "__main__":
    main()
