#product_code=input('Podaj kod produkry')
from bs4 import BeautifulSoup
import requests
product_code='96685108'
url=f'https://www.ceneo.pl/{product_code}#tab=reviews'
respons=requests.get(url)
page=BeautifulSoup(respons.text,'html.parser')
opinions=page.select('div.js_product-review')
for opinion in opinions:
    print(opinion['data-entry-id'])
print(len(opinions))
print(type(opinions))