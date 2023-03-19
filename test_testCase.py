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

# TC Positive Homepage Navigation


def test_positive_homepage_navigation(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    response_data = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nava")))
    time.sleep(2)
    assert response_data.text == "PRODUCT STORE"

# TC Positive Product Purchase


def test_positive_product_purchase(browser):
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
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "//button[contains(text(),'Place Order')]").click()
    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("Syarif Ridhohidayatulloh")
    driver.find_element(By.ID, "country").send_keys("Indonesia")
    driver.find_element(By.ID, "city").send_keys("Jakarta")
    driver.find_element(By.ID, "card").send_keys("111 222 333 444 555")
    driver.find_element(By.ID, "month").send_keys("March")
    driver.find_element(By.ID, "year").send_keys("2023")
    driver.find_element(By.XPATH,
                        "//button[contains(text(),'Purchase')]").click()
    driver.find_element(
        By.XPATH, "//body/div[10]/div[7]/div[1]/button[1]").click()
    response_data = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nava")))
    assert response_data.text == "PRODUCT STORE"

# TC Positive Contact Form


def test_positive_contact_form(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(
        By.XPATH, "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[2]/a[1]").click()
    time.sleep(3)
    driver.find_element(
        By.ID, "recipient-email").send_keys("testDummy@gmail.com")
    driver.find_element(By.ID, "recipient-name").send_keys("Dummy")
    driver.find_element(By.ID, "message-text").send_keys("Test")

    driver.find_element(
        By.XPATH, "//body/div[@id='exampleModal']/div[1]/div[1]/div[3]/button[2]").click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    response_data = driver.switch_to.alert.text
    assert response_data == "Thanks for the message!!"


# TC Negative Contact Form Validation = Failed

def test_negative_contact_form_validation(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(
        By.XPATH, "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[2]/a[1]").click()
    time.sleep(3)
    driver.find_element(
        By.ID, "recipient-email").send_keys("testDummy")
    driver.find_element(By.ID, "recipient-name").send_keys("Dummy")
    driver.find_element(By.ID, "message-text").send_keys("Test")

    driver.find_element(
        By.XPATH, "//body/div[@id='exampleModal']/div[1]/div[1]/div[3]/button[2]").click()
    time.sleep(3)
    try:
        response_data = WebDriverWait(driver, 10).until(EC.alert_is_present())
        response_text = response_data.text
        driver.switch_to.alert.accept()
        assert response_text == "Thanks for the Please fill in the data correctly!!"

    except:
        pytest.fail("Pengujian Failed")


# TC Positive Login Fonctionality
def test_positive_login_functionality(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.ID, "login2").click()
    time.sleep(2)
    driver.find_element(By.ID, "loginusername").send_keys("admin")
    driver.find_element(By.ID, "loginpassword").send_keys("admin")
    driver.find_element(
        By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[2]").click()
    response_data = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser")))
    time.sleep(2)
    assert response_data.text == "Welcome admin"
    driver.find_element(By.ID, "logout2").click()
    response_logout = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nava")))
    assert response_logout.text == "PRODUCT STORE"

# TC Negaitve invalid data login Fonctionality


def test_negative1_login_functionality(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.ID, "login2").click()
    time.sleep(2)
    driver.find_element(By.ID, "loginusername").send_keys("anon")
    driver.find_element(By.ID, "loginpassword").send_keys("anon")
    driver.find_element(
        By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[2]"
    ).click()
    time.sleep(3)
    try:
        response_data = WebDriverWait(driver, 10).until(EC.alert_is_present())
        response_text = response_data.text
        driver.switch_to.alert.accept()
        assert response_text == "Wrong password."
    except:
        pytest.fail("Alert not found.")


# TC Negative  blank username Login Fonctionality


def test_negative2_login_functionality(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.ID, "login2").click()
    time.sleep(2)
    driver.find_element(By.ID, "loginusername").send_keys("")
    driver.find_element(By.ID, "loginpassword").send_keys("admin")
    driver.find_element(
        By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[2]"
    ).click()
    time.sleep(3)
    try:
        response_data = WebDriverWait(driver, 10).until(EC.alert_is_present())
        response_text = response_data.text
        driver.switch_to.alert.accept()
        assert response_text == "Please fill out Username and Password."
    except:
        pytest.fail("Alert not found.")


# TC Positive Register Functionality

def test_positive_register_functionality(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)
    driver.find_element(By.ID, "sign-username").send_keys("tarikanzz")
    driver.find_element(By.ID, "sign-password").send_keys("gaszz")
    driver.find_element(
        By.XPATH, "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[2]").click()
    time.sleep(2)
    try:
        response_data = WebDriverWait(driver, 10).until(EC.alert_is_present())
        response_text = response_data.text
        driver.switch_to.alert.accept()
        assert response_text == "Sign up successful."
    except:
        pytest.fail(
            "Pengujian Failed : This user already exist. Harap Ubah data terlebih dahulu")


# TC Negative Register Functionality short = FAILED
def test_negative_register_functionality(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)
    driver.find_element(By.ID, "sign-username").send_keys("mmzz")
    driver.find_element(By.ID, "sign-password").send_keys("aazz")
    driver.find_element(
        By.XPATH, "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[2]").click()
    time.sleep(2)
    try:
        response_data = WebDriverWait(driver, 10).until(EC.alert_is_present())
        response_text = response_data.text
        driver.switch_to.alert.accept()
        assert response_text == "Please fill in the data correctly"
    except:
        pytest.fail("Pengujian Failed")

# TC Negative Register Functionality Blank DATA


def test_negative_register_blankData_functionality(browser):
    driver = browser
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)
    driver.find_element(By.ID, "sign-username").send_keys("")
    driver.find_element(By.ID, "sign-password").send_keys("")
    driver.find_element(
        By.XPATH, "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[2]").click()
    time.sleep(2)
    try:
        response_data = WebDriverWait(driver, 10).until(EC.alert_is_present())
        response_text = response_data.text
        driver.switch_to.alert.accept()
        assert response_text == "Please fill out Username and Password."
    except:
        pytest.fail("Pengujian Failed")
