"""
Page Object Model для страницы калькулятора.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import allure


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Returns:
            None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()
        self.wait.until(EC.presence_of_element_located((By.ID, "calculator")))

    @allure.step("Установить задержку: {delay}")
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает значение задержки вычислений.

        Args:
            delay (int): Значение задержки в секундах

        Returns:
            None
        """
        delay_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay))
        time.sleep(1)

    @allure.step("Нажать кнопку: {button_text}")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку с указанным текстом.

        Args:
            button_text (str): Текст на кнопке

        Returns:
            None
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
        )
        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Нажать кнопку 'равно'")
    def click_equals(self) -> None:
        """
        Нажимает кнопку '='.

        Returns:
            None
        """
        equals_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", equals_button)
        time.sleep(0.5)

        actions = ActionChains(self.driver)
        actions.move_to_element(equals_button).click().perform()

    @allure.step("Получить результат вычисления")
    def get_result(self, wait_time: int = 45) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        Args:
            wait_time (int): Время ожидания результата в секундах

        Returns:
            str: Текст результата
        """
        time.sleep(wait_time)
        screen_element = self.driver.find_element(By.CLASS_NAME, "screen")
        return screen_element.text