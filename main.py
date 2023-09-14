import requests

r = requests.get("https://yadavyashvant.netlify.app/")

print(r)

print(r.content)