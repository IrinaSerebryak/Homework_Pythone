from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)  # Увеличил время ожидания

    try:

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()  # Развернуть окно на весь экран

        wait.until(EC.presence_of_element_located((By.ID, "calculator")))

        delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        time.sleep(1)

        button_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'7')]")))
        button_7.click()

        button_plus = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'+')]")))
        button_plus.click()

        button_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'8')]")))
        button_8.click()

        button_equals = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'=')]")))

        actions = ActionChains(driver)
        actions.move_to_element(button_equals).click().perform()

        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        screen_element = driver.find_element(By.CLASS_NAME, "screen")
        result_text = screen_element.text
        assert result_text == "15", f"Ожидался результат 15, но получили {result_text}"

        print("Тест успешно завершен! Результат: 15")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise
    finally:
        driver.quit()