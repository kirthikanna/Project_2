import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excel_functions import ExcelReader
from locators import WebLocators
from common import Data
import time



@pytest.fixture(scope="function")
def driver():
    """ Setup Webdriver"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    """ Test Exectues Here"""
    yield driver ##That means run the driver until or unless all the tests which are present in test login.
    """ Cleanup after test"""
    driver.quit()

def test_login_cookies(setup):
    driver = setup
# Read Excel Data
    excel_reader = ExcelReader(Data().EXCEL_FILE, Data().SHEET_NUMBER)
    rows = excel_reader.row_count()

    for row in range(2, rows + 1):
        username = excel_reader.read_data(row, column_number=6).strip()
        password = excel_reader.read_data(row, column_number=7).strip()

        try:
            # Login using username and password
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, WebLocators().USERNAME_INPUT_BOX))).send_keys(username)

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, WebLocators().PASSWORD_INPUT_BOX))).send_keys(password)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, WebLocators().SUBMIT_BUTTON))).click()

            # Wait for successful login
            WebDriverWait(driver, 10).until(lambda a: Data().DASHBOARD_URL in a.current_url)

            print(f" SUCCESS: Login Successful for USERNAME={username} and PASSWORD={password}")
            excel_reader.write_data(row, 8, "TEST PASSED")

            # capture cookies after successful login
            cookies = driver.get_cookies()
            print(f"captured cookies for {username}: {cookies}")
            # quit the current session
            driver.quit()

            # start a new session
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(Data().URL)

            for cookie in cookies:
                driver.add_cookie(cookie)

            # Refresh to apply cookies
            driver.refresh()
            time.sleep(3)
            #verify login via cookies
            assert Data().DASHBOARD_URL in driver.current_url, "Login using cookies failed"
            print(f"Logged Back In using cookies!")

            try:
                # Logout
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.NAME, WebLocators().LOGOUT_BUTTON))).click()

                WebDriverWait(driver, 10).until(EC.url_contains("/auth/login"))
                print(f"Successfully logged out")
            except Exception as e:
                print(f"Warning: Logout failed! Exception: {e}")

        except Exception as e:
            print(f" ERROR: Login Successful for USERNAME={username} and PASSWORD={password}")
            excel_reader.write_data(row, 8, "TEST Failed")
        finally:
            driver.quit()









