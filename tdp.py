

















































# Recursive Descent Parser (Single File)

# Input string (tokens separated by space)
input_string = "id + id * id"
tokens = input_string.split()
tokens.append("$")  # End marker

index = 0

def error():
    print("String Rejected")
    exit()

def match(expected):
    global index
    if tokens[index] == expected:
        index += 1
    else:
        error()

# Grammar functions

def E():
    print("E → T E'")
    T()
    E_prime()

def E_prime():
    global index
    if tokens[index] == "+":
        print("E' → + T E'")
        match("+")
        T()
        E_prime()
    else:
        print("E' → ε")

def T():
    print("T → F T'")
    F()
    T_prime()

def T_prime():
    global index
    if tokens[index] == "*":
        print("T' → * F T'")
        match("*")
        F()
        T_prime()
    else:
        print("T' → ε")

def F():
    global index
    if tokens[index] == "id":
        print("F → id")
        match("id")
    elif tokens[index] == "(":
        print("F → ( E )")
        match("(")
        E()
        match(")")
    else:
        error()

# Start parsing
E()

if tokens[index] == "$":
    print("\nString Accepted")
else:
    error()