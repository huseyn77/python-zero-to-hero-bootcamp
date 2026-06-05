import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1")

if title:
    print(title.text)