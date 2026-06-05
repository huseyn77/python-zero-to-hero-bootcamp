# Web Scraping Notes

## Topics covered
- HTTP requests
- Status codes
- BeautifulSoup
- HTML parsing
- Extracting links
- Extracting tables
- Building scrapers

## Key concepts

Web scraping is the process of extracting information from websites.

Common uses:
- Data collection
- Price monitoring
- Research
- Automation

---

## HTTP Requests

Python commonly uses the requests library.

Example:
response = requests.get(url)

Useful attributes:
response.status_code
response.text

---

## HTTP Status Codes

200 - Success
301 - Redirect
403 - Forbidden
404 - Not Found
500 - Server Error

---

## BeautifulSoup

BeautifulSoup parses HTML documents.

Import:
from bs4 import BeautifulSoup

Create parser:
soup = BeautifulSoup(html, "html.parser")

---

## Finding Elements

Single element:
soup.find()
Multiple elements:
soup.find_all()

---

## Extracting Text

Example:
title.text

Returns text inside HTML tag.

---

## Extracting Attributes

Example:
link["href"]

Returns attribute value.

---

## HTML Structure

Common tags:
<html>
<head>
<body>
<h1>
<p>
<a>
<table>

Understanding HTML structure is essential for scraping.

---

## Ethical Scraping

Always:
- Respect website terms of service
- Avoid excessive requests
- Check robots.txt
- Use scraping responsibly

---

## Common Libraries

requests
BeautifulSoup
lxml
selenium
playwright

---

## Best Practices

- Check status codes
- Handle exceptions
- Avoid hardcoded assumptions
- Respect rate limits
- Use clear selectors