import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest
from Tests.test_base import login

def test_create_newuser(login):
    """Test case:create a new user"""
    driver = login
    wait = WebDriverWait(driver,20)
    #Navigate to admin menu
    print("Clicking Admin menu")
    wait.until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Admin"]'))).click()
     #Click "Add" Button
    print("Clicking Add Button")
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[text()=" Add "]'))).click()

    #Fill new user details
    print("Selecting user role")
    user_role_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'oxd-select-text-input')])[1]")))
    user_role_dropdown.click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='listbox']//span[text()='Admin']"))).click()
    #wait.until(EC.element_to_be_clickable((By.XPATH,'//div[text()="Admin"]'))).click()
    time.sleep(10)

    print("Typing Employee Name")
    employee_name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Type for hints...']")))
    employee_name.send_keys("James  Butler")
    time.sleep(10)
   # # print(driver.page_source)

    print("Clicking Employee name from suggestion")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']")))
    employee_name_suggestion = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[contains(text(),'James  Butler')]")))
    employee_name_suggestion.click()

    print("Clicking Status dropdown")
    status_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'oxd-select-text-input')])[2]")))
    status_dropdown.click()
    time.sleep(2)
   # #  print(driver.page_source)
   #
    print("Selecting status: Enabled")#"//div[@role='listbox']//span[(text()='Enabled')]"
    enabled_option = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='listbox']//span[text()='Enabled']")))
    enabled_option.click()
    time.sleep(2)
    #driver.execute_script("arguments[0].click();", enabled_option)

    print("Typing username")
    user_name = wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")))
    user_name.send_keys("TestUser04")
    time.sleep(2)

    print("Typing Password")
    password = wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@type='password'])[1]")))
    password.send_keys("Test@123")
    time.sleep(2)

    print("Typing confirm password")
    confirm_password = wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@type='password'])[2]")))
    confirm_password.send_keys("Test@123")
    time.sleep(2)
    #
    print("Clicking save button")
    submit =wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()=' Save ']")))
    submit.click()
    time.sleep(2)
    #Verify user creation
    print("waiting for user to appear in list")
    wait.until(EC.presence_of_element_located((By.XPATH,f"//div[text()='TestUser04']")))
    print("\nNew user 'TestUser04' created successfully.")

def test_new_user_login(setup):
    driver = setup
    wait = WebDriverWait(driver, 20)

    # Perform login
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("TestUser04")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Test@123")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print("\nSuccessfully logged in")











