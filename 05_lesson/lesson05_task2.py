from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:

    driver.implicitly_wait(10)

    driver.get("http://uitestingplayground.com/dynamicid")

    print("Страница успешно загружена")

    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

    button_id = blue_button.get_attribute("id")
    print(f"Текущий ID кнопки: {button_id}")

    blue_button.click()
    print("Успешно кликнули на синюю кнопку")

    time.sleep(5)

    print("Скрипт выполнен успешно!")

finally:
    driver.quit()
    print("Браузер закрыт")