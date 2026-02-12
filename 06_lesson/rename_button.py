from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")

field = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
field.send_keys("SkyPro")
browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()
button = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(button)
browser.quit()
