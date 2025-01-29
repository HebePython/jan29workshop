from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("file:///C:/Users/HenrikBergman/Selenium%20-%2029%20Januari/demo-login-page.html")
    return driver

def teardown(driver):
    driver.quit()

def login(driver, username, password):
    
    log_inp = driver.find_element(By.ID, 'username')
    log_inp.send_keys(username)

    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys(password)

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

def check_error_message(driver):
    err_msg = driver.find_element(By.ID, "error-message")
    return err_msg.is_displayed()

def handle_error(driver):
    log_inp = driver.find_element(By.ID, 'username')
    password_element = driver.find_element(By.ID, 'password')
    log_inp.clear()
    password_element.clear()
    login(driver, "test", "test")
    time.sleep(3)
    alert_obj = driver.switch_to.alert
    assert alert_obj.text == "Login successful!"
    alert_obj.accept()
    time.sleep(2)

def check_loading_message(Driver):
    loading_message = driver.find_element(By.ID, "loading-spinner")
    return loading_message.is_displayed()
# Main
driver = setup()

try:
    login(driver, "23pkot", "23o4j23pj")
    time.sleep(5)
    if check_error_message(driver):
        print("Error message is visible")
        handle_error(driver)
        if check_loading_message(driver):
            print("Still not logged in")
        else:
            print("Logged in")
    
    else:
        print("Error message is not visible")
finally:
    time.sleep(10)
    teardown(driver)
