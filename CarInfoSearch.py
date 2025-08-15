from bs4 import BeautifulSoup
import requests

def get_brand_info(brand_name):
    url = f'https://en.wikipedia.org/wiki/{brand_name}'
    html_text = requests.get(url).get_text()
    soup = BeautifulSoup(html_text, 'lxml')
    