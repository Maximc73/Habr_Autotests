import time
from locators import *
from selenium.common.exceptions import NoSuchElementException

def count_pages_number(driver):
    # посчитать количество страниц
    last_page_number = driver.find_element(*last_page_locator)
    element_text = last_page_number.text
    print(f'Number of page is {element_text}')
    time.sleep(1)

def go_to_last_page(driver):
    # кликнуть на последнюю страницу
    last_page = driver.find_element(*last_page_locator)
    last_page.click()

def count_articles_number(driver):
    # посчитать количество записей
    articles = driver.find_elements(*article_locator)
    print(f'Number of articles is {len(articles)}')
    time.sleep(1)

def click_search_button(driver):
    # нажать на иконку поиска
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(2)

def type_text(driver, text):
    # вбить текст
    search_input_element = driver.find_element(*search_input_locator)
    text_to_search = text
    search_input_element.send_keys(text_to_search)
    time.sleep(2)

def click_search_form(driver):
    # поиск поля для поиска
    search_button_element = driver.find_element(*search_button_locator)
    search_button_element.click()
    time.sleep(1)

def check_empty_page_text(driver):
    # проверить текст
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')

