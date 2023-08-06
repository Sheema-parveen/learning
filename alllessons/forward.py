from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Sheema:
  url="https://www.guvi.in/"
  driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

  def forward_back(self):
     self.driver.maximize_window()
     self.driver.get(self.url) 
     print(self.driver.title)
     print(self.driver.current_url)
     print()
     sleep(3)
     self.driver.find_element(by=By.LINK_TEXT ,value="Courses").click()
     print(self.driver.title)
     print(self.driver.current_url)
     print()
     sleep(4)
     self.driver.back()
     print(self.driver.title)
     print(self.driver.current_url)
     print()
     sleep(4)
     self.driver.forward()
     print(self.driver.title)
     print(self.driver.current_url)
     print()
     self.driver.close()
  def get_title(self):
     self.driver.get(self.url)
     return(self.driver.title)
  def get_url(self):
     print(self.driver.title)
     print(self.driver.current_url)
     
Sheema().forward_back()
