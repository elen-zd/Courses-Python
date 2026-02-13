from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
waitPicture = WebDriverWait(browser, 10)
browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
waitPicture.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#compass"))
)
waitPicture.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#calendar"))
)
waitPicture.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#award"))
)
waitPicture.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
)
three_img = browser.find_element(
    By.CSS_SELECTOR, "#award").get_attribute("src")

print(three_img)
browser.quit()
