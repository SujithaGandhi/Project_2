# main.py

from Data import data
import Data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException

import Locators


class OrangeHRM:
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def __init__(self):
       self

   def start(self):
       self.driver.maximize_window()
       self.driver.get(data.Web_Data().url)
       self.driver.implicitly_wait(10)

   def login(self):
       try:
           self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
           self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
           self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
       except NoSuchElementException as e:
           print("Error : ", e)
       finally:
           self.driver.quit()

if __name__ == '__main__':
   orangehrm = OrangeHRM()
   orangehrm.start()
   orangehrm.login()
