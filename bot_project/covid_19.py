import requests
from bs4 import BeautifulSoup


class COVID:
    def __init__(self):
        pass

    def get_common_covid_info(self):
        url = 'https://www.worldometers.info/coronavirus/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        date_info = soup.find(class_='label-counter').next_element.next_element.string
        date = str(date_info).split('Last updated:')[1]
        common_info = soup.find_all(class_='maincounter-number')
        total = str(common_info[0].find('span').string).strip()
        deaths = common_info[1].find('span').string
        recovered = common_info[2].find('span').string

        result = '*Статистика по коронавирусу по состоянию на ' + str(date) + '\n' + \
                 'Количество зараженных: ' + total + '\n' + \
                 'Количество умерших: ' + deaths + '\n' + \
                 'Количество выздоровевших: ' + recovered + '\n' + \
                 '------------------------------------\n'
        return result

    def get_belarus_covid_info(self):
        url = 'https://www.worldometers.info/coronavirus/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        bel = soup.find_all('tr')
        index = 0
        for i in range(len(bel)):
            if len(bel[i].find_all('td')) > 0:
                if ' Belarus ' == str(bel[i].find_all('td')[0].string):
                    index = i

        total_bel = bel[index].find_all('td')[1].string
        deaths_bel = str(bel[index].find_all('td')[3].string).strip()
        if deaths_bel == '':
            deaths_bel = '0'
        recovered_bel = str(bel[index].find_all('td')[5].string).strip()
        result = 'Статистика по коронавирусу в Беларуси\n' + \
                 'Количество зараженных: ' + total_bel + '\n' + \
                 'Количество умерших: ' + deaths_bel + '\n' + \
                 'Количество выздоровевших: ' + recovered_bel + \
                 '\n*приведенные данные могут отличаться от реальной ситуации'
        return result
