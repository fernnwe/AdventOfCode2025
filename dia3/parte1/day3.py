def max_two_digit_from_bank(bank: str) -> int:
    digits = [int(c) for c in bank]
    n = len(digits)
    if n < 2:
        return 0
    suffix_max = [0] * n
    current = -1
    for i in range(n - 1, -1, -1):
        suffix_max[i] = current
        if digits[i] > current:
            current = digits[i]

    best = 0
    for i in range(n - 1):
        if suffix_max[i] != -1:
            candidate = 10 * digits[i] + suffix_max[i]
            if candidate > best:
                best = candidate

    return best

total = 0
with open("bateria.txt", "r", encoding="utf-8") as f:
    for line in f:
        bank = line.strip()
        if not bank:
            continue
        total += max_two_digit_from_bank(bank)

print("Total output joltage:", total)
