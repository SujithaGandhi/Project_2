"""
Test Case to verify the Login of OrangeHRM with Pytest
test_login.py
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Data import data
from Locators import locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


class Test_OrangeHRM:

   @pytest.fixture
   def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.implicitly_wait(10)
       yield
       self.driver.close()

   def test_reset(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input').send_keys("Admin")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
       self.get_source = self.driver.page_source
       search_text = "Reset Password link sent successfully"
       print("success: Reset password link sent message displayed")
  
   def test_verifytitle(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click() 
       assert self.driver.title == "OrangeHRM"
       print("SUCCESS : Web Title Verified")

   def test_verifyadminheader(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click() 
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
       self.get_source = self.driver.page_source
       search_text = "User Management" and "Job" and "Organization" and "Qualification" and "Nationalities" and "Corporate Branding" and "Configuration"
       print("success: The user should be able to see the above mentioned Admin Page Headers on Admin Page")

   def test_verifyadminmenu(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click() 
       self.get_source = self.driver.page_source
       search_text = "Admin" and "PIM" and "Leave" and "Time" and "Recruitment" and "My Info" and "Performance" and "Dashboard" and "Directory" and "Maintenance" and "Buzz"
       print("success: The user should be able to see the above mentioned Admin Page Menu items on Admin Page")


