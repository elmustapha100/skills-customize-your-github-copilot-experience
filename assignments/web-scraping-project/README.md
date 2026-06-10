# 📘 Assignment: Web Scraping and Data Collection

## 🎯 Objective

Build a practical web scraping tool to extract data from a real website, clean and parse it, handle errors gracefully, and store the results. You'll learn how to work with HTTP requests, parse HTML, manage errors, and work with structured data—skills essential for data science and automation.

## 📝 Tasks

### 🛠️ Task 1: Fetch and Explore Web Data

#### Description
Get comfortable with the `requests` library by fetching a real webpage and examining its structure. You'll learn how to make HTTP GET requests and understand what HTML looks like when retrieved programmatically.

#### Requirements
Completed program should:

- Use the `requests` library to fetch data from a public website (we recommend starting with a simple, static page)
- Print the HTTP status code to verify the request succeeded
- Print the first 1000 characters of the HTML to inspect the page structure
- Handle connection errors gracefully (e.g., network unavailable, invalid URL)
- Print a helpful message if the request fails

---

### 🛠️ Task 2: Parse and Extract Data with BeautifulSoup

#### Description
Learn to parse HTML using BeautifulSoup and extract specific data. You'll practice using CSS selectors and HTML navigation to find the information you need—like article titles, prices, links, or dates.

#### Requirements
Completed program should:

- Use BeautifulSoup to parse the HTML from the fetched webpage
- Identify and extract at least 5 data points from the page (e.g., titles, links, prices, dates)
- Store extracted data in a structured format (list of dictionaries or list of tuples)
- Print the extracted data in a readable format
- Handle cases where expected elements are missing (e.g., an article without a description)

---

### 🛠️ Task 3: Clean Data and Handle Edge Cases

#### Description
Real-world data is messy. Handle missing values, clean up formatting (whitespace, special characters), and implement robust error handling. This task teaches defensive programming practices.

#### Requirements
Completed program should:

- Strip unnecessary whitespace and line breaks from extracted data
- Handle missing or incomplete data gracefully (don't crash if an element is empty)
- Validate that extracted data meets basic sanity checks (e.g., non-empty strings, reasonable numbers)
- Implement multiple error handlers: connection errors, parsing errors, unexpected HTML structure
- Log what was scraped successfully and what failed (number of items, any skipped entries)
- Write at least 3 informative error or status messages

---

### 🛠️ Task 4: Store, Analyze, and Export Results ⭐ (Stretch Goal)

#### Description
Save your scraped data to a file and perform basic analysis. This teaches data persistence and gives you experience working with different file formats.

#### Requirements
Completed program should:

- Export cleaned data to a CSV file or JSON file with a timestamp
- Count and report statistics (e.g., "Scraped 42 items successfully")
- Sort or filter the data by at least one criteria (e.g., by date, by price, by length)
- Create a simple summary report showing: total items, success rate, and any failures
- (Bonus) Generate a simple visualization using `matplotlib` or `seaborn` (e.g., chart of most common words or price distribution)

---

## 📚 Concepts You'll Learn

- **HTTP Requests**: How web communication works with `requests`
- **HTML Parsing**: Understanding DOM structure and CSS selectors
- **Error Handling**: Try-except blocks for real-world robustness
- **Data Cleaning**: Processing messy, incomplete data
- **Data Structures**: Working with lists, dictionaries, and structured data
- **File I/O**: Exporting data to CSV/JSON

## 🔧 Getting Started

1. Install required packages:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Start with the provided `starter-code.py` to understand the basic structure

3. Test your scraper on simple, public websites first (avoid sites with strict terms of service)

4. Use browser developer tools (F12) to inspect HTML and find CSS selectors

## ⚠️ Important Notes

- **Respect robots.txt**: Check if a website allows scraping before building your tool
- **Add delays**: Use `time.sleep()` between requests to avoid overwhelming servers
- **User-Agent**: Some sites require a proper User-Agent header—the starter code includes this
- **Terms of Service**: Read the website's ToS—some sites prohibit scraping

## 🎓 Learning Tips

- Start small: Test on one element before scaling to all elements
- Use `print()` statements liberally to debug HTML parsing
- Save raw HTML to a file during development to avoid repeated requests
- Break the project into manageable pieces—don't try to do everything at once
