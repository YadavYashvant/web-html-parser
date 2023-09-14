import requests
from bs4 import BeautifulSoup

r = requests.get("https://yadavyashvant.netlify.app/")

print(r)

soup = 