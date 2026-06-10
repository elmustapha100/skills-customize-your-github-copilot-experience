# Starter Code for File I/O and Error Handling Assignment

# Task 1: Read and Write Text Files
def read_and_process_file(input_filename, output_filename):
    """
    Read a text file, process the content, and write to output file.
    
    TODO: Implement this function to:
    - Open input_filename for reading
    - Read lines and process them (e.g., convert to uppercase)
    - Write processed content to output_filename
    - Use 'with' statement for file operations
    - Handle FileNotFoundError if input file doesn't exist
    """
    pass


# Task 2: Exception Handling
def safe_file_operation(filename):
    """
    Demonstrate comprehensive error handling for file operations.
    
    TODO: Implement this function to:
    - Try to open and read a file
    - Catch FileNotFoundError and provide a helpful message
    - Catch IOError and provide a different message
    - Handle other potential exceptions
    - Return data if successful, None or default if error occurs
    """
    pass


# Task 3: Work with Different File Formats
def read_csv_file(filename):
    """
    Read and parse a CSV file.
    
    TODO: Implement this function to:
    - Open and read the CSV file
    - Parse lines into a structured format
    - Handle malformed CSV lines
    - Return parsed data
    """
    pass

def read_json_file(filename):
    """
    Read and parse a JSON file.
    
    TODO: Implement this function to:
    - Open and read the JSON file
    - Parse JSON content
    - Handle JSON decoding errors
    - Return parsed data
    """
    pass

def process_multiple_formats(filename):
    """
    Detect file format and process accordingly.
    
    TODO: Implement this function to:
    - Check file extension
    - Call appropriate reader (read_csv_file or read_json_file)
    - Handle unknown file formats
    - Return processed data
    """
    pass


# Task 4: Build a Logging System
class SimpleLogger:
    """A basic logging system that writes to a file."""
    
    def __init__(self, log_filename):
        """Initialize the logger with a log file."""
        # TODO: Store the log filename
        pass
    
    def log(self, level, message):
        """
        Write a log entry with timestamp and level.
        
        TODO: Implement this method to:
        - Add current timestamp
        - Format message as: [TIMESTAMP] [LEVEL] message
        - Write to log file in append mode
        - Handle any file write errors
        """
        pass
    
    def log_error(self, error_message):
        """Log an error with ERROR level."""
        # TODO: Call log() with ERROR level
        pass
    
    def log_info(self, info_message):
        """Log an info message with INFO level."""
        # TODO: Call log() with INFO level
        pass


# Main function to test all tasks
def main():
    """Test all file I/O and error handling functions."""
    
    # TODO: Task 1 - Test read_and_process_file()
    
    # TODO: Task 2 - Test safe_file_operation() with valid and invalid files
    
    # TODO: Task 3 - Test process_multiple_formats() with CSV and JSON files
    
    # TODO: Task 4 - Test SimpleLogger with various message types
    
    pass


if __name__ == "__main__":
    main()
