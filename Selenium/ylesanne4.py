from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

name = driver.find_element(By.NAME, "username")
name.send_keys("tomsmith")
time.sleep(2)
password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")
time.sleep(2)
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()
time.sleep(2)
success = driver.find_element(By.CLASS_NAME, "success")
print(success.text)
input()

driver.quit()
