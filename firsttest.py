from selenium import webdriver
from time import sleep

class Ombot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.omegle.com/")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]/img").click()
        sleep(2)


Ombot()
