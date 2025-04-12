import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def setup():
    """Initialize webdriver and return the instance"""

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

#Parameterizinig login credentials
@pytest.mark.parametrize("username,password",[("Admin","admin123")])

def test_home(setup,username,password):
    """ Verify whether the home URL is accessible"""
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #wait for the dashboard to load
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"body")))

    #Get the current url after loading
    current_url = driver.current_url

    #Assertion : Check if the current url matches the expected home url
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "Home URL is not working!"
    print("Home URL is working correctlyl!")

