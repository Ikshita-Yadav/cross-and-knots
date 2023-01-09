from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/Users/ikshi/bin/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)#another way to delay the code after this line for a specific amt of time

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
          purchase = ActionChains(driver)
          purchase.click(item)
          purchase.perform()
      
driver.quit()