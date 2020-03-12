import requests
from bs4 import BeautifulSoup


class MoneyRates:
    def __init__(self):
        pass

    def get_exchange_rates_nb_rb(self):
        url = 'http://www.nbrb.by/statistics/rates/ratesdaily.asp'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        date = soup.find(id='curDate').string
        exchange_rates_table = soup.find(class_='currencyTable')
        usd = exchange_rates_table.find_all('tr')[5].find(class_='curCours').find('div').string
        euro = exchange_rates_table.find_all('tr')[6].find(class_='curCours').find('div').string
        rub = exchange_rates_table.find_all('tr')[17].find(class_='curCours').find('div').string
        result = 'АКТУАЛЬНЫЕ КУРСЫ ВАЛЮТ НБ РБ \n' + \
                 '                 на ' + date + '\n' + \
                 'USD        ' + usd + \
                 '\n-------------------\n' + \
                 'EURO      ' + euro + \
                 '\n-------------------\n' + \
                 '100RUB  ' + rub + \
                 '\n-------------------\n'
        return result
