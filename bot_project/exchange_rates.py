import requests
from bs4 import BeautifulSoup


def get_nb_rb_page():
    url = 'http://www.nbrb.by/statistics/rates/ratesdaily.asp'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def get_exchange_rates_table():
    soup = get_nb_rb_page()
    return soup.find(class_='currencyTable')


def get_exchange_rate(code):
    exchange_code_list = get_exchange_rates_table().find_all('td', attrs={'class': 'curAmount'})
    rates_list = get_exchange_rates_table().find_all('td', attrs={'class': 'curCours'})
    index = 0

    for i in range(len(exchange_code_list)):
        if code in exchange_code_list[i].string:
            index = i
            break

    rate = rates_list[index].find('div').string
    return rate


class MoneyRates:
    def __init__(self):
        pass

    def get_exchange_rates_nb_rb(self):
        date = get_nb_rb_page().find(id='curDate').string
        usd = get_exchange_rate('USD')
        euro = get_exchange_rate('EUR')
        rub = get_exchange_rate('RUB')
        result = 'АКТУАЛЬНЫЕ КУРСЫ ВАЛЮТ НБ РБ \n' + \
                 '                 на ' + date + '\n' + \
                 'USD        ' + usd + \
                 '\n-------------------\n' + \
                 'EUR        ' + euro + \
                 '\n-------------------\n' + \
                 '100RUB  ' + rub + \
                 '\n-------------------\n'
        return result
