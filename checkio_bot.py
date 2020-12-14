import json
from dataclasses import dataclass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import sys

# load key dari file JSON


def read_credentials():
    secrets = 'secrets.json'
    with open(secrets) as f:
        keys = json.loads(f.read())
        return keys


@dataclass
class Task:
    name: str
    links: str


# masuk ke checkio intial
class CheckIOSolver:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.google = "https://www.google.com/"
        self.base_url = "https://checkio.org"
        self.search_text = "Python CheckIO"  # bot akan mencari Dengan kunci ini
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.command_or_control = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL


if __name__ == '__name__':
    credentials = read_credentials()
