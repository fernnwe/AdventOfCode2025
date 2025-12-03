def es_invalido(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mitad = len(s) // 2
    return s[:mitad] == s[mitad:]


total = 0

with open("data/id.txt", "r") as f:
    contenido = f.read().strip()

rangos = contenido.split(",")

for r in rangos:
    if not r:
        continue

    inicio, fin = map(int, r.split("-"))

    for num in range(inicio, fin + 1):
        if es_invalido(num):
            total += num

print("Resultado final:", total)
