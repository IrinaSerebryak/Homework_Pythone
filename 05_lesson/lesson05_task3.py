from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:

    driver.implicitly_wait(10)

    driver.get("http://the-internet.herokuapp.com/inputs")

    print("Страница успешно загружена")

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("Sky")
    print("Введен текст: 'Sky'")

    time.sleep(1)

    input_field.clear()
    print("Поле очищено")

    time.sleep(1)

    input_field.send_keys("Pro")
    print("Введен текст: 'Pro'")

    time.sleep(2)

    print("Скрипт выполнен успешно!")

finally:

    driver.quit()
    print("Браузер закрыт")