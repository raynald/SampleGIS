import unittest
from selenium import webdriver
import time

def find_by_xpath(driver, xpath):
    web_elem = driver.find_element_by_xpath(xpath)
    if not web_elem:
        raise Exception('Cannot find this element!')
    return web_elem

def find_by_id(driver, elem_id):
    web_elem = driver.find_element_by_id(elem_id)
    if not web_elem:
        raise Exception('Cannot find this element!')
    return web_elem

def find_by_name(driver, name):
    web_elem = UiBase.driver.find_element_by_name(name)
    if not web_elem:
        raise Exception('Cannot find this element!')
    return web_elem

def find_by_label(driver, label):
    _xpath = "//button[text()='%s']" % (label)
    return find_by_xpath(driver, _xpath)

driver = webdriver.Firefox()
driver.implicitly_wait(65)
driver.maximize_window()
base_url = 'http://localhost:6543'
driver.get(base_url)
assert 'ICI House' in driver.page_source
find_by_label(driver, 'ICI House').click()
time.sleep(3)
inp = find_by_id(driver, 'pac-input')
inp.send_keys("Zurich\n")
time.sleep(3)
assert 'Projektwettbewerb' in driver.page_source
driver.quit()
