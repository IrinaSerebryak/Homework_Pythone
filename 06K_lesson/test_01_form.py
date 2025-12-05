from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_form_validation():
    driver = webdriver.Edge()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        try:
            submit_button.click()
        except:
            driver.execute_script("arguments[0].click();", submit_button)
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.is-invalid")))
        except TimeoutException:
            import time
            time.sleep(30)

        zip_code_field = driver.find_element(By.ID, "zip-code")

        assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"

        fields_to_check = [
            ("first-name", "First name"),
            ("last-name", "Last name"),
            ("address", "Address"),
            ("e-mail", "Email"),
            ("phone", "Phone"),
            ("city", "City"),
            ("country", "Country"),
            ("job-position", "Job position"),
            ("company", "Company")
        ]
        for field_id, field_name in fields_to_check:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class"), f"Поле {field_name} не подсвечено зеленым"

    finally:
        driver.quit()
if __name__ == "__main__":
    test_form_validation()