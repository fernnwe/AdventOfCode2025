from collections import defaultdict, deque
import sys

def load_graph(filename):
    graph = defaultdict(list)
    with open(filename, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.split("#", 1)[0].strip()
            if not line:
                continue
            if ":" not in line:
                continue
            src, rest = line.split(":", 1)
            src = src.strip()
            targets = [t.strip() for t in rest.split() if t.strip()]
            graph[src].extend(targets)
            for t in targets:
                if t not in graph:
                    graph[t] = []
    return graph


def reverse_graph(graph):
    rev = defaultdict(list)
    for a, outs in graph.items():
        for b in outs:
            rev[b].append(a)
    return rev


def mark_reachable(graph, target):
    rev = reverse_graph(graph)
    q = deque([target])
    reachable = {target}
    while q:
        node = q.popleft()
        for prev in rev[node]:
            if prev not in reachable:
                reachable.add(prev)
                q.append(prev)
    return reachable


def fast_count_paths(graph, start, end, must_visit):
    sys.setrecursionlimit(10000)

    # Precompute reachability for pruning
    reach_out = mark_reachable(graph, end)
    reach_dac = mark_reachable(graph, "dac")
    reach_fft = mark_reachable(graph, "fft")

    memo = {}

    def dfs(node, need_dac, need_fft):
        key = (node, need_dac, need_fft)
        if key in memo:
            return memo[key]

        # prune: cannot reach OUT
        if node not in reach_out:
            return 0

        # prune: if we still need DAC but node cannot reach DAC in future
        if need_dac and node not in reach_dac:
            return 0

        # prune: if we still need FFT but node cannot reach FFT in future
        if need_fft and node not in reach_fft:
            return 0

        # update required visits
        if node == "dac":
            need_dac = False
        if node == "fft":
            need_fft = False

        # reached OUT
        if node == end:
            return 1 if (not need_dac and not need_fft) else 0

        total = 0
        for nxt in graph[node]:
            total += dfs(nxt, need_dac, need_fft)

        memo[key] = total
        return total

    return dfs(start, "dac" in must_visit, "fft" in must_visit)

if __name__ == "__main__":
    graph = load_graph("data/day11.txt")
    result = fast_count_paths(graph, "svr", "out", {"dac", "fft"})
    print("Total paths from svr to out visiting dac and fft:", result)
