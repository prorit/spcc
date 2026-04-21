

















































# Code Optimization (4 Techniques in One File)

# Input Three Address Code (TAC)
code = [
    "t1 = 5 + 3",
    "t2 = t1 + 0",
    "t3 = t1 + 0",
    "t4 = t2",
    "a = t4",
    "b = 10",
    "c = b + 2",
    "d = b + 2"
]

print("Original Code:\n")
for line in code:
    print(line)

# -------------------------------
# 1. Constant Folding
# -------------------------------
def constant_folding(code):
    new_code = []
    for line in code:
        parts = line.split()
        if len(parts) == 5:
            if parts[2].isdigit() and parts[4].isdigit():
                result = eval(parts[2] + parts[3] + parts[4])
                new_code.append(f"{parts[0]} {parts[1]} {result}")
            else:
                new_code.append(line)
        else:
            new_code.append(line)
    return new_code

# -------------------------------
# 2. Constant Propagation
# -------------------------------
def constant_propagation(code):
    const_table = {}
    new_code = []

    for line in code:
        parts = line.split()

        if len(parts) == 3 and parts[2].isdigit():
            const_table[parts[0]] = parts[2]
            new_code.append(line)
        else:
            for var in const_table:
                if var in line:
                    line = line.replace(var, const_table[var])
            new_code.append(line)

    return new_code

# -------------------------------
# 3. Common Subexpression Elimination
# -------------------------------
def common_subexpression(code):
    expr_table = {}
    new_code = []

    for line in code:
        parts = line.split()
        if len(parts) == 5:
            expr = parts[2] + parts[3] + parts[4]
            if expr in expr_table:
                new_code.append(f"{parts[0]} = {expr_table[expr]}")
            else:
                expr_table[expr] = parts[0]
                new_code.append(line)
        else:
            new_code.append(line)

    return new_code

# -------------------------------
# 4. Dead Code Elimination
# -------------------------------
def dead_code_elimination(code):
    used = set()
    new_code = []

    # Find used variables
    for line in code:
        parts = line.split()
        if len(parts) >= 3:
            used.update(parts[2:])

    # Remove unused assignments
    for line in code:
        parts = line.split()
        if parts[0] in used or parts[0] in ['a', 'b', 'c', 'd']:
            new_code.append(line)

    return new_code

# Apply optimizations step by step
code = constant_folding(code)
code = constant_propagation(code)
code = common_subexpression(code)
code = dead_code_elimination(code)

# Output optimized code
print("\nOptimized Code:\n")
for line in code:
    print(line)
