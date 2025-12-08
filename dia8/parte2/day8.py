import math
from itertools import combinations
from functools import reduce
import operator

class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True

def get_input(filename="data/day8.txt"):
    pos_data = []
    with open(filename, "r") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            pos_data.append({"x": x, "y": y, "z": z})
    return pos_data

def distance3D(a, b):
    dx = a["x"] - b["x"]
    dy = a["y"] - b["y"]
    dz = a["z"] - b["z"]
    return math.sqrt(dx*dx + dy*dy + dz*dz)

def setup(pos_data):
    memo = []
    N = len(pos_data)
    k = 0
    for i in range(N):
        for j in range(i + 1, N):
            memo.append({
                "dist": distance3D(pos_data[i], pos_data[j]),
                "a": i,
                "b": j
            })
            k += 1
    memo.sort(key=lambda e: e["dist"])
    return memo

def answer1(pos_data, memo):
    uf = UF(len(pos_data))
    N = len(pos_data)
    # Igual que Lua: solo las primeras N aristas
    for i in range(N):
        e = memo[i]
        uf.union(e["a"], e["b"])
    
    sizes = {}
    for i in range(len(pos_data)):
        r = uf.find(i)
        sizes[r] = sizes.get(r, 0) + 1

    largest = sorted(sizes.values(), reverse=True)
    while len(largest) < 3:
        largest.append(1)
    
    return largest[0] * largest[1] * largest[2]

def answer2(pos_data, memo):
    uf = UF(len(pos_data))
    components = len(pos_data)
    
    for e in memo:
        if uf.union(e["a"], e["b"]):
            components -= 1
            if components == 1:
                return pos_data[e["a"]]["x"] * pos_data[e["b"]]["x"]
    return -1

if __name__ == "__main__":
    pos_data = get_input("data/day8.txt")
    memo = setup(pos_data)
    print("Answer 1:", answer1(pos_data, memo))
    print("Answer 2:", answer2(pos_data, memo))
