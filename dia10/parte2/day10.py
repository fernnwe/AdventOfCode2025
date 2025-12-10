from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, PULP_CBC_CMD

def parse_line(line):
    # Separar botones y objetivos
    lights_part, rest = line.split('] ')
    buttons_part, target_part = rest.rsplit(' {', 1)
    target = list(map(int, target_part.rstrip('}').split(',')))

    # Parsear botones
    buttons = []
    for btn in buttons_part.split(' '):
        if not btn:
            continue
        btn = btn.strip('()')
        indices = list(map(int, btn.split(',')))
        buttons.append(indices)
    return buttons, target

def min_presses_glpk(buttons, target):
    n_buttons = len(buttons)
    n_counters = len(target)
    
    prob = LpProblem("MinPulses", LpMinimize)
    btn_vars = [LpVariable(f"btn_{i}", lowBound=0, cat=LpInteger) for i in range(n_buttons)]
    for counter_idx in range(n_counters):
        prob += lpSum(btn_vars[i] for i, btn in enumerate(buttons) if counter_idx in btn) == target[counter_idx]
    prob += lpSum(btn_vars)

    # usando GLPK (GRACIAS DEYBIS XD)
    prob.solve()

    # OBTENEMOS EL RESULTADO
    return int(sum(var.varValue for var in btn_vars))

def min_total_presses(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            buttons, target = parse_line(line)
            presses = min_presses_glpk(buttons, target)
            total += presses
    return total

if __name__ == "__main__":
    filename = "data/day10.txt"
    result = min_total_presses(filename)
    print(result)
