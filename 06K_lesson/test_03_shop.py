from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_shopping_cart_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for item_id in items_to_add:
            add_button = driver.find_element(By.ID, item_id)
            add_button.click()

        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        first_name_field = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys("Иван")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")

        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text

        total_amount = total_text.split("$")[1]

        assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получили ${total_amount}"

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_cart_total()