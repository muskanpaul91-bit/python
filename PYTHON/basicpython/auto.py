from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
sleep(2)
browser.get("https://youtube.com")
sleep(5)
element = browser.find_element("name", "search_query")
search ="Best Indian food"                                                    # OR  element.send_keys("Indian Foods")
for char in search:
    element.send_keys(char)
    sleep(0.4)
sleep(2)
element.send_keys(Keys.ENTER)
sleep(2)
first_short = browser.first_element("xpath", 'copy content')
first_short.click()
while True:
    next_btn = browser.find_element("xpath",'copy path')
    next_btn.click()
    sleep(25)