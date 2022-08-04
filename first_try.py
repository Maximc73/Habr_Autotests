import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def setup():
    print('set up')
    driver = webdriver.WebDriver(executable_path='chromedriver.exe')

    driver.get('https://habr.com/ru/all/')
    time.sleep(2)
    return driver

def tear_down(driver):
    print('tear down')
    driver.quit()

def test_basic_search(driver):
    # поиск поля для поиска
    search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__item'
    search_button_element = driver.find_element(*search_button_locator)
    search_button_element.click()
    time.sleep(1)

    # вбить текст
    search_input_locator = By.XPATH, '//*[@class="tm-input-text-decorated__input"]'
    search_input_element = driver.find_element(*search_input_locator)
    text_to_search = 'ffgrgdfg'
    search_input_element.send_keys(text_to_search)
    time.sleep(2)

    # нажать на иконку поиска
    search_icon_locator = By.CSS_SELECTOR, 'span.tm-svg-icon__wrapper'
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(2)

    # посчитать количество записей
    article_locator = By.CSS_SELECTOR, 'article'
    articles = driver.find_elements(*article_locator)
    print(f'Number of articles is {len(articles)}')
    time.sleep(1)

    # посчитать количество страниц
    last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
    last_page_number = driver.find_element(*last_page_locator)
    element_text = last_page_number.text
    print(f'Number of page is {element_text}')
    time.sleep(1)


if __name__ == '__main__':
    driver = setup()
    try:
        test_basic_search(driver)
    except NoSuchElementException as error:
        print(f'Test failed, reason {error}')

    tear_down(driver)
