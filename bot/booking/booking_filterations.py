from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

class Booking_Filterations:
    def __init__(self, driver:WebDriver):
        self.driver=driver

    def apply_star_rating(self, *star_values):
        filter=self.driver.find_element(By.ID, "filter_group_class_:R14q:")
        filter_childs=filter.find_elements(By.CSS_SELECTOR, "*")
        # print(len(filter_childs))

        for star in star_values:
            for element in filter_childs:
                if str(element.get_attribute("innerHTML")).strip()==f"{star} stars":
                    element.click()
            time.sleep(1)

        sort_but=self.driver.find_element(By.XPATH, "//button[@data-testid='sorters-dropdown-trigger']")
        sort_but.click()
        self.driver.find_element(By.XPATH, "//button[@data-id='price']").click()