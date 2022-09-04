from selenium.webdriver.common.by import By

last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
article_locator = By.CSS_SELECTOR, 'article'
search_icon_locator = By.CSS_SELECTOR, 'span.tm-svg-icon__wrapper'
search_input_locator = By.XPATH, '//*[@class="tm-input-text-decorated__input"]'
search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__item'
empty_res_locator = By.XPATH, '//*[@data-test-id="empty-placeholder-text"]'