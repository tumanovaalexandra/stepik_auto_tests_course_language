from selenium.webdriver.common.by import By
import time


def test_find_add_to_card(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(30)
    assert len(button) > 0