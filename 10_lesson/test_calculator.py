"""
Тесты для калькулятора.
"""

import sys
import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.calculator_page import CalculatorPage

@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест медленного калькулятора")
@allure.description("Проверка работы калькулятора с задержкой вычислений")
class TestCalculator:
    """Класс тестов для калькулятора."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Фикстура для инициализации драйвера."""
        with allure.step("Инициализация WebDriver"):
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install())
            )
            self.calculator_page = CalculatorPage(self.driver)
        yield
        with allure.step("Закрытие WebDriver"):
            self.driver.quit()

    @allure.story("Основные операции")
    @allure.tag("smoke", "calculator")
    def test_slow_calculator(self):
        """Тестирование вычисления 7 + 8 с задержкой."""
        with allure.step("Открыть калькулятор"):
            self.calculator_page.open()

        with allure.step("Установить задержку 45 секунд"):
            self.calculator_page.set_delay(45)

        with allure.step("Выполнить операцию 7 + 8"):
            self.calculator_page.click_button('7')
            self.calculator_page.click_button('+')
            self.calculator_page.click_button('8')
            self.calculator_page.click_equals()

        with allure.step("Получить и проверить результат"):
            result = self.calculator_page.get_result()

            with allure.step(f"Проверить, что результат равен 15 (получено: {result})"):
                assert result == "15", f"Ожидался результат 15, но получили {result}"


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results"])