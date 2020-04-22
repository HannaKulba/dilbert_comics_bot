import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_petrol_page():
    url = 'https://azs.belorusneft.by/sitebeloil/ru/center/azs/center/fuelandService/price/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def get_petrol_price(index):
    petrol_table = get_petrol_page().find(id='leftcontainer').find('table')
    petrol_prices_list = petrol_table.find_all('td', attrs={'class': 'col2'})
    return petrol_prices_list[index].string


def date():
    day = str(datetime.today().day)
    month = datetime.today().month
    year = str(datetime.today().year)
    if month < 10:
        month = '0' + str(month)
    return day + '.' + month + '.' + year


class Petrol():
    def __init__(self):
        pass

    def get_petrol_prices(self):
        today_date = date()
        petrol_92 = get_petrol_price(0)
        petrol_95 = get_petrol_price(1)
        petrol_98 = get_petrol_price(2)
        # dtz = get_petrol_price(1)
        dt = get_petrol_price(4)
        gaz = get_petrol_price(3)
        result = 'Цены на топливо на ' + today_date + '\n' + \
                 'АИ-92-К5: ' + petrol_92 + '\n' + \
                 'АИ-95-К5: ' + petrol_95 + '\n' + \
                 'АИ-98-К5: ' + petrol_98 + '\n' + \
                 'ДТ: ' + dt + '\n' + \
                 'ГАЗ ПБА: ' + gaz
        return result
