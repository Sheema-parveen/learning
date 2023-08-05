from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
  
class basicprogram:
    #basic stuffs which are to be used  in the progrm are in constructor
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    #method to open the webpage of www.guvi.in
    def login(self):
        # to maximize the browser
        #open the firefox browser and render www.guvi.in on the browser
        self.driver.get(self.url)
        #to close the browser after automation is done
        self.driver.close()

s=basicprogram("https://www.guvi.in")
s.login()
