from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping_cart_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 30)

    driver.get("https://www.saucedemo.com/")

    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    first_name_field = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    first_name_field.send_keys("Ирина")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Серебрякова")

    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("443075")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text
    total_amount = total_text.replace("Total: $", "")

    assert total_amount == "58.29"

    driver.quit()

if __name__ == "__main__":
    test_shopping_cart_total()