from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def _get_sidebar_main_menu(driver: webdriver.Chrome) -> Optional[WebElement]:
    sidebar = driver.find_element(By.ID, "sidebar_main_menu")
    return sidebar
