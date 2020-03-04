import configparser


class Config:
    def __init__(self):
        pass

    def read_config_file(self):
        config = configparser.RawConfigParser()
        config.read('ConfigFile.properties')
        return config

    def get_login(self):
        config = self.read_config_file()
        return config.get('SkypeSection', 'skype.username')

    def get_password(self):
        config = self.read_config_file()
        return config.get('SkypeSection', 'skype.password')

    def get_chat_topic(self):
        config = self.read_config_file()
        return config.get('SkypeSection', 'skype.chatTopic')
