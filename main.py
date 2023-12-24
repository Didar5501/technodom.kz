import re 
import requests 
from bs4 import BeautifulSoup 

count = 0
for i in range(1, 4):
    url = f'https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit=24&brands=apple&page={i}&sorting=score&price=0' 
    response = requests.get(url) 
    data = response.json() 
    
    for product in data.get('payload', []):
        product_title = product.get('title')
        product_price = product.get('price')
        
        if "256" in product_title: 
            print(f'{product_title} {product_price}\n')
            count += 1
        if count>=20:
            break
        