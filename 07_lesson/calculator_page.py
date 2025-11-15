from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()
        self.wait.until(EC.presence_of_element_located((By.ID, "calculator")))

    def set_delay(self, delay):
        delay_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(str(delay))
        time.sleep(1)  # Даем время для применения задержки

    def click_button(self, button_text):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']")))

        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)

    def click_equals(self):

        equals_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", equals_button)
        time.sleep(0.5)

        actions = ActionChains(self.driver)
        actions.move_to_element(equals_button).click().perform()

    def get_result(self, wait_time=45):

        time.sleep(wait_time)  # Ждем вычисления
        screen_element = self.driver.find_element(By.CLASS_NAME, "screen")
        return screen_element.text