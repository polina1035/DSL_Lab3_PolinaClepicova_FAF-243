
### 4. REPORT.md


# Laboratory Work Report: Lexer & Scanner

## Course: Formal Languages & Finite Automata
## Author: [Your Name]
## Date: March 2026

## Topic: Lexical Analysis (Lexer/Scanner)

### Objectives

1. Understand what lexical analysis is
2. Get familiar with the inner workings of a lexer/scanner/tokenizer
3. Implement a sample lexer and demonstrate how it works

### Theoretical Background

**Lexical analysis** is the process of converting a sequence of characters into a sequence of tokens. It is the first phase of a compiler or interpreter.

Key concepts:
- **Lexeme**: A sequence of characters that forms a unit of the language
- **Token**: A pair consisting of a token type and the lexeme value
- **Lexer** (tokenizer/scanner): A program that performs lexical analysis

The lexer reads the input character by character, groups them into lexemes, and produces tokens. It also removes whitespace and comments, and tracks line numbers for error reporting.

### Implementation

I implemented a lexer for mathematical expressions with the following token types:

#### Token Categories:

1. **Numbers**:
   - `INT`: Integer numbers (e.g., 42, 0, 123)
   - `FLOAT`: Floating-point numbers (e.g., 3.14, 0.5, 2.0)

2. **Operators**:
   - `PLUS`: Addition (+)
   - `MINUS`: Subtraction (-)
   - `MULTIPLY`: Multiplication (*)
   - `DIVIDE`: Division (/)
   - `POWER`: Exponentiation (^)
   - `ASSIGN`: Assignment (=)

3. **Trigonometric Functions**:
   - `SIN`: Sine function (sin)
   - `COS`: Cosine function (cos)

4. **Constants**:
   - `PI`: π (pi)
   - `E`: Euler's number (e)

5. **Delimiters**:
   - `LPAREN`: Left parenthesis '('
   - `RPAREN`: Right parenthesis ')'
   - `COMMA`: Comma ','

6. **Special**:
   - `EOF`: End of file
   - `ILLEGAL`: Illegal character
   - `IDENT`: Generic identifier

#### Key Methods:

| Method | Description |
|--------|-------------|
| `read_char()` | Reads the next character from input |
| `peek_char()` | Looks at the next character without consuming it |
| `skip_whitespace()` | Skips spaces, tabs, and newlines |
| `read_number()` | Reads integers and floats |
| `read_identifier()` | Reads identifiers and keywords |
| `next_token()` | Returns the next token |
| `tokenize()` | Tokenizes the entire input |

### Testing Results

The lexer was tested with various expressions:

#### Test 1: Simple Arithmetic
Input: "3 + 4 * 2"
Output: Token(INT, '3', line=1, col=1)
Token(PLUS, '+', line=1, col=3)
Token(INT, '4', line=1, col=5)
Token(MULTIPLY, '*', line=1, col=7)
Token(INT, '2', line=1, col=9)
Token(EOF, '', line=1, col=10)

#### Test 2: Trigonometric Functions
 Input: "sin(pi/2) + cos(0)"
 Output: Token(SIN, 'sin', line=1, col=1)
 Token(LPAREN, '(', line=1, col=4)
 Token(PI, 'pi', line=1, col=5)
 Token(DIVIDE, '/', line=1, col=7)
 Token(INT, '2', line=1, col=8)
 Token(RPAREN, ')', line=1, col=9)
 Token(PLUS, '+', line=1, col=11)
 Token(COS, 'cos', line=1, col=13)
 Token(LPAREN, '(', line=1, col=16)
 Token(INT, '0', line=1, col=17)
 Token(RPAREN, ')', line=1, col=18)
 Token(EOF, '', line=1, col=19)

#### Test 3: Floating Point Numbers
Input: "3.14 * 2.5 ^ 2"
Output: Token(FLOAT, '3.14', line=1, col=1)
Token(MULTIPLY, '*', line=1, col=6)
Token(FLOAT, '2.5', line=1, col=8)
Token(POWER, '^', line=1, col=12)
Token(INT, '2', line=1, col=14)
Token(EOF, '', line=1, col=15)

#### Test 4: Complex Expression
Input: "sin(pi * 0.5) + cos(pi) - 3.14"
Output: 15 tokens including SIN, COS, PI, FLOAT, operators, and parentheses

#### Test 5: Constants
Input: "2 * pi * e"
Output: Token(INT, '2', line=1, col=1)
Token(MULTIPLY, '*', line=1, col=3)
Token(PI, 'pi', line=1, col=5)
Token(MULTIPLY, '*', line=1, col=8)
Token(E, 'e', line=1, col=10)
Token(EOF, '', line=1, col=11)


### Difficulties Encountered

1. **Float number recognition**: Distinguishing between the decimal point in a float and a dot operator (if it existed) required careful lookahead.
2. **Keyword vs identifier**: Implementing the lookup table for keywords while still allowing custom identifiers.
3. **Position tracking**: Maintaining accurate line and column numbers while reading characters and skipping whitespace.

### Conclusions

In this laboratory work:
-  I learned the fundamentals of lexical analysis
-  I implemented a fully functional lexer for mathematical expressions
- The lexer successfully handles integers, floats, operators, and functions
- Trigonometric functions (sin, cos) are properly recognized
-  Constants (pi, e) are identified as special token types
-  Each token contains position information (line, column)

The lexer can be easily extended to support:
- More trigonometric functions (tan, cot, asin, acos)
- Other mathematical functions (log, exp, sqrt)
- Variables and assignments
- Comments
- String literals

### References

1. [Lexical Analysis - Wikipedia](https://en.wikipedia.org/wiki/Lexical_analysis)
2. [Crafting Interpreters: Scanning](https://craftinginterpreters.com/scanning.html)
3. [Formal Languages and Automata Theory](https://www.tutorialspoint.com/automata_theory/lexical_analysis.htm)

### Appendix: Full Token List

| Token Type | Example | Description |
|------------|---------|-------------|
| INT | 42, 0, 123 | Integer numbers |
| FLOAT | 3.14, 0.5 | Floating point numbers |
| PLUS | + | Addition operator |
| MINUS | - | Subtraction operator |
| MULTIPLY | * | Multiplication operator |
| DIVIDE | / | Division operator |
| POWER | ^ | Exponentiation operator |
| ASSIGN | = | Assignment operator |
| LPAREN | ( | Left parenthesis |
| RPAREN | ) | Right parenthesis |
| COMMA | , | Comma separator |
| SIN | sin | Sine function |
| COS | cos | Cosine function |
| PI | pi | π constant |
| E | e | Euler's number |
| IDENT | x, var | Generic identifier |
| EOF | - | End of input |
| ILLEGAL | @, # | Illegal character |


