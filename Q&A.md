# 🎓 Viva Questions & Answers (System Programming & Compiler Design)

## 📦 Module 1: Introduction to System Software

### 1. What is system software?
System software is a set of programs designed to manage and control computer hardware and provide a platform for running application software. It acts as an interface between hardware and users, ensuring efficient execution of tasks. Examples include operating systems, compilers, assemblers, and device drivers.

### 2. What are the goals of system software?
The main goals of system software are to provide a convenient environment for users, ensure efficient utilization of hardware resources, and improve system performance. It also aims to abstract hardware complexity and support application development.

### 3. Differentiate between system programming and application programming.
System programming involves developing system-level software such as compilers, assemblers, and OS components, focusing on hardware interaction and efficiency. Application programming, on the other hand, deals with creating user-oriented programs like web apps or mobile apps, focusing on functionality and user experience.

### 4. What are system programs?
System programs are utilities that provide essential services to users and other programs. They include tools like assemblers, compilers, loaders, linkers, editors, and debuggers, which help in program development and execution.

### 5. What is an assembler?
An assembler is a translator that converts assembly language instructions into machine-level instructions. It replaces symbolic names with actual addresses and generates object code that can be executed by the processor.

### 6. Difference between compiler and interpreter.
A compiler translates the entire source code into machine code before execution, resulting in faster execution but requiring more memory. An interpreter translates and executes the program line-by-line, making debugging easier but execution slower.

### 7. What is a linker?
A linker is a system program that combines multiple object files into a single executable file. It resolves external references and links library functions to the main program.

### 8. What is a loader?
A loader is responsible for loading the executable program into memory and preparing it for execution. It also performs address relocation and resolves remaining references.

---

## ⚙️ Module 2: Assemblers

### 9. What are the basic elements of assembly language?
Assembly language consists of mnemonic opcodes (like MOV, ADD), symbolic operands (registers or memory), labels (for referencing addresses), and directives such as DC (Define Constant) and DS (Define Storage) used for data definition.

### 10. What is a two-pass assembler?
A two-pass assembler processes the program in two phases. In Pass-1, it scans the code to build the symbol and literal tables and assigns addresses using the location counter. In Pass-2, it generates the final machine code by resolving all symbols and literals.

### 11. What is the role of Location Counter (LC)?
The Location Counter keeps track of the memory address of each instruction during assembly. It is updated sequentially as instructions are processed and helps in assigning addresses to labels and variables.

### 12. What is a symbol table?
A symbol table is a data structure used by the assembler to store symbols (labels) along with their addresses and attributes. It is essential for resolving symbol references during code generation.

### 13. What is a literal?
A literal is a constant value specified directly in the instruction, such as `='5'`. Literals are stored in a literal table and assigned addresses during assembly, usually at the end or at LTORG.

### 14. What is forward reference?
A forward reference occurs when a symbol is used before it is defined in the program. Since its address is not known initially, it must be resolved later.

### 15. How are forward references handled?
Forward references are handled in two-pass assemblers during the second pass when symbol addresses are known. In single-pass assemblers, techniques like backpatching are used to fill missing addresses later.

### 16. What is a single-pass assembler?
A single-pass assembler processes the source code only once. It generates machine code immediately but must handle forward references using techniques like backpatching, making it more complex than a two-pass assembler.

---

## 🧩 Module 3: Macros and Macro Processor

### 17. What is a macro?
A macro is a user-defined sequence of instructions grouped under a single name. It allows reuse of code and reduces repetition, improving program readability and maintainability.

### 18. What is macro expansion?
Macro expansion is the process of replacing a macro call with its corresponding sequence of instructions (macro body) during program processing.

### 19. What are positional parameters?
Positional parameters are arguments passed to a macro in a fixed order. The values are substituted based on their position in the macro definition.

### 20. What are keyword parameters?
Keyword parameters are arguments passed using name-value pairs, allowing flexibility in the order of parameters and making macros more readable and user-friendly.

### 21. What is a Macro Name Table (MNT)?
Macro Name Table (MNT) is a data structure used in a macro processor to store the names of macros along with pointers to their definitions in the Macro Definition Table (MDT). It helps in locating the macro definition during macro expansion.

### 22. What is a Macro Definition Table (MDT)?
MDT stores the actual body (instructions) of all macros. When a macro is called, the processor uses the MDT to retrieve and expand the macro definition into the source program.

### 23. What is a parameterized macro?
A parameterized macro is a macro that accepts parameters (arguments) so that the same macro can be reused with different values, increasing flexibility and reducing redundancy.

### 24. What is conditional macro expansion?
Conditional macro expansion allows execution of specific parts of a macro based on conditions. It uses directives like AIF (conditional jump) and AGO (unconditional jump) to control expansion flow.

---

## 🔗 Module 4: Loaders and Linkers

### 25. What are the main functions of a loader?
The loader performs four main functions: allocation (assign memory), linking (resolve external references), relocation (adjust addresses), and loading (place the program into memory for execution).

### 26. What is relocation?
Relocation is the process of modifying address-dependent instructions so that a program can be loaded at different memory locations without affecting its execution.

### 27. What is linking?
Linking is the process of combining different object modules and resolving external references between them to create a complete executable program.

### 28. What is an absolute loader?
An absolute loader loads a program into a fixed memory location specified by the assembler. It does not perform relocation, making it simple but less flexible.

### 29. What is a relocating loader?
A relocating loader adjusts address-dependent instructions so that the program can be loaded at any memory location. It provides flexibility in memory usage.

### 30. What is a direct linking loader?
A direct linking loader links multiple object modules directly during loading. It uses structures like External Symbol Dictionary (ESD) and Relocation and Linkage Directory (RLD) for resolving references.

### 31. What is dynamic linking?
Dynamic linking is performed at runtime instead of compile time. Required modules are loaded only when needed, reducing memory usage and improving efficiency.

### 32. Difference between static and dynamic linking.
Static linking combines all modules before execution, increasing program size. Dynamic linking loads modules during execution, reducing memory usage and improving modularity.

---

## 🧠 Module 5: Compilers – Analysis Phase

### 33. What are the phases of a compiler?
The compiler has several phases: lexical analysis, syntax analysis, semantic analysis, intermediate code generation, code optimization, and code generation. The first three form the analysis phase.

### 34. What is lexical analysis?
Lexical analysis is the first phase of a compiler that scans source code and converts it into tokens such as keywords, identifiers, operators, and constants.

### 35. What is a token?
A token is the smallest meaningful unit in a program, consisting of a token type and its lexeme. For example, `int`, `a`, and `=` are tokens.

### 36. What is the role of Finite State Automata (FSA) in lexical analysis?
Finite State Automata are used to recognize patterns in input strings. They help in identifying tokens like identifiers and numbers efficiently.

### 37. What data structures are used in lexical analysis?
Common data structures include symbol tables (to store identifiers), buffers (to store input), and transition tables for finite automata.

### 38. What is syntax analysis?
Syntax analysis (parsing) checks whether the sequence of tokens follows the grammatical rules of the programming language. It builds a parse tree or syntax tree.

### 39. What is Context-Free Grammar (CFG)?
CFG is a set of production rules used to define the syntax of programming languages. It consists of terminals, non-terminals, start symbol, and production rules.

### 40. What is the difference between top-down and bottom-up parsing?
Top-down parsing starts from the start symbol and tries to derive the input string, while bottom-up parsing starts from the input string and reduces it to the start symbol.

### 41. What is an LL(1) parser?
An LL(1) parser is a top-down predictive parser that reads input from Left to right, produces a Leftmost derivation, and uses 1 lookahead token. It does not require backtracking and uses a parsing table to decide production rules.

### 42. What is a shift-reduce parser?
A shift-reduce parser is a bottom-up parser that uses two main operations: **shift** (push input onto stack) and **reduce** (apply grammar rules to reduce symbols). It works by reducing the input string to the start symbol.

### 43. What is an operator precedence parser?
It is a type of bottom-up parser that uses precedence relations between operators to parse expressions. It is mainly used for arithmetic expressions where operator priority matters.

### 44. What is an SLR parser?
SLR (Simple LR) parser is a type of bottom-up parser that uses LR parsing techniques with a parsing table constructed using FOLLOW sets. It is more powerful than LL(1) but simpler than full LR parsers.

### 45. What is semantic analysis?
Semantic analysis checks the meaning of the program after syntax analysis. It ensures type correctness, variable declaration, scope resolution, and logical consistency of the program.

### 46. What is type checking?
Type checking ensures that operations in a program are applied to compatible data types, such as not adding an integer to a string.

### 47. What is a syntax-directed definition (SDD)?
SDD is a method of associating semantic rules with grammar productions. It helps in translation and intermediate code generation during parsing.

---

## ⚙️ Module 6: Compilers – Synthesis Phase

### 48. What is intermediate code generation?
It is the phase where source code is converted into a machine-independent intermediate representation (IR), making it easier to optimize and generate target code.

### 49. What are the types of intermediate code?
Common types include syntax trees, postfix notation, and three-address code (TAC). TAC can be represented as triples, quadruples, and indirect triples.

### 50. What is Three Address Code (TAC)?
TAC is an intermediate code format where each instruction contains at most three operands. It simplifies complex expressions into simpler steps using temporary variables.

### 51. What is a quadruple representation?
A quadruple consists of four fields: operator, operand1, operand2, and result. It explicitly stores the result in a separate field.

### 52. What is a triple representation?
A triple stores operator and operands but does not explicitly store the result; instead, it refers to the result using the instruction index.

### 53. What is code optimization?
Code optimization improves the efficiency of intermediate code without changing its output. It aims to reduce execution time and memory usage.

### 54. What are machine-independent optimizations?
These optimizations do not depend on target architecture. Examples include constant folding, dead code elimination, and common subexpression elimination.

### 55. What are machine-dependent optimizations?
These depend on target machine architecture. Examples include register allocation and peephole optimization.

### 56. What is peephole optimization?
It is a machine-dependent optimization technique that examines a small set of instructions and replaces inefficient patterns with more efficient ones.

### 57. What is code generation?
Code generation is the final phase of the compiler where intermediate code is converted into target machine code, considering registers, memory, and instruction set.

### 58. What is a basic block?
A basic block is a sequence of consecutive instructions with a single entry point and a single exit point, with no branching in between.

### 59. What is a flow graph?
A flow graph represents control flow between basic blocks. Nodes represent blocks, and edges represent control transfer.

### 60. Why is code optimization important?
Code optimization improves performance, reduces execution time, minimizes memory usage, and enhances overall efficiency of the program.