from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os

# os.environ['PATH']+=r"/home/siddharth/Documents/ITC/selenium/driver"
driver=webdriver.Chrome()
driver.get("https://phptravels.com/demo/")

driver.implicitly_wait(2)
but=driver.find_element(By.CLASS_NAME, "btn-outline-dark")
but.click()

driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[1])
fname=driver.find_element(By.NAME, "firstname")
fname.send_keys("FIRSTNAME")
lname=driver.find_element(By.NAME, "lastname")
lname.send_keys("LASTNAME")
email=driver.find_element(By.NAME, "email")
email.send_keys("dfvefv3refw@mail.com")

# select = driver.find_element(By.CLASS_NAME, 'country-list')
cc=driver.find_element(By.CLASS_NAME, "flag-container")
cc.click()
code=driver.find_element(By.XPATH, "//li[@data-dial-code='91']")
code.click()
ph=driver.find_element(By.NAME, "phonenumber")
ph.send_keys("1231231234")


pwd="-B$t+d#Dw!Vz"
driver.find_element(By.NAME, "address1").send_keys("test")
driver.find_element(By.NAME, "city").send_keys("test")
driver.find_element(By.NAME, "state").send_keys("test")
driver.find_element(By.NAME, "postcode").send_keys("test")
driver.find_element(By.NAME, "password").send_keys(pwd)
driver.find_element(By.NAME, "password2").send_keys(pwd)

while True:
    pass