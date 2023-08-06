import logging
from abc import abstractmethod

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class PageObject(object):
    """Base class for Page objects for web_1-based applications"""

    url = None

    # TODO: Handle StaleElementException problems
    # TODO: Find elements. Wait until elem is not present
    def __init__(self, webdriver, url=None, timeout=30):
        self.webdriver = webdriver
        self.url = url
        self.timeout = timeout
        self.webdriver.set_page_load_timeout(timeout)

    def navigate(self):
        self.webdriver.get(self.url)
        return self.validate_page()

    @abstractmethod
    def validate_page(cls):
        return

    def find_element(self, locator, element, wait=3, retries=3):
        """Find element on page.
        Function retries @retries times, waiting @wait seconds after each iteration"""
        result = None
        for _ in range(retries):
            try:
                result = WebDriverWait(self.webdriver, wait).until(lambda x: x.find_element(locator, element))
                logging.debug("Element '{}' found".format(element))
                break
            except (NoSuchElementException, TimeoutException):
                logging.debug("Element could not be found. Retrying...".format(element))
            except Exception as ex:
                logging.exception("An error occurred when trying to find element with ID '{}'".format(element))
                raise
        else:
            logging.debug("Element '{}':'{}' could not be found".format(locator, element))
        return result

    def find_elements(self, by_locator, locator_value, wait=3, retries=3):
        """Function retries @retries times, waiting @wait seconds after each iteration"""
        # for _ in retries:
        raise NotImplemented


if __name__ == "__main__":
    # TODO: Delete
    driver = webdriver.Chrome()
    pp = PageObject(driver)
    pp.webdriver.get("https://www.google.com")
    print(pp.find_element(By.ID, "lst-ib"))
    print(pp.find_element(By.CLASS_NAME, "gsfi"))
    print(pp.find_element(By.XPATH, '//*[@id="lst-ib"]'))
    print(pp.find_element(By.LINK_TEXT, "Google Search"))
    pp.webdriver.close()
