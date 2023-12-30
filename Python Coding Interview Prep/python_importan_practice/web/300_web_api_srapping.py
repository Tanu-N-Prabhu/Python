from bs4 import BeautifulSoup
import requests

scrapingdog_api_key = '5eab86fbe562fc52fe6e46c0'
r = requests.get('https://api.scrapingdog.com/scrape?api_key='+ scrapingdog_api_key +'&url=https://apiworld.co/awards/api-300-top-industry-innovations/').text

soup = BeautifulSoup(r, 'html.parser')
allapis = soup.find_all("tr")
l = {}
u = list()
for i in range(0, len(allapis)):
    try:
        api = allapis[i].find_all("td")
    except LookupError:
        api = None

for i in range(0, len(allapis)):
    try:
        api = allapis[i].find_all("td")
    except LookupError:
        api = None
    try:
        l["company"] = api[0].text.replace("\n", "")
    except LookupError:
        l["company"] = None

    try:
        l["api"] = api[1].text.replace("\n", "")
    except LookupError:
        l["api"] = None

    try:
        l["category"] = api[2].text.replace("\n", "")
    except LookupError:
        l["category"] = None

    u.append(l)
    l = {}

print(u)
