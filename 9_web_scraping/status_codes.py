import requests

response = requests.get("https://example.com")

if response.status_code == 200:
    print("Request successful")
else:
    print("Request failed")