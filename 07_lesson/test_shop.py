from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_connection():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://www.saucedemo.com/")
        print("Страница успешно загружена!")
        print(f"Заголовок: {driver.title}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_connection()