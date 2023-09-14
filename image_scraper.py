import requests
from bs4 import BeautifulSoup

url = str(input("Enter URL of website to be scraped: "))

r = requests.get(url)

print(r)

soup = BeautifulSoup(r.content, 'html.parser')

images_list = []

images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"source": src, "alt": alt})

for image in images_list:
    print(image)