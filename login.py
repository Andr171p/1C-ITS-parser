import time
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


def login(username: str, password: str) -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(...)
        logger.info("Open main page of its.1c.ru")
        login_button = (
            WebDriverWait(driver, 10)
            .until(EC.element_to_be_clickable((By.XPATH, "//a[@id='login']")))
        )
        login_button.click()
        logger.info("Click to enter button")

        portal_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Войти через Портал 1С:ИТС']"))
        )
        portal_button.click()
        logger.info("Click to login portal button")

        username_form = (
            WebDriverWait(driver, 10)
            .until(EC.presence_of_element_located((By.ID, "username")))
        )
        username_form.clear()
        username_form.send_keys(username)
        logger.info("Username entered")

        time.sleep(3)

        password_form = (
            WebDriverWait(driver, 10)
            .until(EC.presence_of_element_located((By.ID, "password")))
        )
        password_form.clear()
        password_form.send_keys(password)
        logger.info("Password entered")

        submit_button = (
            WebDriverWait(driver, 10)
            .until(EC.element_to_be_clickable((By.XPATH, "//input[@id='loginButton']")))
        )
        submit_button.click()
        logger.info("Click submit button")

        time.sleep(5)

        logger.info("User login successfully")
    except Exception as ex:
        logger.error(ex)
    finally:
        return driver


if __name__ == "__main__":
    from settings import settings

    logging.basicConfig(level=logging.INFO)
    driver = login(settings.its.login, settings.its.password)
