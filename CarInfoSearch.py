from bs4 import BeautifulSoup
import requests

def get_brand_info(brand_name):
    url = f'https://en.wikipedia.org/wiki/{brand_name}'
    html_text = requests.get(url).get_text()
    soup = BeautifulSoup(html_text, 'lxml')
    table_row = soup.find_all('tr')

    new_brand_name = brand_name.replace("_", " ").replace("-", " ")

    for row in table_row:
        table_header = 'th'
        if table_header and "Founded" in table_header:
            date_found = table_header.find('td').text
            print(f"{new_brand_name} was founded: {date_found}")