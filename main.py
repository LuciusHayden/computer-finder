from model import create_model
import os
import joblib
from bs4 import BeautifulSoup as bs
import requests
import re
import json
# if (os.path.exists('model.joblib')):
#     model = joblib.load('model.joblib')
# else:
#     model = create_model()

session = requests.Session()
url = "https://www.bestbuy.com/site/all-laptops/pc-laptops/pcmcat247400050000.c?id=pcmcat247400050000"
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}) 

html = session.get(url).text
soup = bs(html, 'html.parser')

laptops =  soup.find_all('a', {'class' :'image-link'})

# for laptop in laptops:
#     siteHtml = session.get(f"https://bestbuy.com{laptop['href']}").text

siteHtml = session.get(f"https://bestbuy.com{laptops[0]['href']}").text
soup_ = bs(siteHtml, 'html.parser')
details = soup_.find_all('script', {'type' : 'application/json'})
data = json.loads(details[2].text)

for category in data['specifications']['categories']:
    print(f"Category: {category['displayName']}")
    for spec in category["specifications"]:
        spec_name = spec.get("displayName", "N/A")
        spec_value = spec.get("value", "N/A")
        spec_definition = spec.get("definition", "No description")
        
        print(f"  - {spec_name}: {spec_value}")
        print(f"    Description: {spec_definition}")
    print("\n")



