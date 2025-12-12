import re
from dataclasses import dataclass
from pathlib import Path
from time import time

@dataclass
class Region:
    width: int
    length: int
    shapes: list[int]

    @property
    def could_fit(self) -> bool:
        total_cells_needed = sum(count * len(shapes[idx]) for idx, count in enumerate(self.shapes))
        return self.width * self.length >= total_cells_needed

def parse_input(blocks: list[str]) -> tuple[dict[int, set[tuple[int,int]]], list[Region]]:
    shapes = {}
    regions = []

    for block in blocks:
        lines = block.strip().split("\n")
        if lines[0].endswith(":"):
            idx = int(lines[0][:-1])
            shapes[idx] = set()
            for r, line in enumerate(lines[1:]):
                for c, char in enumerate(line):
                    if char == "#":
                        shapes[idx].add((r, c))
        else:
            for line in lines:
                numbers = list(map(int, re.findall(r"\d+", line)))
                regions.append(Region(
                    width=numbers[0],
                    length=numbers[1],
                    shapes=numbers[2:]
                ))

    return shapes, regions

if __name__ == "__main__":
    t0 = time()

    input_path = Path(__file__).parent.parent / "data" / "day12.txt"

    if not input_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {input_path}")
    with input_path.open("r", encoding="utf-8") as f:
        data = f.read().strip().split("\n\n")

    shapes, regions = parse_input(data)

    # Parte 1: cuántos regions pueden acomodar sus shapes
    answer = sum(region.could_fit for region in regions)
    print("Answer part 1:", answer)

    print("Tiempo:", round(time() - t0, 4), "s")
