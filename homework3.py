from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://hyperskill.org/tracks")
time.sleep(3)

locators = {
    "page_title": ("xpath", "//h1"),
    "first_track_card": ("xpath", "(//div[contains(@class, 'track-card')])[1]"),
    "search_input": ("xpath", "//input[@type='search']"),
    "footer": ("xpath", "//footer"),
    "navigation_bar": ("xpath", "//nav"),
    "login_button": ("xpath", "//a[contains(@href,'login')]"),
}

for name, (by, value) in locators.items():
    try:
        driver.find_element(By.XPATH, value)
        print(f"[OK] {name} найден")
    except:
        print(f"[FAIL] {name} не найден")

driver.quit()


