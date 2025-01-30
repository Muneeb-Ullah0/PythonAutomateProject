import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example-news-website.com/latest-news'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the article titles (assuming they are within <h2> tags)
    titles = soup.find_all('h2', class_='article-title')

    # Print out the titles
    for title in titles:
        print(title.text.strip())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
