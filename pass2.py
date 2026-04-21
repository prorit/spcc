

















































# Pass-2 of Two Pass Macro Processor

# ---- MNT (Macro Name Table) ----
MNT = {
    "INCR": 0
}

# ---- MDT (Macro Definition Table) ----
MDT = [
    "LDA #1",
    "ADD #2",
    "STA #1",
    "MEND"
]

# ---- Intermediate Code ----
IC = [
    "START",
    "INCR A B",
    "END"
]

print("Expanded Code:\n")

for line in IC:
    parts = line.split()
    opcode = parts[0]

    # Check if macro call
    if opcode in MNT:
        args = parts[1:] 
        mdtp = MNT[opcode]

        # Expand macro
        while MDT[mdtp] != "MEND":
            temp = MDT[mdtp]

            # Replace positional parameters
            for i, arg in enumerate(args):
                key = f"#{i+1}"
                temp = temp.replace(key, arg)

            print(temp)
            mdtp += 1

    else:
        print(line)