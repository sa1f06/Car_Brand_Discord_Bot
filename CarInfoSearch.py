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
        #find the "th" in html
        table_header = 'th'
        #find "th" and "Founded" in html
        if table_header and "Founded" in table_header:
            #find the data inside the html
            date_found = table_header.find('td').text
            print(f"{new_brand_name} was founded: {date_found}")
        if table_header and "Founders" in table_header:
            founder_names = table_header.find('td').text
            print(f"{new_brand_name.title()} was founded by {founder_names}")
        if table_header and "Founder" in table_header:
            founder_name = table_header.find('td').text
            print(f"The founder of {new_brand_name} is: {founder_name}")
        if table_header and "Headquarters" in table_header:
            location = table_header.find("td").text
            print("The headquarters of {new_brand_name} are located in: {location}")
        if table_header and "Revenue" in table_header:
            total_money = table_header.find("td").text
            print(f"The revenue for {new_brand_name} is: {total_money}")
