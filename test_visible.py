import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




@pytest.fixture(scope="function")
def setup():
    """Initialize the webdriver and return driver instance"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver #Return driver for the test case
    driver.quit() #Close the browser after the test
    print("\nBrowser closed.")  # Print message

def test_visiblity(setup):
    """Test to check if username and password fields are visible"""

    driver = setup
    wait = WebDriverWait(driver,20)

    print("\nChecking if username and password fields are visible...")  # Print message

    #Wait for username and password fields to be visible
    username_field = wait.until(EC.visibility_of_element_located((By.NAME,"username")))
    password_field = wait.until(EC.visibility_of_element_located((By.NAME,"password")))


    #Assertions
    assert username_field.is_displayed(),"username field is not visible!"
    assert password_field.is_displayed(),"password field is not visible!"
    print("\n✅ Test Passed: Username and password fields are visible.")  # Print message
