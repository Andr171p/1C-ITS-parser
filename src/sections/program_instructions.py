"""Инструкции по учету в программах 1С"""

from typing import List

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils import _get_sidebar_main_menu
from src.constants import AVAILABLE_SIDEBAR_IDS


INSTRUCTIONS = [
    "Изменения в программах 1С",
    "Ответы специалистов 1С",
    "1С:Бухгалтерия 8 в примерах",
    "1С:ЗУП 8 в примерах",
    "1С:ERP, 1С:КА, 1С:УПП и 1С:УТ в примерах",
    "1С:Розница в примерах",
    "1С:УНФ 8 в примерах",
    "1С:Предприниматель в примерах",
    "1С:БГУ 8 в примерах",
    "1С:ЗКГУ и 1С:ЗКБУ в примерах",
    "1С:Бухгалтерия НКО 8 в примерах",
    "Сервисы 1С",
    "1С:Медицина",
    "Методическая поддержка продуктов 1С",
    "Документация для пользователей 1С",
]


def get_program_instructions(driver: webdriver.Chrome) -> ...:
    # sidebar = _get_sidebar_main_menu(driver)
    menu_element = (
        WebDriverWait(driver, 10)
        .until(EC.element_to_be_clickable((By.XPATH, "//a[@id='menu_element_i1c']")))
    )
    menu_element.click()

    results = {}
    for name in INSTRUCTIONS:
        try:
            section = (
                WebDriverWait(driver, 10)
                .until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{name}']")))
            )
            section.click()

            sidebar_sublist = driver.find_element(By.XPATH, "//div[@id='sidebar_sublist']")
            # sidebar_subsection = sidebar_sublist.find_element(By.XPATH, "//ul[contains(@style, 'display: block')]")

            # subsection_elements = sidebar_subsection.find_elements(By.TAG_NAME, "li")
            subsection_elements = sidebar_sublist.find_elements(By.TAG_NAME, "li")
            subsections = [
                subsection_element.text
                for subsection_element in subsection_elements
                if subsection_element.text.strip() != ""
            ]

            # all_a_tags = sidebar_subsection.find_elements(By.TAG_NAME, "a")
            all_a_tags = sidebar_sublist.find_elements(By.TAG_NAME, "a")
            urls = [a.get_attribute("href") for a in all_a_tags if a.get_attribute("href")]

            results.update({subsection: url for subsection, url in zip(subsections, urls)})
        except Exception as ex:
            print(ex)
            driver.back()
    print(results)
    return results

