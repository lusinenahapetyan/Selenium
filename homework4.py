from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def task1_fill_textboxes(driver):
    driver.get("https://demoqa.com/text-box")
    time.sleep(2)  # ждём загрузку

    # Данные для заполнения
    data = {
        "userName": "Lusine QA",
        "userEmail": "qa@example.com",
        "currentAddress": "Yerevan, Armenia",
        "permanentAddress": "QA Engineer Forever"
    }

    for field_id, value in data.items():
        field = driver.find_element(By.ID, field_id)
        field.clear()
        field.send_keys(value)
        # Проверка, что введено корректно
        entered = field.get_attribute("value")
        assert entered == value, f"Поле {field_id} не заполнилось! -> {entered}"
        print(f"[OK] Поле {field_id} = '{entered}'")

def task2_click_status_codes(driver):
    driver.get("http://the-internet.herokuapp.com/status_codes")
    time.sleep(2)

    # Находим все ссылки со статус-кодами
    links = driver.find_elements(By.XPATH, "//a[contains(@href, 'status_codes')]")

    # Собираем href, чтобы не потерять элементы при перезагрузке
    urls = [link.get_attribute("href") for link in links]

    for url in urls:
        driver.get(url)
        print(f"[CLICKED] Перешли по ссылке: {url}")
        time.sleep(1)
        # Возвращаемся на стартовую
        driver.back()
        time.sleep(1)

def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        print("=== ЗАДАНИЕ 1 ===")
        task1_fill_textboxes(driver)

        print("\n=== ЗАДАНИЕ 2 ===")
        task2_click_status_codes(driver)

        print("\n✅ Все проверки выполнены успешно!")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()


def main():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        print("=== ЗАДАНИЕ 1 ===")
        task1_fill_textboxes(driver)

        print("\n=== ЗАДАНИЕ 2 ===")
        task2_click_status_codes(driver)

        print("\n✅ Все проверки выполнены успешно!")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()