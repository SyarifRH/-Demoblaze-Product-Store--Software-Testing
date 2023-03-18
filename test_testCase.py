import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_homepage_navigation(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    response_data = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nava")))
    time.sleep(2)
    assert response_data.text == "PRODUCT STORE"


def test_product_purchase(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Laptops')]").click()
    time.sleep(2)
    driver.find_element(
        By.XPATH, "//a[contains(text(),'MacBook air')]").click()
    time.sleep(3)
    driver.find_element(
        By.XPATH, "//body/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]").click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Cart')]").click()
    time.sleep(2)
    response_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'MacBook air')]")))
    assert response_product.text == "MacBook air"
    driver.find_element(By.XPATH,
                        "//button[contains(text(),'Place Order')]").click()
    driver.find_element(By.ID, "name").send_keys("Syarif Ridhohidayatulloh")
    driver.find_element(By.ID, "country").send_keys("Indonesia")
    driver.find_element(By.ID, "city").send_keys("Jakarta")
    driver.find_element(By.ID, "card").send_keys("111 222 333 444 555")
    driver.find_element(By.ID, "month").send_keys("March")
    driver.find_element(By.ID, "year").send_keys("2023")
    driver.find_element(By.XPATH,
                        "//button[contains(text(),'Purchase')]").click()
    response_data = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nava")))
    assert response_data.text == "PRODUCT STORE"
