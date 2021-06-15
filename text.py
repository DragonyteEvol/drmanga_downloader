import requests

response= requests.get(input("url:"))
print(response.status_code)

