import requests
from bs4 import BeautifulSoup

url = 'https://www.w3.org/standards/'

res = requests.get(url)
status = res.status_code
content = res.content
# print(content)
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.getText())
print(soup.body.getText())
print(status)