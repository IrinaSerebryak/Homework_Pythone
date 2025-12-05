from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first_name, last_name, postal_code):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)

    def continue_to_overview(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        from checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.driver)