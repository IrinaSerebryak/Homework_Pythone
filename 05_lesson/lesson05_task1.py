from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_blue_button():

    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.implicitly_wait(10)

        driver.get("http://uitestingplayground.com/classattr")

        print("Страница успешно загружена")

        blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

        blue_button.click()
        print("Успешно кликнули на синюю кнопку")

        try:
            alert = driver.switch_to.alert
            print(f"Alert текст: {alert.text}")
            alert.accept()
            print("Alert принят")
        except:
            print("Alert не появился")

        time.sleep(5)

        print("Тест завершен успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()
            print("Браузер закрыт")


if __name__ == "__main__":
    test_blue_button()