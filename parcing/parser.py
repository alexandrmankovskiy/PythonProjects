import requests

from bs4 import BeautifulSoup 

URL = 'https://auto.ria.com/uk/legkovie/lexus/?page=1'
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
 'accept':'*/*'}

def getHtml(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
def getContent(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='ticket-item')
    cars = []
    for item in items:
        uah_price= item.find('span', class_='i-block')
        if uah_price:
            uah_price = str(uah_price.get_text(strip=True))
        else:
            print('Цену уточняйте')
        cars.append({
            'title': item.find('div', class_='head-ticket').get_text(strip=True),
            'link':item.find('a', class_='address').get('href'),
            'usdt_price':item.find('span', class_='green').get_text(strip=True),
            'mileage':item.find('li', class_='item-char js-race').get_text(strip=True),
            'engine':item.find('i', class_='icon-fuel').find_next_siblings(text=True),
            'uah_price':uah_price.replace('\xa0грн','')

        })
    print(cars)    
def parse():
    html = getHtml(URL)
    if html.status_code == 200:
        getContent(html.text)
    else:
        print('Error, try again later')
parse()
