from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class sheema():
    url="https://qavbox.github.io/demo/dragndrop/"
    driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #actionchains-drop and drop
    def drag_drop(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        action=ActionChains(self.driver)
        blue_box=self.driver.find_element(by=By.ID,value="draggable")
        green_box=self.driver.find_element(by=By.ID,value='droppable')
        action.drag_and_drop(source=blue_box,target=green_box).perform()
    #drag and drop by offset
    def drag_drop_offset(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        action=ActionChains(self.driver)
        blue_box=self.driver.find_element(by=By.ID,value='draggable')
        action.drag_and_drop_by_offset(blue_box,200,200).perform()
#sheema().drag_drop()
sheema().drag_drop_offset()


