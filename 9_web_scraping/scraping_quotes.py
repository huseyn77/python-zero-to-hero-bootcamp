import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

for quote in quotes[:5]:
    print(quote.text)