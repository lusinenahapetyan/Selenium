from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse

def wait_for_load(driver, timeout=20):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

def host(url: str) -> str:
    return urlparse(url).hostname or ""

def main():
    
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        
        driver.get("https://vk.com")
        wait_for_load(driver)
        first_title = driver.title
        first_url = driver.current_url
        print(f"[1] VK title: {first_title}")
        print(f"[1] VK url:   {first_url}")

      
        driver.get("https://ya.ru")
        wait_for_load(driver)
        second_title = driver.title
        second_url = driver.current_url
        print(f"[2] YA title: {second_title}")
        print(f"[2] YA url:   {second_url}")

      
        driver.back()
        wait_for_load(driver)
        back_title = driver.title
        back_url = driver.current_url

       
        assert host(back_url) == host(first_url) or back_title == first_title, (
            f"Ожидали вернуться на VK. Сейчас title='{back_title}', url='{back_url}'"
        )
        print(f"[3] Back OK: {back_title} | {back_url}")

    
        driver.refresh()
        wait_for_load(driver)
        refreshed_url = driver.current_url
        print(f"[4] After refresh url: {refreshed_url}")

        
        before_forward_url = driver.current_url
        driver.forward()
        wait_for_load(driver)
        forward_url = driver.current_url
        print(f"[5] Forward url: {forward_url}")

        assert forward_url != before_forward_url, (
            f"URL не изменился после перехода вперёд: {forward_url}"
        )

       
        assert host(forward_url) == host(second_url), (
            f"Ожидали хост как у ya.ru, но получили: {host(forward_url)}"
        )

        print(" Все проверки пройдены успешно.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()