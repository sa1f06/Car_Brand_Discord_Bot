from bs4 import BeautifulSoup
import requests

#Get the brand name the user inputs to go to the wikipedia page of the car brand
def get_brand_info(brand_name):
    url = f'https://en.wikipedia.org/wiki/{brand_name}'
#Get the html text of the page
    html_text = requests.get(url).get_text()
#Create instance of BeautifulSoup, parse through the html with lxml
    soup = BeautifulSoup(html_text, 'lxml')
#Find every "tr" in the page's html
    table_row = soup.find_all('tr')

    new_brand_name = brand_name.replace("_", " ").replace("-", " ")

    for row in table_row:
        table_header = 'th'
        if table_header and "Founded" in table_header:
            date_found = table_header.find('td').text
            print(f"{new_brand_name} was founded: {date_found}")
        if table_header and "Founders" in table_header:
            founder_names = table_header.find('td').text
            print(f"{new_brand_name.title()} was founded by {founder_names}")
        if table_header and "Founder" in table_header:
            founder_name = table_header.find('td').text
            print(f"The founder of {new_brand_name} is: {founder_name}")
