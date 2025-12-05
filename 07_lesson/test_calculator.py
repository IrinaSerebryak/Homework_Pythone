import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)

    try:
        # Открываем калькулятор
        calculator_page.open()

        # Устанавливаем задержку
        calculator_page.set_delay(45)

        # Выполняем вычисление 7 + 8
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_equals()  # Используем специальный метод для =

        # Получаем и проверяем результат
        result = calculator_page.get_result()
        assert result == "15", f"Ожидался результат 15, но получили {result}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()