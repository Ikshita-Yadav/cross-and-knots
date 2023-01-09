from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/ikshi/bin/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://pillartopost.com/")
print(driver.title)

link = driver.find_element_by_link_text("Radon Testing")
link.click()

try:
    btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "GET AN INSPECTION"))
    )
    #print(teams.text)
    btn.click()

    #team = teams.find_elements_by_class_name("team-holder")
    time.sleep(5)
    driver.back()
    driver.back()
    driver.forward()


except:
    driver.quit()