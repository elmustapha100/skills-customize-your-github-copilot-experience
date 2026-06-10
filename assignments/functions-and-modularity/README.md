# 📘 Assignment: Functions and Modularity

## 🎯 Objective

Master the fundamentals of writing reusable functions and organizing code into modules. You'll learn how to decompose problems into smaller, manageable pieces and write clean, maintainable code.

**Skills practiced:** Function definition, parameters and return values, scope and namespaces, code reusability, module organization, documentation

## 📝 Tasks

### 🛠️ Write and Call Functions

#### Description
Create basic functions with different parameter and return value combinations to understand function fundamentals.

#### Requirements
Completed program should:

- Define at least 3 functions: one with no parameters, one with parameters, and one that returns a value
- Call each function and display the results
- Use meaningful function names that describe what they do
- Include a `main()` function that orchestrates the other functions

### 🛠️ Work with Parameters and Return Values

#### Description
Build functions that accept multiple parameters and return useful results, practicing parameter passing techniques.

#### Requirements
Completed program should:

- Create functions that accept 2+ parameters
- Demonstrate default parameter values
- Return multiple values using tuples (e.g., `return x, y`)
- Call these functions with different argument combinations and display results
- Example: `calculate_stats(numbers)` returns min, max, average

### 🛠️ Understand Scope and Namespaces

#### Description
Explore how variable scope works in Python and avoid common scoping issues.

#### Requirements
Completed program should:

- Demonstrate local vs. global variables
- Show how function parameters create local scope
- Avoid unintended global variable modifications
- Create a function that safely uses variables without scope conflicts
- Include comments explaining scope behavior

### 🛠️ Organize Code into Modules

#### Description
Refactor code into separate modules to demonstrate code organization and reusability.

#### Requirements
Completed program should:

- Create a separate module file (e.g., `math_utils.py`) with utility functions
- Import and use functions from that module in your main script
- Include docstrings for functions in the module
- Demonstrate how modules enable code reuse across projects
- The main script should be clean and organized, calling functions from the module
