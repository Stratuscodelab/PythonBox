import requests
from bs4 import BeautifulSoup
import json


# this script scrapes a website for .png links and their corresponding CIDs
# and saves the results to a metadata file.




def scrape_png_links_and_cid(base_url):
    all_png_data = []
    page = 1  # Start from the first page

    while True:
        print(f"Fetching page {page}...")
        # Construct the URL for the current page
        url = f"{base_url}?page={page}"
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all hyperlinks (<a> tags)
            links = soup.find_all('a')
            print(f"Found {len(links)} hyperlink(s) on page {page}.")

            # Collate .png links and CIDs
            png_data = []
            for link in links:
                href = link.get('href')  # Get the hyperlink reference
                if href and href.endswith('.png'):  # Check if the link ends with .png
                    # Extract the CID from the hyperlink path
                    parts = href.split('/')
                    if len(parts) >= 2:  # Ensure the path has enough parts
                        cid = parts[-2]  # CID is assumed to be the second-to-last part
                        image_name = parts[-1]  # Image name is the last part
                        png_data.append({'name': image_name, 'cid': cid})
                        print(f"Extracted PNG: {image_name}, CID: {cid}")

            # If no .png links are found, assume we've reached the last page
            if not png_data:
                print(f"No .png links found on page {page}. Stopping pagination.")
                break

            # Add the data from this page to the overall list
            all_png_data.extend(png_data)

            # Move to the next page
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching page {page}: {e}")
            break

    return all_png_data

# Base URL to scrape (without the `?page=` parameter)
base_url = ""

# Scrape the .png links and CIDs across all pages
png_list = scrape_png_links_and_cid(base_url)

# Print the results
if png_list:
    print("Scraping completed. Here are the results:")
    for item in png_list:
        print(f"Image Name: {item['name']}, CID: {item['cid']}")
else:
    print("No .png links were found on the pages.")

# Save the data to a metadata file (e.g., JSON)
if png_list:
    with open('metadata.json', 'w') as f:
        json.dump(png_list, f, indent=4)
        print("Metadata saved to metadata.json")
else:
    print("No data to save to metadata.json.")