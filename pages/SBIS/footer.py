from pages.SBIS.locators import FooterLocators
from pages.web_element import WebElement


class Footer:
    def __init__(self, browser):
        self.locators = FooterLocators
        self.browser = browser
        self.download_local_versions = WebElement(browser=self.browser, locator=self.locators.DOWNLOAD_LOCAL,
                                                  description='"Скачать локальные версии" в футере')
