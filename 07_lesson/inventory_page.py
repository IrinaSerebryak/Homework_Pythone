from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self, items):
        for item_id in items:
            add_button = self.driver.find_element(By.ID, item_id)
            add_button.click()

    def go_to_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        from cart_page import CartPage
        return CartPage(self.driver)