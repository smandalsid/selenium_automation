from selenium import webdriver
import booking.constants as const
from selenium.webdriver.common.by import By
import time
from booking.booking_filterations import Booking_Filterations
from booking.booking_report import Booking_Report

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown=teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        else:
            while True:
                pass

    def land_first_page(self):
        self.get(const.BASE_URL)

    def click_cross(self):
        self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign in information.']").click()

    def change_currency(self, cur=None):
        but=self.find_element(By.XPATH, "//button[@data-testid='header-currency-picker-trigger']")
        but.click()
        newcur=self.find_element(By.XPATH, f"//div[text()='{cur}']")
        newcur.click()
    
    def dest(self, place):
        inp=self.find_element(By.NAME, "ss")
        inp.clear()
        inp.send_keys(place)
        time.sleep(2)
        drop=self.find_element(By.XPATH, f"//div[@class='cd1e09fdfe']")
        drop.click()

    def date(self, checkin, checkout):
        self.find_element(By.CSS_SELECTOR, "span[data-date='2023-05-17']").click()
        self.find_element(By.CSS_SELECTOR, "span[data-date='2023-05-21']").click()
    
    def search(self):
        self.find_element(By.XPATH, "//button[@class='fc63351294 a822bdf511 d4b6b7a9e7 cfb238afa1 c938084447 f4605622ad aa11d0d5cd']").click()

    def apply_filterations(self):
        filteration=Booking_Filterations(driver=self)
        filteration.apply_star_rating(4, 5)

    def report_results(self):
        hotels=self.find_elements(By.XPATH, "//div[@data-testid='property-card']")


        names=[]
        prices=[]
        ratings=[]
        reviews=[]
        d={}
        for i in hotels:

            try:
                print(
                    i.find_element(By.CSS_SELECTOR, "div[class='fcab3ed991 a23c043802']").text,
                    i.find_element(By.CSS_SELECTOR, "span[class='fcab3ed991 fbd1d3018c e729ed5ab6']").text,
                    i.find_element(By.CSS_SELECTOR, "div[class='b5cd09854e d10a6220b4']").text,i.find_element(By.CSS_SELECTOR, "div[class='b5cd09854e f0d4d6a2f5 e46e88563a']").text
                    )

            except:
                print(i.find_element(By.CSS_SELECTOR, "div[class='fcab3ed991 a23c043802']").text, "New to booking.com")

        

        
        # report = Booking_Report(hotels)
