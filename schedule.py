
from mail_sender import EmailSender

from time import sleep

import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class ScheduleCollector:

    def __init__(self):
        self.previous_schedule = None

    def start(self):
        options = webdriver.ChromeOptions()

        self.url="https://docs.google.com/spreadsheets/d/e/2PACX-1vRXLWDLpnv-108LNY1vMSst-yvrWKqGlytCjlt2Qauid7gv7x2MLzKsO0fPWJ9Cfxj3AfevBvc9gGC0/pubhtml"
        with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver:
            driver.get(self.url)
            while True:
                self.find_schedule(driver)
                sleep(3) 
    def find_schedule(self,driver):
        today = datetime.datetime.now()
        table_button=driver.find_element(By.ID,"sheet-button-1944748597")
        table_button.click()
        sleep(5)
        schedule_table = driver.find_element(By.ID, "sheets-viewport")
        current_schedule = schedule_table.text

        self.check_for_differences(current_schedule,today)

    def check_for_differences(self,current_schedule,today):
        if self.previous_schedule is None:
            self.previous_schedule = current_schedule
            print("Schedule initialized.")
        elif self.previous_schedule != current_schedule:
            email_sender=EmailSender()
            email_sender.send_email(f"Schedule has been changed at {today}. Please check your new schedule!\n"+self.url)
            self.previous_schedule = current_schedule
        else:
            print(f"No changes detected at {today}.")

            

def main():
    collector = ScheduleCollector()
    collector.start()

if __name__ == "__main__":
    main()
