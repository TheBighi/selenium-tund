from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# TEST 1: Vormi täitmine vigaste andmetega ja veateate kontrollimine

def test_1_invalid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("vale_kasutaja")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("vale_parool")
        
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()
        
        flash_message = driver.find_element(By.CLASS_NAME, "flash.error")
        assert "Your username is invalid!" in flash_message.text, "Veateate tekst ei vasta oodatule!"
        print("Test 1 EDASIKAS: Vigase logimise veateade on õige.")
        
    finally:
        driver.quit()



# TEST 2: Mitmesammuline otsing ja tulemuste kontrollimine

def test_2_search_and_verify():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://demoqa.com/webtables")
        
        search_box = driver.find_element(By.ID, "searchBox")
        search_box.send_keys("Cierra")
        
        first_name_cell = driver.find_element(By.XPATH, "//div[@class='rt-tbody']//div[@class='rt-td'][1]")
        
        assert first_name_cell.text == "Cierra", f"Oodatud nimi oli 'Cierra', kuid leiti '{first_name_cell.text}'"
        print("Test 2 EDASIKAS: Otsing leidis tabelist õige isiku.")
        
    finally:
        driver.quit()


# TEST 3: Töö mitme elemendiga (Nimekirja ülevaatus)

def test_3_multiple_elements_check():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        
        add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
        
        for _ in range(4):
            add_button.click()
            time.sleep(0.3)
            
        delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
        
        assert len(delete_buttons) == 4, f"Oodati 4 elementi, kuid leiti {len(delete_buttons)}"
        print(f"Test 3 EDASIKAS: Lehelt leiti edukalt kõik {len(delete_buttons)} lisatud elementi.")
        
    finally:
        driver.quit()


# TEST 4: Dropdown-menüü valik ja valitud väärtuse kontroll
def test_4_dropdown_selection():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")
        
        dropdown_element = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_element)
        
        select.select_by_visible_text("Option 2")
        
        selected_option = select.first_selected_option
        assert selected_option.text == "Option 2", "Rippmenüüst ei valitud õiget elementi!"
        print("Test 4 EDASIKAS: Rippmenüü valik 'Option 2' töötab õigesti.")
        
    finally:
        driver.quit()


# TEST 5: Dünaamilise elemendi ildumise ootamine
def test_5_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()
        
        wait = WebDriverWait(driver, 10)
        finish_text = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        
        assert finish_text.text == "Hello World!", "Dünaamiliselt laetud tekst on vale!"
        print("Test 5 EDASIKAS: Dünaamiline element ilmus ja selle tekst on õige.")
        
    finally:
        driver.quit()


# TESTIDE KÄIVITAMINE
if __name__ == "__main__":
    print("--- AUTOMATISEERITUD TESTIDE KÄIVITAMINE ---\n")
    test_1_invalid_login()
    test_2_search_and_verify()
    test_3_multiple_elements_check()
    test_4_dropdown_selection()
    test_5_dynamic_loading()
    print("\n--- KÕIK TESTID ON SIKKUSLIKULT LÄBITUD! ---")
