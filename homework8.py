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

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://demoqa.com/selectable")

        
        grid_tab = wait.until(EC.presence_of_element_located((By.ID, "demo-tab-grid")))
      
        driver.execute_script("arguments[0].scrollIntoView(true);", grid_tab)
        
        driver.execute_script("arguments[0].click();", grid_tab)
        time.sleep(1)

        
        element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='One']")))
        element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Five']")))

        element1.click()
        element2.click()
        time.sleep(1)

        
        assert "active" in element1.get_attribute("class")
        assert "active" in element2.get_attribute("class")
        print("[OK] Элементы One и Five выбраны.")

   
        element1.click()
        element2.click()
        time.sleep(1)

        assert "active" not in element1.get_attribute("class")
        assert "active" not in element2.get_attribute("class")
        print("[OK] Элементы One и Five сняты с выбора.")

        print("\n Все проверки успешно пройдены!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()


    