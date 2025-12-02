def es_invalido(n):
    s = str(n)
    L = len(s)

    for pat_len in range(1, L // 2 + 1):
        if L % pat_len != 0:
            continue

        repeticiones = L // pat_len
        patron = s[:pat_len]

        if patron * repeticiones == s and repeticiones >= 2:
            return True

    return False


total = 0

with open("id.txt", "r") as f:
    contenido = f.read().strip()

rangos = contenido.split(",")

for r in rangos:
    if not r:
        continue

    inicio, fin = map(int, r.split("-"))

    for num in range(inicio, fin + 1):
        if es_invalido(num):
            total += num

print("Resultado :", total)
