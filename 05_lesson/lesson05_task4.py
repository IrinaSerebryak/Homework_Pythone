from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


def test_login():

    driver = None

    try:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.implicitly_wait(10)

        driver.get("http://the-internet.herokuapp.com/login")

        print("Страница логина успешно загружена")
        print(f"Заголовок страницы: {driver.title}")

        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("✓ Введен username: tomsmith")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("✓ Введен password: SuperSecretPassword!")

        time.sleep(3)

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("✓ Нажата кнопка Login")

        time.sleep(3)

        success_message = driver.find_element(By.CLASS_NAME, "success")

        message_text = success_message.text
        print("\n" + "=" * 50)
        print("ТЕКСТ ИЗ ЗЕЛЕНОЙ ПЛАШКИ:")
        print(message_text)
        print("=" * 50)

        time.sleep(3)

        print("\nВсе операции выполнены успешно!")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

    finally:

        if driver:
            driver.quit()
            print("✓ Браузер закрыт методом quit()")

if __name__ == "__main__":
    test_login()