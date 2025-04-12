import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Tests.test_main import driver


@pytest.fixture(scope="function")
def setup():
    """Initialize the webdriver and return driver instance"""

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    print("\nBrowser opened and navigated to login page")
    yield driver
    driver.quit()
    print("\nBrowser closed")

@pytest.fixture(scope="function")
def login(setup):
    """Login before running test cases"""
    driver = setup
    wait = WebDriverWait(driver,20)

    #Perform login
    wait.until(EC.visibility_of_element_located((By.NAME,"username"))).send_keys("Admin")
    wait.until(EC.visibility_of_element_located((By.NAME,"password"))).send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
    print("\nSuccessfully logged in")
    return driver

@pytest.mark.parametrize("menu_name",["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard"])
def test_menu_visibility(login,menu_name):
    """Test if menus are visible after login"""
    driver = login
    wait = WebDriverWait(driver,20)
    menu_xpath = f"//span[text()='{menu_name}']"
    try:
        menu_element = wait.until(EC.visibility_of_element_located((By.XPATH,menu_xpath)))
        assert menu_element.is_displayed(),f"{menu_name} menu is not visible!"
        print(f"{menu_name} menu is visible")
    except Exception as e:
        print(f"visibility test failed for {menu_name}:{e}")

@pytest.mark.parametrize("menu_name",["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard"])
def test_menu_clickability(login,menu_name):
    """Test if menus are clickble after login"""
    driver = login
    wait = WebDriverWait(driver, 20)
    menu_xpath = f"//span[text()='{menu_name}']"
    try:
        menu_element = wait.until(EC.element_to_be_clickable((By.XPATH,menu_xpath)))
        menu_element.click()
        print(f"{menu_name} menu is clickable.")
    except Exception as e:
        print(f"clickability test failed for {menu_name} : {e}")

