from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    driver.implicitly_wait(10)

    driver.get("http://the-internet.herokuapp.com/login")

    print("Страница логина успешно загружена")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Введен username: tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введен password: SuperSecretPassword!")

    time.sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Нажата кнопка Login")

    time.sleep(2)

    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")

    message_text = success_message.text
    print("\n" + "=" * 50)
    print("ТЕКСТ ИЗ ЗЕЛЕНОЙ ПЛАШКИ:")
    print(message_text)
    print("=" * 50)

    time.sleep(5)

    print("Скрипт выполнен успешно!")

finally:

    driver.quit()
    print("Браузер закрыт")