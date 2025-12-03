def max_joltage(bank: str, k: int = 12) -> int:
    stack = []
    n = len(bank)
    for i, digit in enumerate(bank):
        while stack and len(stack) + (n - i) > k and stack[-1] < digit:
            stack.pop()
        if len(stack) < k:
            stack.append(digit)
    return int("".join(stack))

total = 0
with open("bateria.txt", "r", encoding="utf-8") as f:
    for line in f:
        bank = line.strip()
        if not bank:
            continue
        total += max_joltage(bank, 12)

print("Total :", total)
