############################################################################
import csv
import requests
from bs4 import BeautifulSoup


def scrape_names_emails(base_url, start_page, last_page):
    # Prepare CSV writing
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header
        csvwriter.writerow(['URL', 'Name', 'Email'])


        # Iterate over each page
        for page in range(start_page, last_page + 1):
            # Construct the URL for the current page
            page_url = f"{base_url}?page={page}"
            print(f"Scraping {page_url}...")


            # Send a GET request to the page URL
            response = requests.get(page_url)


            # Check if the request was successful
            if response.status_code != 200:
                print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
                continue


            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')


            # Find all name elements
            name_elements = soup.find_all('h2', class_='directory-grid-name')


            # Process each name element found
            for name_element in name_elements:
                try:
                    # Extract the name
                    full_name = name_element.get_text(strip=True)


                    # Find the email element related to this name
                    email_element = name_element.find_next('div', class_='directory-grid-email')
                   
                    if email_element:
                        email = email_element.get_text(strip=True)
                    else:
                        email = "No Email Found"


                    # Append the collected data to the CSV file
                    csvwriter.writerow([page_url, full_name, email])
                    print(f'Name: {full_name}, Email: {email}')
                except Exception as e:
                    print(f"An error occurred for one of the entries: {str(e)}")
                    continue


    print("Data has been written to scraped_data.csv")


# Example usage
base_url = ""
start_page = 0  # Initial page number
last_page = 122  # Last page number to scrape


scrape_names_emails(base_url, start_page, last_page)
