import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://www.annahar.com/english/section/186-mena'# Replace with the URL of the website you're interested in

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and collect data from the web page
    article_titles = []
    for article in soup.find_all('article'):
        title = article.find('h2').get_text()
        article_titles.append(title)
    
    # Print the collected data
    for i, title in enumerate(article_titles, start=1):
        print(f"{i}. {title}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
