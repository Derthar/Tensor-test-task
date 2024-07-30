from pages.SBIS.locators import HeaderLocators
from pages.web_element import WebElement


class Header:
    def __init__(self, browser):
        self.locators = HeaderLocators
        self.browser = browser
        self.contacts = WebElement(browser=self.browser, locator=self.locators.CONTACTS,
                                   description='"Контакты" в хедере')
