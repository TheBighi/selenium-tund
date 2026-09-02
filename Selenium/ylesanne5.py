from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

checkboxes_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
checkboxes_link.click()
time.sleep(2)

checkboxes = driver.find_elements(By.CSS_SELECTOR, "form#checkboxes input[type='checkbox']")

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

time.sleep(2)

driver.back()
time.sleep(2)

input()

driver.quit()
