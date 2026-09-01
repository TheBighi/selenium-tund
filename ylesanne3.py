from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

time.sleep(2)

add_button = driver.find_element(By.TAG_NAME, "button")

add_button.click()

input()

driver.quit()
