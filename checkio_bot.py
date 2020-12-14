import json
from dataclasses import dataclass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import sys
import time

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
        self.base_url = "https://checkio.org/"
        self.search_text = "Python CheckIO"  # bot akan mencari Dengan kunci ini
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.command_or_control = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

    def single_interation_over_session(self):
        self.login_to_checkio()
        links = self.get_islands_links()
        print(links)
        time.sleep(5)
        self.driver.quit()

    def get_islands_links(self):
        # mencari map__station_state_opened di class
        opened_stations = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'map__station_state_opened')]")
        opened_stations_links = []
        for link in opened_stations:
            opened_stations_links.append(link.find_element_by_css_selector(
                'a.map__station__link').get_attribute('href'))
        return opened_stations_links

    def login_to_checkio(self):
        self.driver.get(self.base_url)
        self.get_on_python_checkio()
        self.put_credentials_to_form()

    # Click menuju page sign
    def get_on_python_checkio(self):
        try:
            self.driver.find_element_by_link_text('Python').click()
            time.sleep(2)
        except NoSuchElementException:
            print("Incorrect Page")

    def put_credentials_to_form(self):
        try:
            self.driver.find_element_by_id('id_username').send_keys(self.login)
            time.sleep(2)
            password_field = self.driver.find_element_by_id('id_password')
            password_field.send_keys(self.password)
            password_field.submit()
            time.sleep(3)
        except NoSuchElementException:
            print("Failed to login to checkIO")


if __name__ == '__main__':
    credentials = read_credentials()
    bot = CheckIOSolver(credentials.get('username'),
                        credentials.get('password'))
    bot.single_interation_over_session()
