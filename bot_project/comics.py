import requests
from bot_project.database import Database
from bs4 import BeautifulSoup
from datetime import datetime


class Comics:
    def __init__(self):
        pass

    def get_last_comics_data(self):
        url = 'https://dilbert.com/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        last_comics = soup.find(class_='comic-item-container')
        date = last_comics.get('data-id')
        title = last_comics.get('data-title')
        url = last_comics.get('data-image')
        id = url.split('.com/')[1][0:7]
        return id, date, title, url

    def is_last_comics_in_DB(self):
        last_comics_data = self.get_last_comics_data()
        date_last_comics_in_DB = Database().get_last_added_record()[1]
        today_date = str(datetime.today().date())
        comics_date = last_comics_data[1]
        if today_date == comics_date:
            if comics_date == date_last_comics_in_DB:
                return True
            else:
                return False
        else:
            return True
