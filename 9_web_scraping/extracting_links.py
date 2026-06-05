from bs4 import BeautifulSoup

html = """
<a href="https://example.com">Example</a>
"""

soup = BeautifulSoup(html, "html.parser")

link = soup.find("a")

print(link["href"])