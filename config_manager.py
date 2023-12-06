import configparser


class ConfigManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('setting/config.ini')

    def get_domain(self, env):
        print(self.config)
        return "http://localhost:1313/CodeTutor/"
