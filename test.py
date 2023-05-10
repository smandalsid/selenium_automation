from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com/")

#open tab
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't') 
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page 
driver.get('http://stackoverflow.com/')
# Make the tests...
time.sleep(5)
# close the tab
# (Keys.CONTROL + 'w') on other OSs.
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 'w') 


# driver.close()
while True:
    pass