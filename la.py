

















































# Simple Lexical Analyzer

# Sample source code
source_code = """
int a = 10;
float b = 20.5;
if (a < b) {
    a = a + 1;
}
"""

# Define token categories
keywords = {"int", "float", "if", "else", "while", "return"}
operators = {"+", "-", "*", "/", "=", "<", ">", "=="}
separators = {"(", ")", "{", "}", ";", ","}

tokens = []

# Function to check if number
def is_number(word):
    try:
        float(word)
        return True
    except:
        return False

# Tokenization process
words = source_code.replace("\n", " ").split()

for word in words:
    # Remove separators attached to words
    temp = ""
    for char in word:
        if char in separators:
            if temp:
                tokens.append(temp)
                temp = ""
            tokens.append(char)
        else:
            temp += char
    if temp:
        tokens.append(temp)

# Classify tokens
print("Tokens and Their Types:\n")

for token in tokens:
    if token in keywords:
        print(f"{token} : KEYWORD")
    elif token in operators:
        print(f"{token} : OPERATOR")
    elif token in separators:
        print(f"{token} : SEPARATOR")
    elif is_number(token):
        print(f"{token} : NUMBER")
    else:
        print(f"{token} : IDENTIFIER")
