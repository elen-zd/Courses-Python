from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)
search_field = "input"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Sky")
sleep(2)
search_input.clear()
search_input.send_keys("Pro")
sleep(2)

driver.quit()
