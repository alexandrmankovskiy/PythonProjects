import requests
import csv
from bs4 import BeautifulSoup 

URL = 'https://auto.ria.com/uk/legkovie/lexus/?page=1'
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
 'accept':'*/*'}
FILE = 'cars.csv'


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
            # 'engine':item.find('i', class_='icon-fuel').find_next_siblings(text=True),
            'uah_price':uah_price.replace('\xa0грн','')
        })
    return cars    

def getPagesNum(html): # returns 216 when there is 108 pages
    soup = BeautifulSoup(html,'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    return int(pagination[-1].get_text())

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Mark','Link','Dollar','Milage','UAH'])
        for item in items:
            writer.writerow([item['title'],item['link'],item['usdt_price'],item['mileage'],item['uah_price']])
def parse():
    html = getHtml(URL)
    if html.status_code == 200:
        cars = []
        pages_count = getPagesNum(html.text)
        for page1 in range(1, pages_count + 1):
            print(f'Process going on {page1} from {pages_count}...')
            html = getHtml(URL, params = {'page' : page1})
            cars.extend(getContent(html.text))
        save_file(cars, FILE)
        print(f'We got: {len(cars)} cars')
    else:
        print('Error, try again later')
parse()