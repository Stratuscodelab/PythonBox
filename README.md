# PythonBox
A box full of python scripts for various uses.

# Web Scraper for PNG Links and CIDs

This Python script (`scrape.py`) scrapes a website for `.png` image links and their corresponding CIDs (Content Identifiers). The extracted data is saved to a `metadata.json` file for further use.

---

## Features

- **Pagination Support**: Automatically navigates through paginated pages to collect all `.png` links.
- **CID Extraction**: Extracts the CID from the URL structure.
- **JSON Output**: Saves the scraped data in a structured `metadata.json` file.
- **Error Handling**: Handles HTTP request errors gracefully.

---

## Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

---

## Installation

1. Clone the repository or download the `scrape.py` file.
2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
