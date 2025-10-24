from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("http://uitestingplayground.com/classattr")

print("Страница успешно загружена")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

blue_button.click()
print("Успешно кликнули на синюю кнопку")

alert = driver.switch_to.alert
print(f"Alert текст: {alert.text}")
alert.accept()
print("Alert принят")
print("Alert не появился")

time.sleep(5)

print("Тест завершен успешно!")

driver.quit()