# Parte 2 - Contar cada vez que el dial pasa por 0

with open("input.txt") as f:
    rotations = [line.strip() for line in f.readlines()]

dial = 50
zero_count = 0
size = 100

for rotation in rotations:
    direction = rotation[0]
    steps = int(rotation[1:])

    if direction == 'R':
        for _ in range(steps):
            dial = (dial + 1) % size
            if dial == 0:
                zero_count += 1
    else:
        for _ in range(steps):
            dial = (dial - 1) % size
            if dial == 0:
                zero_count += 1

print("RESULTADO:", zero_count)
