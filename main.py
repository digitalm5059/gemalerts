import requests

url = "https://bidplus.gem.gov.in/all-bids"

response = requests.get(url)

print(response.status_code)
