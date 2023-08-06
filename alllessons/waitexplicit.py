from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By 
#python explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#python Exception class
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

class sheema:
    driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait=WebDriverWait(driver,10)
    username_inputbox="email" #ID
    password_inputbox="pass" #ID
    submit_button="login" #NAME

    def __init__(self,url):
       self.url = url
       self.driver.get(self.url)
    

    def element_present(self):
        try: 
            username_locator = self.wait.until(EC.presence_of_element_located((By.ID, self.username_inputbox)))
            password_locator=self.wait.until(EC.presence_of_element_located((By.ID, self.password_inputbox)))
            submit_button=self.wait.until(EC.presence_of_element_located((By.NAME, self.submit_button)))
            print("Username inputbox#",username_locator)
            print("password inputbox #",password_locator)
            print("submitButton #",submit_button)
            username_locator.send_keys("suman@guvi.in")
            password_locator.send_keys("secret@123")
            submit_button.click()
        except NoSuchElementException as e:
            print(e)
        finally:
            self.driver.quit()
    def title(self):
        try:
           print(self.driver.title!="Facebook – log in or sign up")
        except:
           print("web url wrong!")
        finally:
            self.driver.quit()

    def url_to(self, test_url):
        try:            
            if(test_url != self.driver.current_url):
                 return True
        except:
            return False
        finally:
            self.driver.quit()

    
    def visible_element(self):
        try:
            username_locator = self.wait.until(EC.presence_of_element_located((By.ID, self.username_inputbox)))
            password_locator = self.wait.until(EC.presence_of_element_located((By.ID, self.password_inputbox)))
            submit_button = self.wait.until(EC.presence_of_element_located((By.NAME, self.submit_button)))
            if(username_locator and password_locator and submit_button):
                username_locator.send_keys('suman@guvi.in')
                password_locator.send_keys('secret@123')
                submit_button.click()
        except StaleElementReferenceException as e:
            print(e)
        finally:
            self.driver.quit()

   

url="https://www.facebook.com/"
s=sheema(url)
#s.element_present()
#s.title()
#print(s.url_to("www.facebook.com"))

print(s.url_to("https://www.facebook.com/"))
#s.title()#self.driver.title=="Facebook–log in or sign up") o/p web url wrong
#(test_url != self.driver.current_url)0/p none

#s.title()#self.driver.title!="Facebook–log in or sign up")
#(test_url != self.driver.current_url)0/p none

s.title()#self.driver.title!="Facebook–log in or sign up") o/p web url wrong
#(test_url == self.driver.current_url)0/p none



#print(s.url_to("www.facebook.com"))
"""
#s.title()#self.driver.title=="Facebook–log in or sign up") o/p true web url wrong
#(test_url != self.driver.current_url)0/p web url wrong

#s.title()#self.driver.title!="Facebook–log in or sign up") o/p true web url wrong
#(test_url != self.driver.current_url)

#s.title()#self.driver.title!="Facebook–log in or sign up") o/p true web url wrong
#(test_url != self.driver.current_url)0/p web url wrong

#s.title()#self.driver.title!="Facebook–log in or sign up") o/p true web url wrong
#(test_url == self.driver.current_url)0/p web url wrong

#s.title()#self.driver.title=="Facebook – log in or sign up") o/p true 
#(test_url != self.driver.current_url)0/p web url wrong

#s.title()#self.driver.title!="Facebook – log in or sign up") o/p  web url wrong
#(test_url != self.driver.current_url)0/p web url wrong

#s.title()#self.driver.title!="Facebook – log in or sign up")o/p  web url wrong
#(test_url == self.driver.current_url)o/p none  

s.title()#self.driver.title=="Facebook – log in or sign up")0/p web url wrong 
#(test_url == self.driver.current_url)o/p none

"""

#s.visible_element()