from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class sheema():
    url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username="Admin"
    password="admin123"
    click_button='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    logout_1='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
    logout_2=""

    def logout(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        #login into dashboard of the HRM
        cookies_1=self.driver.get_cookies()
        cookies_home_page=cookies_1[0]["value"]
        print('home page cookies:',cookies_home_page)
        self.driver.find_element(by=By.NAME,value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME,value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH,value=self.click_button).click()
        #logout from dashboard
        cookies_2=self.driver.get_cookies()
        cookie_login =cookies_2[0]['value']
        print('logged in cookie:',cookie_login)
        sleep(4)
        logout_button=self.driver.find_element(by=By.XPATH,value=self.logout_1)
        action=ActionChains(self.driver)
        action.click(on_element=logout_button)
        action.perform()
        sleep(3)
        self.driver.find_element(by=By.LINK_TEXT,value="Logout").click()

print(sheema().logout())