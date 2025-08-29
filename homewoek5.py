import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def task1_upload_file(driver):
    driver.get("https://demoqa.com/upload-download")
    time.sleep(2)

    test_file = "test_upload.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Hello, this is test upload for QA task.")

    upload_input = driver.find_element(By.ID, "uploadFile")
    abs_path = os.path.abspath(test_file)
    upload_input.send_keys(abs_path)

    uploaded_text = driver.find_element(By.ID, "uploadedFilePath").text
    assert os.path.basename(test_file) in uploaded_text, "Файл не загрузился!"
    print(f"[OK] Файл {test_file} успешно загружен!")

    os.remove(test_file)


def task2_download_files(driver):
    driver.get("http://the-internet.herokuapp.com/download")
    time.sleep(2)

    download_dir = "lesson_6/downloads"
    os.makedirs(download_dir, exist_ok=True)

    links = driver.find_elements(By.XPATH, "//a[contains(@href,'download')]")
    urls = [link.get_attribute("href") for link in links]

    for i, url in enumerate(urls, start=1):
        filename = os.path.join(download_dir, url.split("/")[-1])
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"[OK] Файл {i}: {filename} скачан")

    print(f"\n✅ Всего скачано файлов: {len(urls)}")


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        print("=== ЗАДАНИЕ 1 ===")
        task1_upload_file(driver)

        print("\n=== ЗАДАНИЕ 2 ===")
        task2_download_files(driver)

        print("\n🎉 Все задания выполнены успешно!")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
