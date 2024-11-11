from model import create_model
import os
import joblib
from bs4 import BeautifulSoup as bs
import requests

if (os.path.exists('model.joblib')):
    model = joblib.load('model.joblib')
else:
    model = create_model()

url = "https://www.bestbuy.com/site/all-laptops/pc-laptops/pcmcat247400050000.c?id=pcmcat247400050000"

html = requests.get(url).text
soup = bs(html, 'html.parser')

laptops = soup.find_all('div', class_="list-wrapper top-border")
print(len(laptops))


