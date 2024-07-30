import time
from pages.base_page import BasePage
from pages.SBIS.locators import MainPageLocators
import allure
from pages.SBIS.header import Header
from pages.SBIS.footer import Footer


class SbisMainPage(BasePage):
    @allure.step('Переход на главную страницу портала "sbis.ru"')
    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser=self.browser)
        self.locators = MainPageLocators
        self.header = Header(browser=self.browser)
        self.footer = Footer(browser=self.browser)
        time.sleep(1)
