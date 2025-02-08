# Flipkart Web Scraping Script
This script automates web scraping using Selenium to extract product details from Flipkart based on search queries stored in a CSV file. 
It iterates through multiple pages, extracting product information such as name, rating, price, discount, and image links.
## workflow
### Read Search Queries from CSV
- Opens and reads records.csv containing search queries.
- Stores them in a list for iteration.
### Search & Extract Product Information
- Inputs each search query into Flipkart's search bar.
- Store Data in List
- Handles missing elements using try-except to avoid crashes.
### Save Data to CSV & JSON
- Saves it as CSV (products2.csv) inside an output folder.
- Also saves the data in JSON (products2.json).
### Areas for Improvement
- Headless Mode for faster execution (options.add_argument("--headless")).
- Check if elements exist before extracting to avoid exceptions.
