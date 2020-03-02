import bot_project.database as database
import bot_project.credentials as credentials
import requests
import urllib.request as saver
from bs4 import BeautifulSoup
from skpy import Skype
from datetime import datetime


def get_last_comics_data():
    url = 'https://dilbert.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    last_comics = soup.find(class_='comic-item-container')
    date = last_comics.get('data-id')
    title = last_comics.get('data-title')
    url = last_comics.get('data-image')
    id = url.split('.com/')[1][0:7]
    return id, date, title, url


def is_last_comics_in_DB():
    last_comics_data = get_last_comics_data()
    date_last_comics_in_DB = database.get_last_added_record()[1]
    today_date = str(datetime.today().date())
    comics_date = last_comics_data[1]
    if today_date == comics_date:
        if comics_date == date_last_comics_in_DB:
            return True
        else:
            return False
    else:
        return True


def get_recent_skype_chat(login):
    recent_chat = login.chats.recent()
    chat_id = list(recent_chat.keys())[0]
    return chat_id


def login_to_skype():
    skype = Skype(credentials.get_login(), credentials.get_password())
    return skype


def send_file_to_chat(login):
    channel = login.chats.chat(get_recent_skype_chat(login))
    image = 'bot_project/images/' + get_last_comics_data()[2] + '.jpg'
    saver.urlretrieve('https:' + get_last_comics_data()[3], image)
    channel.sendFile(open(image, 'rb'), get_last_comics_data()[2], image=True)


if __name__ == '__main__':
    if is_last_comics_in_DB():
        print('No new comics :(')
    else:
        database.insert_values(get_last_comics_data())
        sk = login_to_skype()
        send_file_to_chat(sk)
