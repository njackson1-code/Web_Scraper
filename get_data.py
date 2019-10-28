import requests
from bs4 import BeautifulSoup
import json

url = "http://ethans_fake_twitter_site.surge.sh/"
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

print(content)