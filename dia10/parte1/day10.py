import re

def parse_numbers(token):
    return [int(x) for x in re.findall(r'\d+', token)]


def parse_input(path):
    machines = []
    with open(path, "r") as f:
        for line in f:
            tokens = line.strip().split()

            # lights
            lights = 0
            for i, ch in enumerate(tokens[0][1:]):
                if ch == '#':
                    lights |= (1 << i)

            # buttons
            buttons = []
            for tok in tokens[1:-1]:
                bits = 0
                for num in parse_numbers(tok):
                    bits |= (1 << num)
                buttons.append(bits)

            # joltages
            joltages = parse_numbers(tokens[-1])

            machines.append((lights, buttons, joltages))

    return machines



# Replicar next_same_bits de Rust
def next_same_bits(n):
    smallest = n & -n
    ripple = n + smallest
    ones = n ^ ripple
    next_val = (ones >> 2) // smallest
    return ripple | next_val


def part1(machines):
    total = 0

    for lights, buttons, _ in machines:
        limit = 1 << len(buttons)
        set_size = 0
        found = False

        while not found:
            set_size += 1
            n = (1 << set_size) - 1

            while n < limit:
                xor_val = 0
                # iterate positions where n has bits set
                x = n
                idx = 0
                while x:
                    if x & 1:
                        xor_val ^= buttons[idx]
                    idx += 1
                    x >>= 1

                if xor_val == lights:
                    total += set_size
                    found = True
                    break

                n = next_same_bits(n)

    return total


def part2(_machines):
    # placeholder igual que tu Rust
    return 123456789


if __name__ == "__main__":
    machines = parse_input("data/day10.txt")
    print("Part 1:", part1(machines))
    print("Part 2:", part2(machines))
