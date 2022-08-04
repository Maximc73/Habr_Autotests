import time

from selenium.webdriver.common.by import By
from first_try import setup, tear_down


def test_empty_search(driver):
    # открыть поиск
    search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__item'
    search_button_element = driver.find_element(*search_button_locator)
    search_button_element.click()
    time.sleep(2)
    # вбить текст
    search_input_locator = By.XPATH, '//*[@class="tm-input-text-decorated__input"]'
    search_input_element = driver.find_element(*search_input_locator)
    text_to_search = 'rtrrtrtrttrrt'
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
    # проверить текст
    empty_res_locator = By.XPATH, '//*[@data-test-id="empty-placeholder-text"]'
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')

if __name__ == '__main__':
    driver = setup()

    test_empty_search(driver)

    tear_down(driver)


