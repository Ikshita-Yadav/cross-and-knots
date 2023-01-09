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

search = driver.find_element_by_name("postalcode")#found the serach box with HTML element name postal code
search.clear()#clears the text box
search.send_keys("test")#typed the string "test" in it
search.send_keys(Keys.RETURN) #Return == enter key ; pressing enter so that it does search

#we are asking the selenium to wait explicitly for the elemnt to appear before we run the next part of the code
#because we do not want it to run the code on the worng part or when it has not loaded yet.
try:
    teams = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "other-teams"))
    )
    #print(teams.text)

    team = teams.find_elements_by_class_name("team-holder")
    for t in team:
        header = t.find_element_by_class_name("teaminfo-header")
        loc = header.find_element_by_class_name("location-hover")
        name = loc.find_element_by_class_name("team-name")
        print(name.text)

finally:
    driver.quit()

#teams = driver.find_element_by_id("")


#print(driver.page_source)# gets us the html code for the entire page we are accessing

#time.sleep(5)#delays the exceution of the code by 5 seconds

#driver.close() #closes that tab
#driver.quit() #closes the entire browser 
