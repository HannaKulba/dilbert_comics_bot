from bot_project.configurations import Config
from skpy import Skype, SkypeGroupChat
from bot_project.comics import Comics
from bot_project.database import Database
from bot_project.exchange_rates import MoneyRates
from bot_project.covid_19 import COVID
import urllib.request as saver


class CustomSkype:
    def __init__(self):
        self.config = Config()
        self.username = self.config.get_login()
        self.password = self.config.get_password()
        self.chat_topic = self.config.get_chat_topic()

    def login_to_skype(self):
        skype = Skype(self.username, self.password)
        return skype

    def get_chat_id(self):
        topic = self.chat_topic
        recent_chat = self.login_to_skype().chats.recent()
        chats = list(recent_chat.values())
        for chat in chats:
            if type(chat) is SkypeGroupChat and chat.topic == topic:
                return chat.id
        return 'No chat with topic ' + topic

    def send_file_to_chat(self):
        login = self.login_to_skype()
        chat_id = self.get_chat_id()
        if 'No chat with topic' in chat_id:
            print(chat_id)
        else:
            if Comics().is_last_comics_in_DB():
                print('No new comics :(')
            else:
                comics_data = Comics().get_last_comics_data()
                Database().insert_values(comics_data)
                title = comics_data[2]
                image_url = comics_data[3]
                channel = login.chats.chat(chat_id)
                image = 'bot_project/images/' + title + '.jpg'
                saver.urlretrieve('https:' + image_url, image)
                channel.sendFile(open(image, 'rb'), title, image=True)

    def send_exchange_rates_and_covid_info_to_chat(self):
        login = self.login_to_skype()
        chat_id = self.get_chat_id()
        data = MoneyRates().get_exchange_rates_nb_rb()
        common_info_COVID = COVID().get_common_covid_info()
        belarus_info_COVID = COVID().get_belarus_covid_info()
        channel = login.chats.chat(chat_id)
        channel.sendMsg(data)
        channel.sendMsg(common_info_COVID + belarus_info_COVID)
