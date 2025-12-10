from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Rect:
    min: Point
    max: Point

    def canon(self):
        return Rect(
            Point(min(self.min.x, self.max.x), min(self.min.y, self.max.y)),
            Point(max(self.min.x, self.max.x), max(self.min.y, self.max.y)),
        )

    def add1(self):
        return Rect(self.min, Point(self.max.x + 1, self.max.y + 1))

    def dx(self):
        return self.max.x - self.min.x

    def dy(self):
        return self.max.y - self.min.y

    def inset1(self):
        return Rect(
            Point(self.min.x + 1, self.min.y + 1),
            Point(self.max.x - 1, self.max.y - 1)
        )

    def overlaps(self, other):
        return not (
            self.max.x <= other.min.x or
            self.min.x >= other.max.x or
            self.max.y <= other.min.y or
            self.min.y >= other.max.y
        )

def read_points():
    points = []
    with open("data/day9.txt") as f:
        for token in f.read().split():
            x, y = map(int, token.split(","))
            points.append(Point(x, y))
    return points

def main():
    points = read_points()

    rects = []
    lines = []

    # Generate all rectangles from red points
    for i, p in enumerate(points):
        for q in points[:i]:
            rects.append(Rect(p, q).canon())

        if i > 0:
            lines.append(Rect(points[i - 1], points[i]).canon())

    # Close loop
    lines.append(Rect(points[-1], points[0]).canon())

    part1 = 0
    part2 = 0

    for r in rects:
        r2 = r.add1()  # expand
        area = r2.dx() * r2.dy()

        # track part1
        if area > part1:
            part1 = area

        if area <= part2:
            continue

        # check if ANY line overlaps inset rectangle
        inset = r2.inset1()
        bad = False
        for l in lines:
            if l.add1().overlaps(inset):
                bad = True
                break

        if not bad:
            part2 = area

    print("Part 2:", part2)

if __name__ == "__main__":
    main()
