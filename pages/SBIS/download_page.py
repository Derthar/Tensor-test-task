import time
from pages.base_page import BasePage
from pages.SBIS.locators import DownloadPageLocators
import allure
from pages.SBIS.header import Header
from pages.SBIS.footer import Footer
from pages.web_element import WebElement


class SbisDownloadPage(BasePage):
    @allure.step('Переход на страницу загрузок портала "sbis.ru"')
    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser=self.browser)
        self.locators = DownloadPageLocators
        self.header = Header(browser=self.browser)
        self.footer = Footer(browser=self.browser)
        self.plugin_download = WebElement(browser=self.browser, locator=self.locators.DOWNLOAD_PLUGIN_EXE,
                                          description='Скачать веб-установщик')
        time.sleep(1)
