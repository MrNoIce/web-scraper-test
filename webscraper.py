from bs4 import BeautifulSoup
import requests

url = 'https://github.com/MrNoIce'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

print(content)
info = content.find_all('p', attrs={"class": "content"})
for info in content.find_all('p', attrs={"class": "content"}):
    print(info.encode('utf-8'))


