# MiniGO AST - Programming Language Principles Assignment 2

## Overview

This project implements an Abstract Syntax Tree (AST) for MiniGO, a simplified version of the Go programming language. It was developed as the second assignment for the Programming Language Principles (PPL) course at Ho Chi Minh City University of Technology (HCMUT).

## Project Structure

The project is organized into several components:

- **Lexer**: Breaks down source code into tokens
- **Parser**: Builds an abstract syntax tree from tokens
- **AST Classes**: Represents different elements of the MiniGO language
- **Visitors**: Implements the visitor pattern for AST traversal
- **Main Application**: Demonstrates the functionality of the compiler components

## Features

- Lexical analysis of MiniGO source code
- Syntactic analysis to build an abstract syntax tree
- Support for MiniGO language constructs including:
  - Variable declarations
  - Function declarations
  - Basic data types (int, float, string, bool)
  - Control structures (if-else, for loops)
  - Arrays and array access
  - Binary and unary operations

## Getting Started

### Prerequisites

- Python 3.x
- ANTLR4 (if used for grammar definition)

### Installation

1. Clone the repository
2. Install required dependencies

### Usage

Run the main application with a MiniGO source file as input:

```
python main.py input_file.go
```

## Implementation Details

### Lexical Analysis

The lexer analyzes the source code and breaks it down into tokens such as keywords, identifiers, literals, and operators.

### Syntax Analysis

The parser checks if the sequence of tokens conforms to the grammar rules of MiniGO and builds an abstract syntax tree.

### Abstract Syntax Tree

The AST represents the hierarchical structure of the program, capturing its syntactic and semantic information.

### AST Visitors

Visitors traverse the AST to perform various operations such as type checking, optimization, or code generation.

## Example

### MiniGO Input

```go
func main() {
    var x int = 10
    if x > 5 {
        println(x)
    }
}
```

### Generated AST (Visualization)

```
Program
└── FuncDecl: main
    └── Body
        ├── VarDecl: x (int)
        │   └── IntLit: 10
        └── IfStmt
            ├── Condition
            │   └── BinaryExpr: >
            │       ├── Id: x
            │       └── IntLit: 5
            └── ThenStmt
                └── CallExpr: println
                    └── Id: x
```

## Testing

The project includes test cases to verify the correctness of the implementation. Run the tests with:

This project is an academic assignment for the PPL course at HCMUT and is not licensed for public use.
