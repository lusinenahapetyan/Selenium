import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form_positive(setup_browser):
    driver = setup_browser

    first_name = "Lusine"
    driver.find_element(By.ID, "firstName").send_keys(first_name)
    time.sleep(1)
    assert driver.find_element(By.ID, "firstName").get_attribute("value") == first_name

    last_name = "Nahapetyan"
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    time.sleep(1)
    assert driver.find_element(By.ID, "lastName").get_attribute("value") == last_name

    email = "lusinenahapetyan@gmail.com"
    driver.find_element(By.ID, "userEmail").send_keys(email)
    time.sleep(1)
    assert driver.find_element(By.ID, "userEmail").get_attribute("value") == email

    phone = "077554581"
    driver.find_element(By.ID, "userNumber").send_keys(phone)
    time.sleep(1)
    assert driver.find_element(By.ID, "userNumber").get_attribute("value") == phone

    address = "s.matnishyan190"
    driver.find_element(By.ID, "currentAddress").send_keys(address)
    time.sleep(1)
    assert driver.find_element(By.ID, "currentAddress").get_attribute("value") == address


@pytest.mark.parametrize(
    "first_name,last_name,email,phone",
    [
        ("", "Nahapetyan", "lusinenahapetyan@gmail.com", "077554581"),  
        ("Lusine", "", "lusinenahapetyan@gmail.com", "077554581"),       
        ("Lusine", "Nahapetyan", "invalid_email", "077554581"),          
        ("Lusine", "Nahapetyan", "lusinenahapetyan@gmail.com", "abc123"),
    ]
)
def test_fill_form_negative(setup_browser, first_name, last_name, email, phone):
    driver = setup_browser

    driver.find_element(By.ID, "firstName").send_keys(first_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    driver.find_element(By.ID, "userEmail").send_keys(email)
    driver.find_element(By.ID, "userNumber").send_keys(phone)
    
    time.sleep(1)
    
    
    if first_name == "":
        assert driver.find_element(By.ID, "firstName").get_attribute("value") == ""
    if last_name == "":
        assert driver.find_element(By.ID, "lastName").get_attribute("value") == ""
    if "@" not in email:
        assert "@" not in driver.find_element(By.ID, "userEmail").get_attribute("value")
    if not phone.isdigit():
        assert not driver.find_element(By.ID, "userNumber").get_attribute("value").isdigit()

