from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
#dropdown
from selenium.webdriver.support.ui import Select
from time import sleep

class sheema:
    url="https://www.imdb.com/search/title/"
    driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#click the drop down
    def click_select_by_user_rating(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        user_rating= self.driver.find_element(by=By.NAME,value="user_rating-min")
        sleep(4)
        user_rating.click()
#select by visible text
    def select_by_user_rating(self,rating_count):
        rating_count=str(rating_count)
        self.driver.maximize_window()
        self.driver.get(self.url)
        user_rating=self.driver.find_element(by=By.NAME,value="user_rating-min")
        user_rating_dropdown=Select(user_rating)
        user_rating_dropdown.select_by_visible_text(rating_count)
#select one values from multiple dropdown
    def select_by_language(self,lang):
        self.driver.maximize_window()
        self.driver.get(self.url)
        language=self.driver.find_element(by=By.NAME,value="languages")
        language_dropdown=Select(language)
        language_dropdown.select_by_value(lang)

    def select_multiple_values(self,lang):
        self.driver.maximize_window()
        self.driver.get(self.url)
        language=self.driver.find_element(by=By.NAME,value="languages")
        language_dropdown=Select(language)
        language_dropdown.select_by_value("af")
        sleep(2)
        language_dropdown.select_by_value("guq")
        sleep(2)
        language_dropdown.select_by_value("ab")
#using for loop     
    def select_by_multiple_values(self,lang_data):
        self.driver.maximize_window()
        self.driver.get(self.url)
        language=self.driver.find_element(by=By.NAME,value="languages")
        language_dropdown=Select(language)
        for lang in range(len(lang_data)):
            language_dropdown.select_by_value(lang_data[lang])
            sleep(2)
#deselectby name
    def disselect_by_name(self,lang_data):
        language= self.driver.find_element(by=By.NAME,value="languages")
        language_dropdown=Select(language)
        for lang in range(len(lang_data)):
            language_dropdown.deselect_by_value(lang_data[lang])
            sleep(2)

    

    # deselect by text
    def disselect_by_text(self, lang_data):
        language = self.driver.find_element(by=By.NAME, value="languages")
        language_dropdown = Select(language)
        for lang in range(len(lang_data)):
            language_dropdown.deselect_by_visible_text(lang_data[lang])
            sleep(2)
   
 # select all the values of the dropdown
    def select_all(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        language = self.driver.find_element(by=By.NAME, value="languages")
        language_dropdown = Select(language)
        language_option = language_dropdown.options
        for lang in language_option:
            lang.click()    



#sheema().click_select_by_user_rating()
#sheema().select_by_user_rating(1.1)
#sheema().select_by_language("en")
sheema().select_multiple_values(["ab","guq","af"])
#sheema().select_by_multiple_values(["ab","guq","af"])
sheema().disselect_by_name(["ab","guq","af"])
#sheema().disselect_by_text(["Abkhazian", "Aché", "Afrikaans"])
#sheema().select_all()
