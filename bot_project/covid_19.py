import requests
from bs4 import BeautifulSoup


def get_covid_page():
    url = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def get_date():
    date_info = get_covid_page().find(class_='label-counter').next_element.next_element.next_element.string
    date = str(date_info).split('Last updated:')[1]
    return date


def get_common_info():
    common_info = get_covid_page().find_all(id='maincounter-wrap')
    return common_info


def get_count(key):
    common_info_list = get_common_info()
    index = 0

    for i in range(len(common_info_list)):
        if key in str(common_info_list[i].find('h1').string).lower():
            index = i
            break

    count = str(get_common_info()[index].find('span').string).strip()
    return count


def get_main_table_countries():
    countries_table_rows = get_covid_page().find('table').find_all('tr')
    return countries_table_rows


def get_belarus_count(index):
    countries = get_main_table_countries()
    country_index = 0
    for i in range(len(countries)):
        if len(countries[i].find_all('td')) > 0:
            if 'Belarus' in str(countries[i].find('td').string):
                country_index = i
                break
    count = str(countries[country_index].find_all('td')[index].string).strip()
    if count == '':
        count = '0'
    return count


class COVID:
    def __init__(self):
        pass

    def get_common_covid_info(self):
        date = get_date()
        total = get_count('cases')
        deaths = get_count('deaths')
        recovered = get_count('recovered')

        result = '*Статистика по коронавирусу по состоянию на ' + str(date) + '\n' + \
                 'Количество зараженных: ' + total + '\n' + \
                 'Количество умерших: ' + deaths + '\n' + \
                 'Количество выздоровевших: ' + recovered + '\n' + \
                 '------------------------------------\n'
        return result

    def get_belarus_covid_info(self):
        total_bel = get_belarus_count(1)
        deaths_bel = get_belarus_count(3)
        recovered_bel = get_belarus_count(5)
        result = 'Статистика по коронавирусу в Беларуси\n' + \
                 'Количество зараженных: ' + total_bel + '\n' + \
                 'Количество умерших: ' + deaths_bel + '\n' + \
                 'Количество выздоровевших: ' + recovered_bel + \
                 '\n*приведенные данные могут отличаться от реальной ситуации'
        return result
