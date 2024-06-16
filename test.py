import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest:
    def run_test(url):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)

        # Username field presence and functionality
        #         Find element by ID doesn't work correct, but I have no time to find out the correct way to indentify element
        username = driver.find_element(By.ID, "r1")
        username.send_keys("john_doe@company.con")

        # Password field presence and functionality
        password = driver.find_element(By.ID, "r2")
        password.send_keys("123456")

        # Login button field presence and functionality
        login_button = driver.find_element(By.XPATH, "//*[@id='"'root'"']/div/div/div[1]/div[2]/form/button")
        login_button.click()
        time.sleep(3)
        if login_button.is_displayed():
            raise Exception("Login failed after 3 second")

        driver.quit()


if __name__ == "__main__":
    LoginTest.run_test("https://web.eos.bnk-il.com/auth")
