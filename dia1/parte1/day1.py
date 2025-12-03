def solve_day1():
    position = 50
    count_zero = 0
    
    with open("data/input.txt", "r") as f:
        lines = f.read().strip().splitlines()

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        # Rotación hacia la izquierda 
        if direction == "L":
            position = (position - distance) % 100

        # Rotación hacia la derecha
        else:
            position = (position + distance) % 100

        if position == 0:
            count_zero += 1

    print("PASSWORD:", count_zero)


if __name__ == "__main__":
    solve_day1()
