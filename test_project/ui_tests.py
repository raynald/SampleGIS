"""
UI Test for this application
"""
from selenium import webdriver
import time

def find_by_xpath(driver_, xpath):
    """
    :param driver_:
    :param xpath:
    :return: web element found by xpath
    """
    web_elem = driver_.find_element_by_xpath(xpath)
    if not web_elem:
        raise Exception('Cannot find this element!')
    return web_elem

def find_by_id(driver_, elem_id):
    """
    :param driver_:
    :param elem_id:
    :return: web element found by id
    """
    web_elem = driver_.find_element_by_id(elem_id)
    if not web_elem:
        raise Exception('Cannot find this element!')
    return web_elem

def find_by_name(driver_, name):
    """
    :param driver_:
    :param name:
    :return: web element found by name
    """
    web_elem = driver_.find_element_by_name(name)
    if not web_elem:
        raise Exception('Cannot find this element!')
    return web_elem

def find_by_label(driver_, label):
    """
    :param driver:
    :param label:
    :return: web element found by label
    """
    _xpath = "//button[text()='%s']" % (label)
    return find_by_xpath(driver_, _xpath)

def test_my_app():
    # Driver configuration
    driver = webdriver.Firefox()
    driver.implicitly_wait(65)
    driver.maximize_window()

    base_url = 'http://localhost:6543'
    # Open base_url
    driver.get(base_url)
    # Assert result
    assert 'ICI House' in driver.page_source
    find_by_label(driver, 'ICI House').click()
    time.sleep(3)
    # Search for a city
    inp = find_by_id(driver, 'pac-input')
    inp.send_keys("Zurich\n")
    time.sleep(3)
    # Assert result
    assert 'Projektwettbewerb' in driver.page_source
    # Leaving the test
    driver.quit()
