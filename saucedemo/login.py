import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_failed_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("haitest")
        driver.find_element(By.NAME,"login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", error_message)

    def test_a_failed_login_password(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR,"[data-test='password']").send_keys("salah_pw")
        driver.find_element(By.NAME,"login-button").click()
        # error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        # self.assertIn("Epic sadface: Password is required", error_message)
    
    def test_a_success_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR,"[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME,"login-button").click()
        #baseLogin.inputLogin(driver, inputan.valid_user, inputan.valid_password)
        #driver.maximize_window()

    def tearDown(self):
        self.browser.close()
        
        #driver.find_element(By.ID,"user-name").send_keys("standard_user")
    # steps
    # driver = self.browser #buka web browser
    # driver.get("https://www.saucedemo.com/") # buka situs
    # time.sleep(3)
    # driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
    # time.sleep(1)
    # driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
    # time.sleep(1)
    # driver.find_element(By.ID, "login-button").click()
    # time.sleep(1)

# validasi
# response_data = driver.find_element(By.CLASS_NAME,"title").text
# self.assertIn('PRODUCTS', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()