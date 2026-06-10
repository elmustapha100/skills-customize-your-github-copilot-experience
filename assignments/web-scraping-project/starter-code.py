"""
Web Scraping Project - Starter Code
====================================

This starter code provides a basic framework for building a web scraper.
Complete the tasks in the README to build out each part.

Topics covered:
- HTTP requests with the requests library
- HTML parsing with BeautifulSoup
- Error handling and logging
- Data cleaning and storage
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time


class WebScraper:
    """A simple web scraper for collecting and processing data."""
    
    def __init__(self, url):
        """
        Initialize the scraper with a target URL.
        
        Args:
            url (str): The website URL to scrape
        """
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.raw_html = None
        self.soup = None
        self.data = []
    
    def fetch_page(self):
        """
        TASK 1: Fetch the webpage using requests.
        
        TODO:
        - Make a GET request to self.url with self.headers
        - Check the status code
        - Store the HTML content in self.raw_html
        - Print the status code and first 500 characters
        - Handle any request exceptions gracefully
        """
        try:
            # YOUR CODE HERE
            pass
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching the page: {e}")
            return False
        
        return True
    
    def parse_page(self):
        """
        TASK 2: Parse the HTML and extract data.
        
        TODO:
        - Create a BeautifulSoup object from self.raw_html
        - Find all relevant elements using CSS selectors or tag names
        - Extract at least 5 data points per item (modify as needed)
        - Store results as dictionaries in self.data
        - Handle missing elements gracefully
        
        Example structure:
        self.data = [
            {'title': '...', 'link': '...', 'price': '...'},
            ...
        ]
        """
        if self.raw_html is None:
            print("❌ No HTML to parse. Fetch the page first.")
            return False
        
        try:
            # YOUR CODE HERE
            self.soup = BeautifulSoup(self.raw_html, 'html.parser')
            
            # TODO: Extract data using self.soup
            pass
        
        except Exception as e:
            print(f"❌ Error parsing the page: {e}")
            return False
        
        return True
    
    def clean_data(self):
        """
        TASK 3: Clean and validate the extracted data.
        
        TODO:
        - Remove whitespace and special characters from strings
        - Handle missing values (None, empty strings)
        - Validate data types and sanity checks
        - Remove duplicate entries if any
        - Print statistics about what was cleaned
        """
        if not self.data:
            print("❌ No data to clean. Parse the page first.")
            return False
        
        try:
            cleaned_data = []
            skipped = 0
            
            for item in self.data:
                # YOUR CODE HERE: Implement data cleaning logic
                pass
            
            self.data = cleaned_data
            print(f"✅ Cleaned {len(cleaned_data)} items ({skipped} skipped)")
            
        except Exception as e:
            print(f"❌ Error cleaning data: {e}")
            return False
        
        return True
    
    def save_to_csv(self, filename=None):
        """
        TASK 4: Export data to a CSV file.
        
        Args:
            filename (str): Output filename. If None, generates one with timestamp.
        
        TODO:
        - If filename is None, create one like 'scraped_data_2024-01-15.csv'
        - Write all data rows with proper headers
        - Print success message with item count
        """
        if not self.data:
            print("❌ No data to save.")
            return False
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"scraped_data_{timestamp}.csv"
        
        try:
            # YOUR CODE HERE: Implement CSV export
            pass
        
        except Exception as e:
            print(f"❌ Error saving to CSV: {e}")
            return False
        
        return True
    
    def print_summary(self):
        """Print a summary of what was scraped."""
        print("\n" + "="*50)
        print("📊 SCRAPING SUMMARY")
        print("="*50)
        print(f"Total items collected: {len(self.data)}")
        if self.data:
            print(f"First item: {self.data[0]}")
        print("="*50 + "\n")


def main():
    """Main function to run the scraper."""
    
    # TODO: Choose a website to scrape (start with a simple one)
    url = "https://example.com"  # Replace with your target URL
    
    # Create scraper instance
    scraper = WebScraper(url)
    
    # TASK 1: Fetch the page
    print("🔍 Step 1: Fetching the page...")
    if not scraper.fetch_page():
        return
    
    # TASK 2: Parse and extract data
    print("\n🔍 Step 2: Parsing and extracting data...")
    if not scraper.parse_page():
        return
    
    # TASK 3: Clean the data
    print("\n🔍 Step 3: Cleaning data...")
    if not scraper.clean_data():
        return
    
    # Print summary
    scraper.print_summary()
    
    # TASK 4: Save to file (optional)
    print("🔍 Step 4: Saving data...")
    if scraper.save_to_csv():
        print("✅ Data saved successfully!")


if __name__ == "__main__":
    main()
