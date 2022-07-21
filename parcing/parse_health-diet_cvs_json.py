import json
import requests
from bs4 import BeautifulSoup
import csv
import os
# url = 'https://health-diet.ru/table_calorie/'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
domain_name = 'https://health-diet.ru'
# r = requests.get(url, HEADERS)
# # print(r.text)

# src = r.text

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open('index.html',encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
product_categoris = soup.find_all(class_='mzr-tc-group-item-href')
# categoris_dict = {}
# for item in product_categoris:
#     item_name = item.text
#     item_href = domain_name + item.get('href')
#     # print(f'{item_name}:{domain_name}{item_href}')
#     categoris_dict[item.text] = item_href
# with open('data.json', 'w',encoding='utf-8')as file:
#     json.dump(categoris_dict, file, indent = 4, ensure_ascii = False)

with open('data.json',encoding='utf-8') as file:
    all_categoris = json.load(file)
itterations = len(all_categoris)-1 
print(f'Overoll pages: {itterations}')
count = 0
for category_name, category_href in all_categoris.items():
    count += 1    
    rep = [' ', ',','`','-',"'"]
    for item in rep:
        if item in rep:
            category_name = category_name.replace(item, '_')
    r = requests.get(url = category_href, headers=HEADERS)
    src = r.text
    with open(f'data/{count}_{category_name}.html', 'w',encoding='utf-8') as file:
        src = file.write(src)
    with open(f'data/{count}_{category_name}.html',encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue
    table_th = soup.find('table').find('tr').find_all('th')
    product = table_th[0].text       
    calories = table_th[1].text
    protein = table_th[2].text   
    fats = table_th[3].text    
    carbohydrate = table_th[4].text

    with open(f'data/{count}_{category_name}_table.csv', 'w',encoding='utf-8-sig') as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(
            (
                product,
                calories,
                protein,
                fats,
                carbohydrate
            )
        )
    # os.startfile('table.csv')
    products_data = soup.find('tbody').find_all('tr')
    products_info_json = []
    for item in products_data:
        products_td = item.find_all('td')

        title = products_td[0].find('a').text
        calories = products_td[1].text
        protein = products_td[2].text
        fats = products_td[3].text
        carbohydrate = products_td[4].text
        products_info_json.append(
            {
                'Title':title,
                'Calories':calories,
                'Protein':protein,
                'Fats':fats,
                'Carbonhydrate':carbohydrate
            }
        )
        with open(f'data/{count}_{category_name}_table.csv', 'a',encoding='utf-8-sig') as file:
            writer = csv.writer(file,delimiter=";")
            writer.writerow(
                (
                    title,
                    calories,
                    protein,
                    fats,
                    carbohydrate
                )
            )
    with open(f'data/{count}_{category_name}_json.json', 'a', encoding='utf-8') as file:
        json.dump(products_info_json, file, indent=4, ensure_ascii=False)

    print(f'# Ittereation: {count}...')
    itterations = itterations - 1
    print()
    print(f'Itterations left: {itterations}')
    if itterations == 0:
        print('The work is done!')
        break
    