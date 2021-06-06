import requests
import flask

res = requests.get("https://google.com")

print(res.text)
