import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def main():
    
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, 15)

    try:
        
        driver.get("https://hyperskill.org/login")

        driver.execute_script("window.open('https://www.avito.ru/');")

        driver.execute_script("window.open('https://www.ozon.ru/');")

        tabs = driver.window_handles

        for i, tab in enumerate(tabs, start=1):
            driver.switch_to.window(tab)
            wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
            print(f"[{i}] Title: {driver.title}")

      
        driver.switch_to.window(tabs[0])
        btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in')]")))
        driver.execute_script("arguments[0].click();", btn1)
        print("[OK] Клик по кнопке 'Sign in' на Hyperskill")

        
        driver.switch_to.window(tabs[1])
        link2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Недвижимость')]")))
        driver.execute_script("arguments[0].click();", link2)
        print("[OK] Клик по ссылке 'Недвижимость' на Avito")

      
        driver.switch_to.window(tabs[2])
        input3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='search']")))
        input3.click()
        print("[OK] Клик по поисковой строке на Ozon")

        print("\n Все шаги успешно выполнены!")

    finally:
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    main()
