

















































# Pass-1 of Two Pass Macro Processor

# Input program
input_code = [
    "MACRO",
    "INCR &ARG1,&ARG2",
    "A 1,&ARG1",
    "L 2,&ARG2",
    "MEND",
    "START",
    "INCR A,B",
    "END"
]

MDT = []   # Macro Definition Table
MNT = []   # Macro Name Table
PNTAB = {} # Parameter Name Table

MDTC = 0
MNTC = 0

i = 0
while i < len(input_code):
    line = input_code[i]

    if line == "MACRO":
        i += 1
        header = input_code[i]

        parts = header.split()
        macro_name = parts[0]

        # Extract parameters
        params = header[len(macro_name):].strip()
        param_list = []

        temp = ""
        for ch in params:
            if ch in [',', ' ']:
                if temp:
                    param_list.append(temp)
                    temp = ""
            else:
                temp += ch
        if temp:
            param_list.append(temp)

        # Build PNTAB
        PNTAB.clear()
        for idx, param in enumerate(param_list):
            PNTAB[param] = idx + 1

        # Add to MNT
        MNT.append((macro_name, MDTC))
        MNTC += 1

        # Add header to MDT
        MDT.append(header)
        MDTC += 1

        # Process macro body
        while True:
            i += 1
            body = input_code[i]

            if body == "MEND":
                MDT.append("MEND")
                MDTC += 1
                break

            # Replace parameters with positional notation
            for param, pos in PNTAB.items():
                body = body.replace(param, f"#{pos}")

            MDT.append(body)
            MDTC += 1

    else:
        print(line)  # Non-macro lines (Intermediate Code)

    i += 1

# Print MNT
print("\nMNT:")
for name, index in MNT:
    print(name, index)

# Print MDT
print("\nMDT:")
for idx, line in enumerate(MDT):
    print(idx, line)