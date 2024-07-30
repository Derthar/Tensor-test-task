import time

from pages.base_page import BasePage
from pages.TENSOR.locators import MainPageLocators
import allure
from pages.web_element import WebElement, WebElements


class TensorMainPage(BasePage):
    @allure.step('Переход на главную страницу портала "tensor.ru"')
    def __init__(self, browser):
        # time.sleep(1)
        self.browser = browser
        super().__init__(browser=self.browser)
        self.locators = MainPageLocators
        self.power_in_people_block = WebElement(browser=self.browser, locator=self.locators.POWER_IN_PEOPLE_BLOCK,
                                                description='Блок "Сила в людях"')
        self.power_in_people_title = WebElement(browser=self.browser, locator=self.locators.POWER_IN_PEOPLE_TITLE,
                                                description='Заголовок блока "Сила в людях"')
        self.power_in_people_detailed = WebElement(browser=self.browser, locator=self.locators.POWER_IN_PEOPLE_DETAILED,
                                                   description='Кнопка "Подробнее" в блоке Сила в людях"')
        time.sleep(1)

