from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com")

time.sleep(2)

quotes = driver.find_elements(By.CLASS_NAME, "text")
for quote in quotes:
    print(quote.text)

input()

driver.quit()
