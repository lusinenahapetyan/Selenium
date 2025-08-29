from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 30)

    try:
        driver.get("https://omayo.blogspot.com/")

        # === ЗАДАНИЕ 1 ===
        textbox = wait.until(EC.presence_of_element_located((By.ID, "ta1")))
        textbox.clear()
        textbox.send_keys("Hello from QA 🚀")
        print("[OK] Текст введён в textarea")

        # === ЗАДАНИЕ 2 ===
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "but2")))
        submit_btn.click()
        print("[OK] Кнопка Submit нажата")

        # === ЗАДАНИЕ 3 ===
        alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "alert1")))
        alert_btn.click()
        alert = wait.until(EC.alert_is_present())
        print(f"[OK] Текст алерта: {alert.text}")
        alert.accept()

        # === ЗАДАНИЕ 4 ===
        check_btn = wait.until(EC.element_to_be_clickable((By.ID, "alert2")))
        check_btn.click()

        hidden_div = wait.until(EC.presence_of_element_located((By.ID, "delayedText")))
        print(f"[OK] Появился текст: {hidden_div.text}")

        wait.until(EC.invisibility_of_element((By.ID, "deletesuccess")))
        print("[OK] Элемент 'deletesuccess' исчез со страницы")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
