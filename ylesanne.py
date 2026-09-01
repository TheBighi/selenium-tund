from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

accept_terms = driver.find_element(By.CLASS_NAME, "sy4vM")
time.sleep(1.5)
accept_terms.click()

time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Sander Tamm" + Keys.RETURN)

input()

driver.quit()
