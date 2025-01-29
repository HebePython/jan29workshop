from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("file:///C:/Users/HenrikBergman/Selenium%20-%2029%20Januari/demo-login-page.html")

log_inp = driver.find_element(By.ID, 'username')
log_inp.send_keys("it7dufyui")

password_element = driver.find_element(By.ID, 'password')
password_element.send_keys("wuthwiwt")

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

err_msg = driver.find_element(By.ID, "error-message")

time.sleep(3)

if err_msg.is_displayed():
    loading_message = driver.find_element(By.ID, 'loading-spinner')
    print("Error message is visible")
    log_inp.clear()
    password_element.clear()
    log_inp.send_keys("test")
    password_element.send_keys("test")
    login_button.click()
    if loading_message.is_displayed():
        print("STILL NOT LOGGED IN")
    time.sleep(3)
    alert_obj = driver.switch_to.alert
    assert alert_obj.text == "Login successful!"
    alert_obj.accept()
    time.sleep(2)

    if loading_message.is_displayed():
        print("STILL NOT LOGGED IN")
    else:
        print("WE LOGGED IN")
else:
    print("Error message is not visible")

time.sleep(10)




