from bs4 import BeautifulSoup

html = """
<html>
<body>
<p>First paragraph</p>
<p>Second paragraph</p>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

paragraphs = soup.find_all("p")

for p in paragraphs:
    print(p.text)