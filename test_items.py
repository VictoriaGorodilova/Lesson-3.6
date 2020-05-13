from selenium import webdriver
import time

def test_add_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert len(browser.find_elements_by_css_selector("#add_to_basket_form"))>0, "корзинка не найдена"
