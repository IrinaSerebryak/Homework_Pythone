from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


def test_input_field():

    driver = None

    try:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.implicitly_wait(10)

        driver.get("http://the-internet.herokuapp.com/inputs")

        print("Страница успешно загружена")

        input_field = driver.find_element(By.XPATH, "//input[@type='number']")

        print("Найдено поле ввода")

        input_field.send_keys("Sky")
        print("✓ Введен текст: 'Sky'")

        current_value = input_field.get_attribute("value")
        print(f"✓ Текущее значение поля: '{current_value}'")

        time.sleep(3)

        input_field.clear()
        print("✓ Поле очищено методом clear()")

        current_value = input_field.get_attribute("value")
        print(f"✓ Значение после очистки: '{current_value}'")

        time.sleep(5)

        input_field.send_keys("Pro")
        print("✓ Введен текст: 'Pro'")

        final_value = input_field.get_attribute("value")
        print(f"✓ Финальное значение: '{final_value}'")

        print("\nВсе операции выполнены успешно!")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

    finally:
        if driver:
            driver.quit()
            print("✓ Браузер закрыт методом quit()")


if __name__ == "__main__":
    test_input_field()