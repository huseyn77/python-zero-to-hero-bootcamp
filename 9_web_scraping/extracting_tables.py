from bs4 import BeautifulSoup

html = """
<table>
<tr><td>Python</td></tr>
<tr><td>Java</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")

rows = soup.find_all("td")

for row in rows:
    print(row.text)