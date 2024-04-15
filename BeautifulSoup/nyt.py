import requests
from bs4 import BeautifulSoup

URL = "https://www.nytimes.com/"
data = {}

res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')

for text in soup.find_all('p'):
    data[text] = text.parent.name

print(data)