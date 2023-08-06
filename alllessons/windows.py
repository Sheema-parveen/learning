
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Sheema:
  url="https://www.cowin.gov.in/"
  driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
  dashboard_xpath='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[2]/a'
  def child_window_open(self):
      self.driver.maximize_window()
      self.driver.get(self.url)
      sleep(3)
      parent_window_handle=self.driver.current_window_handle
      print("id of parent window",parent_window_handle)
      self.driver.find_element(by=By.XPATH ,value=self.dashboard_xpath).click()
      all_window_handles=self.driver.window_handles
      print(all_window_handles)
      for i in all_window_handles:
         if (i!=parent_window_handle):
             sleep(4)
             self.driver.close()
             break
  def parent_window_open(self):
      self.driver.maximize_window()
      self.driver.get(self.url)
      sleep(3)
      parent_window_handle=self.driver.current_window_handle
      print("id of parent window",parent_window_handle)
      self.driver.find_element(by=By.XPATH ,value=self.dashboard_xpath).click()
      all_window_handles=self.driver.window_handles
      print(all_window_handles)
      for i in all_window_handles:
         if (i!=parent_window_handle):
             self.driver.switch_to.window(i)
             sleep(4)
             self.driver.close()
             break     
#Sheema().parent_window_open()
Sheema().child_window_open()