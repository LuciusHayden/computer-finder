from model import create_model
import os
import joblib
from bs4 import BeautifulSoup as bs
import requests
import re
import json

if (os.path.exists('model.joblib')):
    model = joblib.load('model.joblib')
else:
    model = create_model()

class Laptop:
    def __init__(self, screen_size, screen_resolution, ram, storage, storage_type, graphics, operating_system, weight):
        # self.company = company
        self.screen_size = screen_size
        self.screen_resolution = screen_resolution
        # self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.storage_type = storage_type
        self.graphics = graphics
        self.operating_system = operating_system
        self.weight = weight

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

        match spec_name:
            # case "GPU Brand":
            #     company = spec_value
            case "Screen Size":
                screen_size = spec_value
            case "Screen Resolution":
                screen_resolution = spec_value
            case "Proccesor Model":
                cpu = spec_value
            case "System Memory (RAM)":
                ram = spec_value
            case "Total Storage Capacity":
                storage = spec_value
            case "Storage Type":
                storage_type = spec_value
            case "Graphics":
                graphics = spec_value
            case "Operating System":
                operating_system = spec_value
            case "Product Weight":
                weight = spec_value
            case _:
                pass

        
        
        print(f"  - {spec_name}: {spec_value}")
        print(f"    Description: {spec_definition}")
 
    print("\n")
    
laptop = Laptop(screen_size, screen_resolution, ram, storage, storage_type, graphics, operating_system, weight)   
    


