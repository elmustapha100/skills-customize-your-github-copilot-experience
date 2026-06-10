# 📘 Assignment: File I/O and Error Handling

## 🎯 Objective

Master reading from and writing to files while handling errors gracefully. You'll learn how to work with different file types, manage exceptions, and write robust code that handles edge cases and unexpected inputs.

**Skills practiced:** File I/O operations, exception handling, try-except blocks, file modes, context managers, error recovery, input validation

## 📝 Tasks

### 🛠️ Read and Write Text Files

#### Description
Create a program that reads data from a file and writes processed data to a new file.

#### Requirements
Completed program should:

- Read a text file line by line
- Process the data (e.g., convert to uppercase, filter, count lines)
- Write the processed data to a new output file
- Handle the case where the input file doesn't exist
- Use `with` statements for file operations (context managers)
- Example: read a file of names and write them in reverse order to a new file

### 🛠️ Implement Exception Handling

#### Description
Add comprehensive error handling to your file operations to catch and recover from errors gracefully.

#### Requirements
Completed program should:

- Use try-except blocks to catch `FileNotFoundError`, `IOError`, and other exceptions
- Provide informative error messages for each exception type
- Handle edge cases (empty files, permission denied, invalid data)
- Continue execution after handling an error when possible
- Log errors or display user-friendly messages

### 🛠️ Work with Different File Formats

#### Description
Expand your program to handle multiple file formats (CSV, JSON, or plain text).

#### Requirements
Completed program should:

- Read and parse data from at least two different file formats
- Handle format-specific errors (e.g., malformed JSON, inconsistent CSV structure)
- Write data to the same or different format
- Validate that data is in the expected format before processing
- Test with both valid and invalid files

### 🛠️ Build a Robust Data Logging System

#### Description
Create a system that logs application events and errors to a file with proper formatting and error recovery.

#### Requirements
Completed program should:

- Write logs to a file with timestamps and message levels (INFO, ERROR, WARNING)
- Include error context and stack traces for debugging
- Handle log file creation and rotation (or at minimum, handle append mode)
- Use exception handling to ensure logging doesn't crash the program
- Demonstrate logging different types of events (success, warnings, errors)
