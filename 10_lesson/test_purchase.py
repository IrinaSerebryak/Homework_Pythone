"""
Тесты для процесса покупки товаров.
"""

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Процесс покупки товаров")
@allure.description("Полный процесс покупки товаров в интернет-магазине")
class TestPurchase:
    """Класс тестов для процесса покупки."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Фикстура для инициализации драйвера."""
        with allure.step("Инициализация WebDriver"):
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install())
            )
            self.driver.maximize_window()
        yield
        with allure.step("Закрытие WebDriver"):
            self.driver.quit()

    @allure.story("Корзина покупок")
    @allure.tag("smoke", "purchase")
    @allure.testcase("TC-001", "Полный процесс покупки")
    def test_complete_purchase(self):
        """Тестирование полного процесса покупки товаров."""
        with allure.step("1. Открыть страницу логина"):
            login_page = LoginPage(self.driver)
            login_page.open()

        with allure.step("2. Выполнить вход с валидными данными"):
            inventory_page = login_page.login("standard_user", "secret_sauce")

        with allure.step("3. Добавить товары в корзину"):
            inventory_page.add_items_to_cart(["add-to-cart-sauce-labs-backpack",
                                              "add-to-cart-sauce-labs-bike-light"])

        with allure.step("4. Перейти в корзину"):
            cart_page = inventory_page.go_to_cart()

        with allure.step("5. Начать оформление заказа"):
            checkout_page = cart_page.checkout()

        with allure.step("6. Заполнить информацию о покупателе"):
            checkout_page.fill_info("John", "Doe", "12345")

        with allure.step("7. Перейти к обзору заказа"):
            overview_page = checkout_page.continue_to_overview()

        with allure.step("8. Проверить итоговую сумму"):
            total = overview_page.get_total_amount()

            with allure.step(f"Проверить, что сумма корректна: {total}"):
                assert float(total) > 0, "Итоговая сумма должна быть больше 0"