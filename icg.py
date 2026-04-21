

















































# Intermediate Code Generation (Three Address Code)

# Input expression
# expression = "a = b + c * d"
expression = input("Enter an expression: ")

# Split into LHS and RHS
lhs, rhs = expression.split("=")
lhs = lhs.strip()
rhs = rhs.strip()

# Operator precedence
precedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

operators = set(precedence.keys())

# Convert expression to postfix (Shunting Yard)
def infix_to_postfix(expr):
    stack = []
    output = []
    tokens = expr.split()

    for token in tokens:
        if token not in operators:
            output.append(token)
        else:
            while (stack and stack[-1] in operators and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

# Generate TAC
def generate_TAC(postfix):
    stack = []
    temp_count = 1

    print("Three Address Code:\n")

    for token in postfix:
        if token not in operators:
            stack.append(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f"t{temp_count}"
            print(f"{temp} = {op1} {token} {op2}")
            stack.append(temp)
            temp_count += 1

    # Final assignment
    print(f"{lhs} = {stack.pop()}")

# Execution
postfix = infix_to_postfix(rhs)
generate_TAC(postfix)
