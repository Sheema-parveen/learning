from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Suman:
    # basic stuffs which are to be used in the program are in the constructor
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


    # Method to open the webpage of www.guvi.in
    def login(self):
        self.driver.get(self.url)


s = Suman('https://www.guvi.in')


s.login()


#after modified using comment line

