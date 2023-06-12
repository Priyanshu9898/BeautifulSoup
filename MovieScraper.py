import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://subslikescript.com/movies'
response = requests.get(url)

# Create a BeautifulSoup object with the website's HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the 'ul' element with class 'scripts-list'
ul_element = soup.find('ul', class_='scripts-list')

# Find all 'a' elements inside the 'ul' element
a_elements = ul_element.find_all('a')

# Extract and print the text attribute of each 'a' element
for a in a_elements:
    print(a.text)
