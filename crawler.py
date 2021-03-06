import requests
from b4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'DESIRED WEBSITE' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = "DESIRED WEBSITE" + link.get('href')
            title = link.string

            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "DESIRED WEBSITE" + link.get('href')
        print(href)


trade_spider(3)