from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

field_username = "#username"
field_password = "#password"

username_input = driver.find_element(By.CSS_SELECTOR, field_username)
username_input.send_keys("tomsmith")
sleep(2)

password_input = driver.find_element(By.CSS_SELECTOR, field_password)
password_input.send_keys("SuperSecretPassword!")
sleep(2)

buttom_login = driver.find_element(By.CSS_SELECTOR, "button.radius").click()
sleep(2)
green_message = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(green_message)

driver.quit()
