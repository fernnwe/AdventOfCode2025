from collections import defaultdict

def load_graph(filename):
    graph = defaultdict(list)
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue
            src, rest = line.split(":")
            src = src.strip()
            targets = rest.strip().split()
            graph[src] = targets
    return graph


def count_paths(graph, start, end):
    memo = {}

    def dfs(node):
        if node == end:
            return 1
        if node in memo:
            return memo[node]

        total = 0
        for nxt in graph[node]:
            total += dfs(nxt)

        memo[node] = total
        return total

    return dfs(start)


if __name__ == "__main__":
    graph = load_graph("data/day11.txt")
    result = count_paths(graph, "you", "out")
    print("Total paths from you to out:", result)
