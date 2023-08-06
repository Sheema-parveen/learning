from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#find out whether a value is present or not
class Sheema:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       #self.username = 'Admin'
       #self.password = 'admin123'
    def guvi(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        course= self.driver.find_element(by=By.LINK_TEXT, value="courses")#if u use wrong value it shows an error
        if course:
           course.click()
           print(course)
           print(type(course))
           self.driver.close()
        else:
           print(False)
           self.driver.close()
"""
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    
    def facebook(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.ID, value="email").send_keys("sheemarrr@gmail.com")
        self.driver.find_element(by=By.ID, value="pass").send_keys("sheema")
        self.driver.find_element(by=By.NAME, value="login").click()
        """
    


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
url_1="https://www.facebook.com/login/"
url_2="https://www.guvi.in/"
#Sheema(url).login()
#Sheema(url_1).facebook()
Sheema(url_2).guvi()