# Data Driven Testing Framework
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import locators
from excel_functions import sheema_excel_function


file = 'C:\\Users\\USER\\Desktop\\workspace\\POM\\test_data.xlsx'
sheet_number = 'Sheet1'
s = sheema_excel_function(file, sheet_number)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
rows = s.row_count()


# Read the Excel file using Rows and Columns
for row in range(2, rows+1):
   # Fetch the Username and Password from the Excel File
   username = s.read_data(row, 6)
   password = s.read_data(row, 7)
  

   # Selenium Automation Code
   driver.find_element(by=By.ID, value=locators.Locators().username_locator).send_keys(username)
   driver.find_element(by=By.ID, value=locators.Locators().password_locator).send_keys(password)
   driver.find_element(by=By.NAME, value=locators.Locators().submit_button).click()


   # Check for the TEST PASS or TEST FAIL
   if 'https://www.facebook.com/checkpoint/?next' in driver.current_url:
       print('SUCCESS : login with {a}'.format(a=username))
       s.write_data(row, 8, "TEST PASS")
       driver.back()
   elif 'https://www.facebook.com/' in driver.current_url:
       print("FAIL : login failure with {a}".format(a=username))
       s.write_data(row, 8, "TEST FAIL")
       driver.back()


# Quit/Close the WebDriver
driver.quit()
