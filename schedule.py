from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class ScheduleCollector:
    def start(self):
        options = webdriver.ChromeOptions()
        
        with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver:
            driver.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRXLWDLpnv-108LNY1vMSst-yvrWKqGlytCjlt2Qauid7gv7x2MLzKsO0fPWJ9Cfxj3AfevBvc9gGC0/pubhtml")
            while True:
                self.find_schedule(driver)
    def find_schedule(self,driver):
        table=driver.find_element(By.ID,"sheet-button-1944748597")
        table.click()
        sleep(5)

def main():
    collector = ScheduleCollector()
    collector.start()

if __name__ == "__main__":
    main()
