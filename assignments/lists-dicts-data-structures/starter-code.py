# Starter Code for Lists, Dicts, and Data Structures Assignment

# Task 1: Lists and List Operations
def demonstrate_lists():
    """Practice fundamental list operations."""
    
    # TODO: Create a list of numbers
    numbers = []
    
    # TODO: Add elements to the list using append()
    
    # TODO: Access elements by index (first, last, etc.)
    
    # TODO: Modify elements
    
    # TODO: Use list slicing to get a subset
    
    # TODO: Sort the list
    
    # TODO: Create a list comprehension that gets only even numbers
    even_numbers = []  # Replace with comprehension
    
    # TODO: Print results
    pass


# Task 2: Dictionaries and Key-Value Pairs
def demonstrate_dicts():
    """Practice dictionary operations."""
    
    # TODO: Create a dictionary (e.g., student names and grades)
    student_grades = {}
    
    # TODO: Add key-value pairs
    
    # TODO: Access values using keys
    
    # TODO: Use get() to safely access values
    
    # TODO: Check if a key exists using 'in'
    
    # TODO: Iterate through keys and values
    
    # TODO: Calculate statistics (e.g., average grade)
    
    # TODO: Print results
    pass


# Task 3: Nested Data Structures
def work_with_nested_structures():
    """Practice working with nested lists and dictionaries."""
    
    # TODO: Create a list of dictionaries (list of student records)
    students = []
    # Example structure: [
    #     {"name": "Alice", "age": 16, "grades": [90, 85, 88]},
    #     {"name": "Bob", "age": 17, "grades": [78, 82, 80]},
    # ]
    
    # TODO: Add student records
    
    # TODO: Access nested data (student name, first grade, etc.)
    
    # TODO: Iterate through students and their grades
    
    # TODO: Search for a student by name
    
    # TODO: Calculate average grade for each student
    
    # TODO: Print results
    pass


# Task 4: Data Management System
class ContactManager:
    """A simple contact management system."""
    
    def __init__(self):
        """Initialize the contact list."""
        # TODO: Create an empty list to store contacts
        self.contacts = []
    
    def add_contact(self, name, phone, email):
        """Add a new contact."""
        # TODO: Create a dictionary for the contact
        # TODO: Add it to the contacts list
        pass
    
    def find_contact(self, name):
        """Find a contact by name."""
        # TODO: Search through contacts for matching name
        # TODO: Return the contact or None if not found
        pass
    
    def remove_contact(self, name):
        """Remove a contact by name."""
        # TODO: Find and remove the contact
        pass
    
    def list_all_contacts(self):
        """Display all contacts."""
        # TODO: Print all contacts in a readable format
        pass
    
    def update_contact(self, name, phone=None, email=None):
        """Update contact information."""
        # TODO: Find contact and update fields if provided
        pass


# Main function to test all tasks
def main():
    """Test all list and dictionary functions."""
    
    print("=== Task 1: Lists ===")
    demonstrate_lists()
    
    print("\n=== Task 2: Dictionaries ===")
    demonstrate_dicts()
    
    print("\n=== Task 3: Nested Structures ===")
    work_with_nested_structures()
    
    print("\n=== Task 4: Contact Manager ===")
    # TODO: Create a ContactManager instance
    # TODO: Add several contacts
    # TODO: Test add, find, remove, list, update operations
    pass


if __name__ == "__main__":
    main()
